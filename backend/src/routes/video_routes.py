from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.video_assembly_agent import VideoAssemblyAgent

router = APIRouter()
video_agent = VideoAssemblyAgent()


class AssembleVideoRequest(BaseModel):
    images: list[str]
    audio: str


class PreviewVideoRequest(BaseModel):
    video_path: str


@router.post("/assemble_video")
async def assemble_video(request: AssembleVideoRequest):
    if not request.images or not request.audio:
        raise HTTPException(status_code=400, detail="Images and audio are required.")

    video_path = video_agent.assemble_video(request.images, request.audio)
    return {"video_path": video_path}


@router.post("/preview_video")
async def preview_video(request: PreviewVideoRequest):
    if not request.video_path:
        raise HTTPException(status_code=400, detail="Video path is required.")

    preview_url = video_agent.preview_video(request.video_path)
    return {"preview_url": preview_url}
