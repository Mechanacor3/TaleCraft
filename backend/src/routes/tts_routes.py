from flask import Blueprint, request, jsonify
from src.agents.tts_agent import TTSAgent

tts_routes = Blueprint('tts_routes', __name__)
tts_agent = TTSAgent()

@tts_routes.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text')
    voice_style = data.get('voice_style')

    if not text or not voice_style:
        return jsonify({'error': 'Text and voice style are required.'}), 400

    audio_clip = tts_agent.generate_audio(text, voice_style)
    return jsonify({'audio_clip': audio_clip}), 200

@tts_routes.route('/available_voices', methods=['GET'])
def available_voices():
    voices = tts_agent.get_available_voices()
    return jsonify({'voices': voices}), 200