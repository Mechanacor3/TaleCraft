import React, { useState } from "react";

const StoryInput: React.FC = () => {
  const [storyIdea, setStoryIdea] = useState<string>("");
  const [outline, setOutline] = useState<string | null>(null);

  const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setStoryIdea(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch("/stories/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ story_idea: storyIdea }),
      });
      const data = await response.json();
      setOutline(data.outline);
    } catch (error) {
      console.error("Error generating outline:", error);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Input Your Story Idea</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full h-32 p-2 border border-gray-300 rounded"
          value={storyIdea}
          onChange={handleInputChange}
          placeholder="Type your story idea here..."
        />
        <button
          type="submit"
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Submit
        </button>
      </form>
      {outline && (
        <div className="mt-4 border rounded p-2">
          <h3 className="font-semibold">Generated Outline</h3>
          <p>{outline}</p>
        </div>
      )}
    </div>
  );
};

export default StoryInput;
