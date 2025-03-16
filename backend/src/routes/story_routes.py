from flask import Blueprint, request, jsonify
from agents.story_agent import StoryAgent

story_routes = Blueprint('story_routes', __name__)
story_agent = StoryAgent()

@story_routes.route('/story', methods=['POST'])
def create_story():
    data = request.json
    story_idea = data.get('story_idea')
    if not story_idea:
        return jsonify({'error': 'Story idea is required'}), 400
    
    outline = story_agent.generate_outline(story_idea)
    return jsonify(outline), 201

@story_routes.route('/story/refine', methods=['PUT'])
def refine_story():
    data = request.json
    outline = data.get('outline')
    adjustments = data.get('adjustments')
    
    if not outline or not adjustments:
        return jsonify({'error': 'Outline and adjustments are required'}), 400
    
    refined_outline = story_agent.refine_outline(outline, adjustments)
    return jsonify(refined_outline), 200

@story_routes.route('/story/<int:story_id>', methods=['GET'])
def get_story(story_id):
    story = story_agent.get_story_by_id(story_id)
    if not story:
        return jsonify({'error': 'Story not found'}), 404
    
    return jsonify(story), 200