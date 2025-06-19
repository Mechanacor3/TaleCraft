from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .routes import image_routes, story_routes, script_routes, tts_routes, video_routes
from .config import Config

app = FastAPI()

if Config.DEMO_MODE:
    # In demo mode we optionally serve a built frontend from the `frontend_dist`
    # directory located at the repository root. This allows running the full
    # application locally without external dependencies.
    frontend_dir = Path(__file__).resolve().parent.parent / "frontend_dist"
    if frontend_dir.exists():
        app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

app.include_router(story_routes.router, prefix="/stories", tags=["stories"])
app.include_router(script_routes.router, prefix="/scripts", tags=["scripts"])
app.include_router(image_routes.router, prefix="/images", tags=["images"])
app.include_router(tts_routes.router, prefix="/tts", tags=["tts"])
app.include_router(video_routes.router, prefix="/videos", tags=["videos"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
