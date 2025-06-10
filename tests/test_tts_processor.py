from backend.src.audio_processing.tts import TTSProcessor


def test_generate_audio_uses_default_voice():
    processor = TTSProcessor()
    clip = processor.generate_audio("hello")
    assert clip == "Audio clip for 'hello' with voice style 'default'"


def test_set_voice_style_changes_generation():
    processor = TTSProcessor()
    processor.set_voice_style("excited")
    clip = processor.generate_audio("hi")
    assert clip == "Audio clip for 'hi' with voice style 'excited'"


def test_save_audio_writes_file(tmp_path):
    processor = TTSProcessor()
    clip = processor.generate_audio("testing")
    file_path = tmp_path / "output.txt"
    processor.save_audio(clip, file_path)
    assert file_path.read_text() == clip
