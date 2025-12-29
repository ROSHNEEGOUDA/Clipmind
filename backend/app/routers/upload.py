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
from app.services.frame_extractor import extract_frames
from app.services.scene_analyzer import detect_scene_type
from app.services.caption_templates import generate_caption_and_hashtags

router = APIRouter()

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
CLIPS_DIR = os.path.join(os.getcwd(), "clips")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CLIPS_DIR, exist_ok=True)


def process_video_async(path: str, job_id: str):
    try:
        print(f"[JOB {job_id}] Processing started")

        #  Get duration
        duration = get_video_duration(path)
        print(f"[JOB {job_id}] Duration: {duration}")

        #  Detect highlights
        highlights = detect_highlights(duration)
        print(f"[JOB {job_id}] Highlights: {highlights}")

        if not highlights:
            print(f"[JOB {job_id}] No highlights, using fallback clip")
            highlights = [{
                "start": int(duration * 0.25),
                "duration": 5
            }]

        #  Create reel
        reel_filename = f"{job_id}_reel.mp4"
        reel_path = os.path.join(CLIPS_DIR, reel_filename)

        print(f"[JOB {job_id}] Creating reel")
        create_reel_from_chunks(
            input_path=path,
            output_path=reel_path,
            highlights=highlights
        )

        #  Extract frames
        frames_dir = os.path.join("temp_frames", job_id)
        print(f"[JOB {job_id}] Extracting frames")
        frames_paths = extract_frames(path, frames_dir)

        #  Analyze scene ( CORE LOGIC)
        scene_type = detect_scene_type(frames_paths)
        print(f"[JOB {job_id}] Scene type detected: {scene_type}")

        #  Generate caption & hashtags (RULE-BASED)
        is_animated = False
        caption, hashtags = generate_caption_and_hashtags(scene_type = scene_type, is_animated=is_animated)


        #  Save results
        RESULTS[job_id] = [{
                "video": f"/clips/{reel_filename}",
                "caption": caption,
                "hashtags": hashtags,
                "scene_type": scene_type
            }]

        print(f"[JOB {job_id}] Reel generated successfully")

    except Exception as e:
        print(f"[JOB {job_id}] Processing failed:", e)
        RESULTS[job_id] = {
            "status": "error",
            "clips": []
        }


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
