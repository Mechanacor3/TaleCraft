from ..config import Config
from ..defaults import DEFAULT_IMAGE_PATH, DEFAULT_SCRIPT_LINES


class ScriptAlignmentAgent:
    def __init__(self) -> None:
        self.script: list[str] = []

    def align_script_with_images(self, images, script):
        """Align a list of script dialogue lines with the given images."""
        if Config.DEMO_MODE:
            demo_images = images or [DEFAULT_IMAGE_PATH] * len(DEFAULT_SCRIPT_LINES)
            return [
                {
                    "image": (
                        demo_images[i] if i < len(demo_images) else DEFAULT_IMAGE_PATH
                    ),
                    "dialogue": line,
                }
                for i, line in enumerate(DEFAULT_SCRIPT_LINES)
            ]

        aligned_script = []
        for i, image in enumerate(images):
            aligned_script.append(
                {"image": image, "dialogue": script[i] if i < len(script) else ""}
            )
        return aligned_script

    def adjust_dialogue(self, aligned_script, index, new_dialogue):
        """Adjust the dialogue at the specified index in the aligned script."""
        if 0 <= index < len(aligned_script):
            aligned_script[index]["dialogue"] = new_dialogue
        return aligned_script

    def generate_script_summary(self, aligned_script):
        """Generate a summary of the aligned script."""
        summary = "Script Summary:\n"
        for item in aligned_script:
            summary += f"Image: {item['image']}, Dialogue: {item['dialogue']}\n"
        return summary.strip()

    def update_script(self, new_script):
        """Replace the stored script and return the updated version."""
        self.script = list(new_script)
        return self.script
