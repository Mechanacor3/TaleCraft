from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .routes import image_routes, story_routes, script_routes, tts_routes, video_routes
from .config import Config

app = FastAPI()

app.include_router(story_routes.router, prefix="/stories", tags=["stories"])
app.include_router(script_routes.router, prefix="/scripts", tags=["scripts"])
app.include_router(image_routes.router, prefix="/images", tags=["images"])
app.include_router(tts_routes.router, prefix="/tts", tags=["tts"])
app.include_router(video_routes.router, prefix="/videos", tags=["videos"])

# Optionally mount a prebuilt frontend if present. This is controlled by the
# SERVE_FRONTEND flag rather than DEMO_MODE so the container can always serve
# the React bundle when it is copied in during the Docker build.
if Config.SERVE_FRONTEND:
    frontend_dir = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"
    if frontend_dir.exists():
        app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
    else:
        raise Exception(f"Frontend dir {frontend_dir} does not exist")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
