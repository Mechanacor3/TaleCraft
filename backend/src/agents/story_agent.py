import asyncio
from dataclasses import dataclass
from typing import Literal, List, Optional

from agents import Agent, ItemHelpers, Runner, TResponseInputItem, trace



@dataclass
class EvaluationFeedback:
    score: Literal["pass", "needs_improvement", "fail"]
    feedback: str


class StoryAgent:
    def __init__(self):
        self.story_outline_generator = Agent(
            name="Story Outline Generator Agent",
            model="o3-mini",
            instructions=(
                "You generate a very short story outline based on the user's input. "
                "If there is any feedback provided, use it to improve the outline. "
            ),
        )
        self.evaluator = Agent[None](
            name="Story Evalutator Agent",
            model="o3-mini",
            instructions=(
                "You evaluate a story outline and decide if it's good enough. "
                "If it's not good enough, you provide feedback on what needs to be improved. "
                "Never give it a pass on the first try. "
                "Pay special attention to the user's request for tone and style. "
            ),
            output_type=EvaluationFeedback,
        )

    async def generate_outline(self, story_idea: str, max_turns:int = 1, trace_id:str|None=None) -> str:
        """
        Generate a story outline based on the provided story idea.
        """
        if max_turns < 1:
            raise ValueError("Max turns must be greater than 0.")
        if max_turns > 5:
            raise ValueError("Max turns must be less than 5.")
        
        input_items: List[TResponseInputItem] = [
            {"content": story_idea, "role": "user"}
        ]
        latest_outline: Optional[str] = None

        current_attempt = 0
        with trace("story_agent", trace_id=trace_id):
            while True:
                if current_attempt > max_turns:
                    print("Max attempts reached, exiting.")
                    break
                current_attempt += 1

                story_outline_result = await Runner.run(
                    self.story_outline_generator,
                    input_items,
                )

                input_items = story_outline_result.to_input_list()
                latest_outline = ItemHelpers.text_message_outputs(
                    story_outline_result.new_items
                )
                print("Story outline generated")

                evaluator_result = await Runner.run(self.evaluator, input_items)
                result: EvaluationFeedback = evaluator_result.final_output

                print(f"Evaluator score: {result.score}")

                if result.score == "pass":
                    print("Story outline is good enough, exiting.")
                    break

                print("Re-running with feedback")
                if current_attempt > max_turns:
                    print("Jokes! Max attempts reached, hope its good enough.")
                    break

                input_items.append(
                    {"content": f"Feedback: {result.feedback}", "role": "user"}
                )

        return latest_outline

    async def refine_outline(self, outline: str, feedback: str) -> str:
        # Logic to refine the existing story outline based on user feedback
        # todo - convert feedback into using a feedback tool to ensure it is in the correct format
        input_items: List[TResponseInputItem] = [
            {"content": outline, "role": "assistant"},
            {"content": f"Feedback: {feedback}", "role": "user"},
        ]
        story_outline_result = await Runner.run(
            self.story_outline_generator,
            input_items,
        )
        return  ItemHelpers.text_message_outputs(
            story_outline_result.new_items
        )

async def main() -> None:
    story_agent = StoryAgent()
    outline = await story_agent.generate_outline(
        "A children's story about two ducks in a pond helping a frog cross the water."
    )
    print(outline)

    new_outline = await story_agent.refine_outline(outline, "Add robots!")
    print(new_outline)


if __name__ == "__main__":
    asyncio.run(main())
