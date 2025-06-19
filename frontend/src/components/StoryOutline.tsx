import React, { useState } from "react";

const StoryOutline: React.FC = () => {
  const [storyOutline, setStoryOutline] = useState<string>("");
  const [userInput, setUserInput] = useState<string>("");

  const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setUserInput(event.target.value);
  };

  const generateOutline = async () => {
    try {
      const response = await fetch("/stories/refine", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ outline: storyOutline, feedback: userInput }),
      });
      const data = await response.json();
      setStoryOutline(data.outline);
      setUserInput("");
    } catch (error) {
      console.error("Error refining outline:", error);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Interactive Story Outline</h2>
      <textarea
        className="w-full p-2 border border-gray-300 rounded"
        rows={4}
        placeholder="Enter your story idea here..."
        value={userInput}
        onChange={handleInputChange}
      />
      <button
        className="mt-2 bg-blue-500 text-white py-2 px-4 rounded"
        onClick={generateOutline}
      >
        Generate Outline
      </button>
      {storyOutline && (
        <div className="mt-4">
          <h3 className="text-xl font-semibold">Generated Outline:</h3>
          <p className="border border-gray-300 p-2 rounded">{storyOutline}</p>
        </div>
      )}
    </div>
  );
};

export default StoryOutline;
