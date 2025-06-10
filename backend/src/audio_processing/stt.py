class STTProcessor:
    def __init__(self, model):
        self.model = model

    def transcribe_audio(self, audio_file):
        """
        Convert speech to text using the specified model.
        
        Parameters:
        audio_file (str): Path to the audio file to be transcribed.

        Returns:
        str: Transcribed text from the audio.
        """
        import os
        import openai
        from openai import OpenAIError

        if not os.path.isfile(audio_file):
            raise FileNotFoundError(f"Audio file '{audio_file}' not found")

        try:
            with open(audio_file, "rb") as f:
                result = openai.Audio.transcribe(self.model, f)
        except OpenAIError as exc:
            raise RuntimeError(f"OpenAI API error: {exc}") from exc
        except Exception as exc:
            raise RuntimeError(f"Failed to transcribe audio: {exc}") from exc

        return result.get("text", "") if isinstance(result, dict) else str(result)

    def set_model(self, model):
        """
        Set the model for speech-to-text processing.
        
        Parameters:
        model (str): The model to be used for transcription.
        """
        self.model = model

    def get_model(self):
        """
        Get the current model used for speech-to-text processing.
        
        Returns:
        str: The current model.
        """
        return self.model
