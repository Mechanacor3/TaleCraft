from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.script_alignment_agent import ScriptAlignmentAgent

router = APIRouter()
script_agent = ScriptAlignmentAgent()


class AlignScriptRequest(BaseModel):
    images: list[str]
    script: str


class EditScriptRequest(BaseModel):
    new_script: str


@router.post("/align_script")
async def align_script(request: AlignScriptRequest):
    if not request.images or not request.script:
        raise HTTPException(status_code=400, detail="Images and script are required.")

    aligned_script = script_agent.align_script_with_images(
        request.images, request.script
    )
    return {"aligned_script": aligned_script}


@router.put("/edit_script")
async def edit_script(request: EditScriptRequest):
    if not request.new_script:
        raise HTTPException(status_code=400, detail="New script is required.")

    updated_script = script_agent.update_script(request.new_script)
    return {"updated_script": updated_script}
