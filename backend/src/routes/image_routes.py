from fastapi import FastAPIRouter, HTTPException
from routes import image_routes, story_routes, script_routes, tts_routes, video_routes
t ImageGenerationAgent
app = FastAPI()

app.include_router(image_routes.router, prefix="/images", tags=["images"])
app.include_router(story_routes.router, prefix="/stories", tags=["stories"])
app.include_router(script_routes.router, prefix="/scripts", tags=["scripts"])t(BaseModel):
app.include_router(tts_routes.router, prefix="/tts", tags=["tts"])
app.include_router(video_routes.router, prefix="/videos", tags=["videos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)@router.post("/regenerate-image")
async def regenerate_image(request: RegenerateImageRequest):
    try:
        new_image_url = image_agent.regenerate_image(request.image_id, request.new_prompt)
        return {"new_image_url": new_image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))