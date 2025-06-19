import os
from typing import Optional

import openai
import requests

from ..config import Config
from ..defaults import DEFAULT_IMAGE_PATH


class ImageGenerationAgent:
    def __init__(self, openai_api_key: Optional[str] = None):
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")

    def _set_api_key(self) -> None:
        if self.openai_api_key:
            openai.api_key = self.openai_api_key

    def generate_image(self, prompt: str) -> str:
        """Generate an image based on the provided prompt using DALL·E."""
        if Config.DEMO_MODE:
            # In demo mode return a placeholder image instead of calling OpenAI.
            return DEFAULT_IMAGE_PATH

        self._set_api_key()
        response = openai.Image.create(prompt=prompt, n=1)
        return response["data"][0]["url"]

    def modify_image(self, image_path: str, new_prompt: str) -> str:
        """Modify an existing image based on a new prompt."""
        if Config.DEMO_MODE:
            return DEFAULT_IMAGE_PATH

        self._set_api_key()
        with open(image_path, "rb") as img:
            response = openai.Image.create_edit(image=img, prompt=new_prompt, n=1)
        return response["data"][0]["url"]

    def regenerate_image(self, image_path: str) -> str:
        """Regenerate an image based on its ID."""
        if Config.DEMO_MODE:
            return DEFAULT_IMAGE_PATH

        self._set_api_key()
        with open(image_path, "rb") as img:
            response = openai.Image.create_variation(image=img, n=1)
        return response["data"][0]["url"]

    def get_image(self, image_id: str) -> str:
        """Retrieve an image based on its ID or URL."""
        if os.path.isfile(image_id):
            return image_id
        response = requests.get(image_id, timeout=10)
        response.raise_for_status()
        tmp_path = os.path.join("/tmp", os.path.basename(image_id))
        with open(tmp_path, "wb") as f:
            f.write(response.content)
        return tmp_path
