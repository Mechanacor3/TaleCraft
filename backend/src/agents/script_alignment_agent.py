class ScriptAlignmentAgent:
    def __init__(self):
        self.script: list[str] = []

    def align_script_with_images(self, images, script):
        """
        Aligns a list of script dialogue lines with the given images.

        Parameters:
        - images: List of image paths or URLs.
        - script: List of dialogue strings to be aligned.

        Returns:
        - aligned_script: A structured representation of the script aligned with images.
        """
        aligned_script = []
        for i, image in enumerate(images):
            aligned_script.append(
                {"image": image, "dialogue": script[i] if i < len(script) else ""}
            )
        return aligned_script

    def adjust_dialogue(self, aligned_script, index, new_dialogue):
        """
        Adjusts the dialogue at the specified index in the aligned script.

        Parameters:
        - aligned_script: The structured representation of the script aligned with images.
        - index: The index of the dialogue to be adjusted.
        - new_dialogue: The new dialogue text to replace the existing one.

        Returns:
        - updated_script: The updated aligned script with the modified dialogue.
        """
        if 0 <= index < len(aligned_script):
            aligned_script[index]["dialogue"] = new_dialogue
        return aligned_script

    def generate_script_summary(self, aligned_script):
        """
        Generates a summary of the aligned script.

        Parameters:
        - aligned_script: The structured representation of the script aligned with images.

        Returns:
        - summary: A summary of the script.
        """
        summary = "Script Summary:\n"
        for item in aligned_script:
            summary += f"Image: {item['image']}, Dialogue: {item['dialogue']}\n"
        return summary.strip()

    def update_script(self, new_script):
        """Replace the stored script and return the updated version."""
        self.script = list(new_script)
        return self.script

