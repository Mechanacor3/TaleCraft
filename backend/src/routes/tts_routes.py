from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.tts_agent import TTSAgent

router = APIRouter()
tts_agent = TTSAgent()


class GenerateAudioRequest(BaseModel):
    text: str
    voice_style: str


@router.post("/generate_audio")
async def generate_audio(request: GenerateAudioRequest):
    if not request.text or not request.voice_style:
        raise HTTPException(
            status_code=400, detail="Text and voice style are required."
        )

    audio_clip = tts_agent.generate_audio(request.text, request.voice_style)
    return {"audio_clip": audio_clip}


@router.get("/available_voices")
async def available_voices():
    voices = tts_agent.get_available_voices()
    return {"voices": voices}
