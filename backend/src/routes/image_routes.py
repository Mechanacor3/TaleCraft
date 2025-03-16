from flask import Blueprint, request, jsonify
from agents.image_generation_agent import ImageGenerationAgent

image_routes = Blueprint('image_routes', __name__)
image_agent = ImageGenerationAgent()

@image_routes.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        image_url = image_agent.generate_image(prompt)
        return jsonify({'image_url': image_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@image_routes.route('/regenerate-image', methods=['POST'])
def regenerate_image():
    data = request.json
    image_id = data.get('image_id')
    new_prompt = data.get('new_prompt')
    if not image_id or not new_prompt:
        return jsonify({'error': 'Image ID and new prompt are required'}), 400

    try:
        new_image_url = image_agent.regenerate_image(image_id, new_prompt)
        return jsonify({'new_image_url': new_image_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500