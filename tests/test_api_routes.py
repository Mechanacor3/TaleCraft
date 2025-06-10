from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from backend.src.app import app
from backend.src.routes import (
    story_routes,
    script_routes,
    image_routes,
    tts_routes,
    video_routes,
)

client = TestClient(app)


def test_generate_story_route():
    with patch.object(
        story_routes.story_agent,
        "generate_outline",
        AsyncMock(return_value="outline"),
    ) as mock_gen:
        response = client.post("/stories/generate", json={"story_idea": "idea"})
        assert response.status_code == 200
        assert response.json() == {"outline": "outline"}
        mock_gen.assert_awaited_once_with("idea")


def test_refine_story_route():
    with patch.object(
        story_routes.story_agent,
        "refine_outline",
        AsyncMock(return_value="refined"),
    ) as mock_refine:
        payload = {"outline": "old", "feedback": "more"}
        response = client.put("/stories/refine", json=payload)
        assert response.status_code == 200
        assert response.json() == {"outline": "refined"}
        mock_refine.assert_awaited_once_with("old", "more")


def test_align_script_route():
    aligned = [{"image": "img", "dialogue": "line"}]
    with patch.object(
        script_routes.script_agent,
        "align_script_with_images",
        return_value=aligned,
    ) as mock_align:
        payload = {"images": ["img"], "script": "line"}
        response = client.post("/scripts/align_script", json=payload)
        assert response.status_code == 200
        assert response.json() == {"aligned_script": aligned}
        mock_align.assert_called_once_with(["img"], "line")


def test_edit_script_route():
    payload = {"new_script": "abc"}
    response = client.put("/scripts/edit_script", json=payload)
    assert response.status_code == 200
    assert response.json() == {"updated_script": list("abc")}


def test_generate_image_route():
    with patch.object(
        image_routes.image_agent,
        "generate_image",
        return_value="http://img",
    ) as mock_img:
        response = client.post("/images/generate-image", json={"prompt": "cat"})
        assert response.status_code == 200
        assert response.json() == {"image_url": "http://img"}
        mock_img.assert_called_once_with("cat")


def test_modify_image_route():
    with patch.object(
        image_routes.image_agent,
        "modify_image",
        return_value="http://edited",
    ) as mock_mod:
        payload = {"image_path": "path.png", "new_prompt": "dog"}
        response = client.put("/images/modify-image", json=payload)
        assert response.status_code == 200
        assert response.json() == {"image_url": "http://edited"}
        mock_mod.assert_called_once_with("path.png", "dog")


def test_regenerate_image_route():
    with patch.object(
        image_routes.image_agent,
        "regenerate_image",
        return_value="http://var",
    ) as mock_reg:
        response = client.post(
            "/images/regenerate-image", json={"image_path": "old.png"}
        )
        assert response.status_code == 200
        assert response.json() == {"image_url": "http://var"}
        mock_reg.assert_called_once_with("old.png")


def test_generate_audio_route():
    with patch.object(
        tts_routes.tts_agent,
        "generate_audio",
        return_value="clip",
    ) as mock_audio:
        payload = {"text": "hi", "voice_style": "default"}
        response = client.post("/tts/generate_audio", json=payload)
        assert response.status_code == 200
        assert response.json() == {"audio_clip": "clip"}
        mock_audio.assert_called_once_with("hi", "default")


def test_available_voices_route():
    response = client.get("/tts/available_voices")
    assert response.status_code == 200
    assert "voices" in response.json()


def test_assemble_video_route():
    with patch.object(
        video_routes.video_agent,
        "assemble_video",
        return_value="/tmp/out.mp4",
    ) as mock_video:
        payload = {"images": ["i"], "audio": "a"}
        response = client.post("/videos/assemble_video", json=payload)
        assert response.status_code == 200
        assert response.json() == {"video_path": "/tmp/out.mp4"}
        mock_video.assert_called_once_with(["i"], "a")


def test_preview_video_route():
    payload = {"video_path": "demo.mp4"}
    response = client.post("/videos/preview_video", json=payload)
    assert response.status_code == 200
    assert response.json() == {"preview_url": {"message": "Preview generated", "video_path": "demo.mp4"}}


def test_generate_image_missing_prompt():
    with patch.object(image_routes.image_agent, "generate_image") as mock_img:
        response = client.post("/images/generate-image", json={})
        assert response.status_code == 422
        mock_img.assert_not_called()


def test_align_script_missing_fields():
    with patch.object(script_routes.script_agent, "align_script_with_images") as mock_align:
        response = client.post("/scripts/align_script", json={})
        assert response.status_code == 422
        mock_align.assert_not_called()


def test_edit_script_missing_body():
    with patch.object(script_routes.script_agent, "update_script") as mock_edit:
        response = client.put("/scripts/edit_script", json={})
        assert response.status_code == 422
        mock_edit.assert_not_called()


def test_generate_audio_missing_params():
    with patch.object(tts_routes.tts_agent, "generate_audio") as mock_audio:
        response = client.post("/tts/generate_audio", json={"text": "hello"})
        assert response.status_code == 422
        mock_audio.assert_not_called()


def test_assemble_video_missing_audio():
    with patch.object(video_routes.video_agent, "assemble_video") as mock_video:
        response = client.post("/videos/assemble_video", json={"images": ["i"]})
        assert response.status_code == 422
        mock_video.assert_not_called()


def test_preview_video_missing_path():
    with patch.object(video_routes.video_agent, "preview_video") as mock_preview:
        response = client.post("/videos/preview_video", json={})
        assert response.status_code == 422
        mock_preview.assert_not_called()

