from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter()

# In-memory data store
_DATA_STORE: Dict[str, Any] = {}

# Pydantic models
class ProgressResponseItem(BaseModel):
    course_id: str
    progress: int

class ProgressResponse(BaseModel):
    user_id: str
    progress: List[ProgressResponseItem]

class CompleteCoursePayload(BaseModel):
    course_id: str

def _calculate_progress(user_id: str, course_id: str) -> int:
    # Simulate progress calculation
    return 50  # Example progress

@router.get("/progress/{user_id}", response_model=ProgressResponse)
async def get_progress(user_id: str):
    if user_id not in _DATA_STORE:
        raise HTTPException(status_code=404, detail="User not found")

    progress_items = []
    for course_id in _DATA_STORE[user_id]["courses"]:
        progress = _calculate_progress(user_id, course_id)
        progress_items.append(ProgressResponseItem(course_id=course_id, progress=progress))

    return ProgressResponse(user_id=user_id, progress=progress_items)

@router.post("/progress/{user_id}/complete")
async def complete_course(user_id: str, payload: CompleteCoursePayload):
    if user_id not in _DATA_STORE:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.course_id not in _DATA_STORE[user_id]["courses"]:
        raise HTTPException(status_code=404, detail="Course not found")

    # Simulate course completion
    _DATA_STORE[user_id]["courses"][payload.course_id]["completed"] = True
    return {"message": "Course marked as completed"}