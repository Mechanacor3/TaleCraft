import asyncio
from dataclasses import dataclass
from typing import Literal

from agents import Agent, ItemHelpers, Runner, TResponseInputItem, trace


@dataclass
class EvaluationFeedback:
    score: Literal["pass", "needs_improvement", "fail"]
    feedback: str


class StoryAgent:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.story_outline = []
        self.story_outline_generator = Agent(
            name="Story Outline Generator Agent",
            model="o1",
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

    async def generate_outline(self, story_idea):
        input_items: list[TResponseInputItem] = [
            {"content": story_idea, "role": "user"}
        ]
        latest_outline: str | None = None

        current_attempt = 0
        with trace("LLM as a judge"):
            while True:
                current_attempt += 1
                if current_attempt > self.max_attempts:
                    print("Max attempts reached, exiting.")
                    break

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

                input_items.append(
                    {"content": f"Feedback: {result.feedback}", "role": "user"}
                )

        self.story_outline = latest_outline

    def refine_outline(self, feedback):
        # Logic to refine the existing story outline based on user feedback
        pass

    def get_outline(self):
        return self.story_outline

    def set_outline(self, outline):
        self.story_outline = outline


async def main():
    story_agent = StoryAgent()
    await story_agent.generate_outline("A childrens story about two ducks in a pond helping a frog cross the water.")
    print(story_agent.get_outline())


if __name__ == "__main__":
    asyncio.run(main())
