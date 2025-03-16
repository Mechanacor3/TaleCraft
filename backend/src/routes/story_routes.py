from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.story_agent import StoryAgent

router = APIRouter()
story_agent = StoryAgent()

class StoryRequest(BaseModel):
    story_idea: str

@router.post("/generate-outline")e-outline")
async def generate_outline(request: StoryRequest):
    try:try:
        outline = await story_agent.generate_outline(request.story_idea)equest.story_idea)
        return {"outline": outline}ne}
    except Exception as e:    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))tr(e))

@story_routes.route('/story/refine', methods=['PUT'])ine")
def refine_story():):
    data = request.json
    outline = data.get('outline')adjustments = data.get('adjustments')
    adjustments = data.get('adjustments')
    
    if not outline or not adjustments:    raise HTTPException(status_code=400, detail="Outline and adjustments are required")
        return jsonify({'error': 'Outline and adjustments are required'}), 400
    
    refined_outline = story_agent.refine_outline(outline, adjustments)        refined_outline = await story_agent.refine_outline(outline, adjustments)
    return jsonify(refined_outline), 200
e:
@story_routes.route('/story/<int:story_id>', methods=['GET'])il=str(e))
def get_story(story_id):
    story = story_agent.get_story_by_id(story_id)
    if not story:c def get_story(story_id: int):
        return jsonify({'error': 'Story not found'}), 404






        raise HTTPException(status_code=500, detail=str(e))    except Exception as e:        return story            raise HTTPException(status_code=404, detail="Story not found")        if not story:        story = await story_agent.get_story_by_id(story_id)    
    return jsonify(story), 200