from flask import Blueprint, request, jsonify
from agents.video_assembly_agent import VideoAssemblyAgent

video_routes = Blueprint('video_routes', __name__)
video_agent = VideoAssemblyAgent()

@video_routes.route('/assemble_video', methods=['POST'])
def assemble_video():
    data = request.json
    images = data.get('images')
    audio = data.get('audio')
    
    if not images or not audio:
        return jsonify({'error': 'Images and audio are required.'}), 400
    
    video_path = video_agent.assemble_video(images, audio)
    
    return jsonify({'video_path': video_path}), 200

@video_routes.route('/preview_video', methods=['POST'])
def preview_video():
    data = request.json
    video_path = data.get('video_path')
    
    if not video_path:
        return jsonify({'error': 'Video path is required.'}), 400
    
    preview_url = video_agent.preview_video(video_path)
    
    return jsonify({'preview_url': preview_url}), 200