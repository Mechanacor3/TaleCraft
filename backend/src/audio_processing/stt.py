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
        # Implement the transcription logic using OpenAI Whisper
        pass

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
