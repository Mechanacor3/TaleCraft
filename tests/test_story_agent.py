import pytest
from backend.src.agents import story_agent
from backend.src.agents.story_agent import StoryAgent, EvaluationFeedback

class DummyResult:
    def __init__(self, input_items, new_items=None, final_output=None):
        self.input = input_items
        self.new_items = new_items or []
        self.final_output = final_output

    def to_input_list(self):
        return self.input + self.new_items


@pytest.mark.asyncio
async def test_generate_outline_single_turn(monkeypatch):
    agent = StoryAgent()

    async def mock_run(starting_agent, input_items, **kwargs):
        if starting_agent is agent.story_outline_generator:
            return DummyResult(input_items, ["outline"], None)
        return DummyResult(input_items, [], EvaluationFeedback(score="pass", feedback="good"))

    monkeypatch.setattr(story_agent.Runner, "run", mock_run)
    monkeypatch.setattr(story_agent.ItemHelpers, "text_message_outputs", lambda items: "".join(items))

    outline = await agent.generate_outline("idea", max_turns=1)
    assert outline == "outline"


@pytest.mark.asyncio
async def test_generate_outline_max_turns_exceeded(monkeypatch):
    agent = StoryAgent()
    call = {"n": 0}

    async def mock_run(starting_agent, input_items, **kwargs):
        if starting_agent is agent.story_outline_generator:
            call["n"] += 1
            return DummyResult(input_items, [f"outline{call['n']}"])
        return DummyResult(input_items, [], EvaluationFeedback(score="needs_improvement", feedback="no"))

    monkeypatch.setattr(story_agent.Runner, "run", mock_run)
    monkeypatch.setattr(story_agent.ItemHelpers, "text_message_outputs", lambda items: "".join(items))

    outline = await agent.generate_outline("idea", max_turns=1)
    assert outline == "outline2"


@pytest.mark.asyncio
async def test_refine_outline_returns_new(monkeypatch):
    agent = StoryAgent()

    async def mock_run(starting_agent, input_items, **kwargs):
        return DummyResult(input_items, ["new outline"])

    monkeypatch.setattr(story_agent.Runner, "run", mock_run)
    monkeypatch.setattr(story_agent.ItemHelpers, "text_message_outputs", lambda items: "".join(items))

    result = await agent.refine_outline("old", "feedback")
    assert result == "new outline"


@pytest.mark.asyncio
async def test_generate_outline_demo_mode(monkeypatch):
    monkeypatch.setenv("DEMO_MODE", "true")
    import importlib

    import backend.src.agents.story_agent as sa

    importlib.reload(sa)
    agent = sa.StoryAgent()
    outline = await agent.generate_outline("idea")
    assert outline == sa.DEFAULT_STORY_OUTLINE
