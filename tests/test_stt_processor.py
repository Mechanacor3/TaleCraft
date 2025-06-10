from backend.src.audio_processing.stt import STTProcessor


def test_get_and_set_model():
    stt = STTProcessor(model="model1")
    assert stt.get_model() == "model1"
    stt.set_model("model2")
    assert stt.get_model() == "model2"
