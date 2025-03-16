from flask import Blueprint, request, jsonify
from agents.script_alignment_agent import ScriptAlignmentAgent

script_routes = Blueprint('script_routes', __name__)
script_agent = ScriptAlignmentAgent()

@script_routes.route('/align_script', methods=['POST'])
def align_script():
    data = request.json
    images = data.get('images')
    script = data.get('script')
    
    if not images or not script:
        return jsonify({'error': 'Images and script are required.'}), 400
    
    aligned_script = script_agent.align_script_with_images(images, script)
    return jsonify({'aligned_script': aligned_script}), 200

@script_routes.route('/edit_script', methods=['PUT'])
def edit_script():
    data = request.json
    new_script = data.get('new_script')
    
    if not new_script:
        return jsonify({'error': 'New script is required.'}), 400
    
    updated_script = script_agent.update_script(new_script)
    return jsonify({'updated_script': updated_script}), 200