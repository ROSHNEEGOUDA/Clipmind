from fastapi import APIRouter
from app.store import RESULTS

router = APIRouter()

@router.get("/results/{job_id}")
def get_results(job_id: str):
    return {
        "job_id": job_id,
        "clips": RESULTS.get(job_id, [])
    }
