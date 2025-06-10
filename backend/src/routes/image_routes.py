from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.image_generation_agent import ImageGenerationAgent

router = APIRouter()
image_agent = ImageGenerationAgent()


class ImageRequest(BaseModel):
    prompt: str


class ModifyImageRequest(BaseModel):
    image_path: str
    new_prompt: str


class RegenerateImageRequest(BaseModel):
    image_path: str


@router.post("/generate-image")
async def generate_image(request: ImageRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    try:
        image_url = image_agent.generate_image(request.prompt)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/modify-image")
async def modify_image(request: ModifyImageRequest):
    if not request.image_path or not request.new_prompt:
        raise HTTPException(
            status_code=400, detail="Image path and new prompt are required."
        )

    try:
        image_url = image_agent.modify_image(request.image_path, request.new_prompt)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/regenerate-image")
async def regenerate_image(request: RegenerateImageRequest):
    if not request.image_path:
        raise HTTPException(status_code=400, detail="Image path is required.")

    try:
        image_url = image_agent.regenerate_image(request.image_path)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
