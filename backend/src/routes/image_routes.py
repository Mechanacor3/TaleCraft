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

    data = request.json
    image_id = data.get('image_id')
    new_prompt = data.get('new_prompt')
    if not image_id or not new_prompt:
        return HTTPException({'error': 'Image ID and new prompt are required'}), 400

    try:
        new_image_url = image_agent.regenerate_image(image_id, new_prompt)
        return HTTPException({'new_image_url': new_image_url}), 200
    except Exception as e:
        return HTTPException({'error': str(e)}), 500