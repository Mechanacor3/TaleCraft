from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.image_generation_agent import ImageGenerationAgent

router = APIRouter()
image_agent = ImageGenerationAgent()


class ImageRequest(BaseModel):
    prompt: str


class RegenerateImageRequest(BaseModel):
    image_id: str
    new_prompt: str


@router.post("/generate-image")
async def generate_image(request: ImageRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    try:
        image_url = image_agent.generate_image(request.prompt)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
