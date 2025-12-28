from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil
import uuid
import threading

from app.services.video_processor import get_video_duration
from app.services.highlight_detector import detect_highlights
from app.services.clipper import create_reel_from_chunks
from app.store import RESULTS

router = APIRouter()

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
CLIPS_DIR = os.path.join(os.getcwd(), "clips")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CLIPS_DIR, exist_ok=True)


def process_video_async(path: str, job_id: str):
    try:
        # Get duration
        duration = get_video_duration(path)

        #  Detect non-continuous highlights
        highlights = detect_highlights(duration)

        if not highlights:
            print(f"[JOB {job_id}] No highlights detected")
            RESULTS[job_id] = []
            return

        #  Create ONE reel
        reel_filename = f"{job_id}_reel.mp4"
        reel_path = os.path.join(CLIPS_DIR, reel_filename)

        create_reel_from_chunks(
            input_path=path,
            output_path=reel_path,
            highlights=highlights
        )

        #  Save result (URL, not file path)
        RESULTS[job_id] = [{
            "video": f"/clips/{reel_filename}"
        }]

        print(f"[JOB {job_id}] Reel generated successfully")

    except Exception as e:
        print(f"[JOB {job_id}] Processing failed:", e)
        RESULTS[job_id] = []


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    try:
        job_id = str(uuid.uuid4())
        safe_name = file.filename.replace(" ", "_")
        file_path = os.path.join(UPLOAD_DIR, f"{job_id}_{safe_name}")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        #  Start background processing
        threading.Thread(
            target=process_video_async,
            args=(file_path, job_id),
            daemon=True
        ).start()

        return JSONResponse(
            status_code=200,
            content={
                "job_id": job_id,
                "filename": safe_name,
                "status": "uploaded_and_processing"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
