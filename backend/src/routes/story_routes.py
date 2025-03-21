from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.story_agent import StoryAgent

router = APIRouter()
story_agent = StoryAgent()

class StoryRequest(BaseModel):
    story_idea: str

class RefineOutlineRequest(BaseModel):
    outline: str
    feedback: str

@router.post("/generate")
async def generate_outline(request: StoryRequest):
    try:
        outline = await story_agent.generate_outline(request.story_idea)
        return {"outline": outline}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/refine")
async def refine_outline(request: RefineOutlineRequest):
    if not request.outline or not request.feedback:
        raise HTTPException(status_code=400, detail="Outline and feedback are required.")
    
    refined_outline = await story_agent.refine_outline(request.outline, request.feedback)
    return {"outline": refined_outline}
