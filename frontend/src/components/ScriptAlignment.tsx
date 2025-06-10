import React, { useState } from "react";

const ScriptAlignment: React.FC = () => {
  const [script, setScript] = useState<string>("");
  const [images, setImages] = useState<string[]>([]); // Array to hold image URLs or data
  const [dialogue, setDialogue] = useState<string[]>([]); // Array to hold dialogue lines

  const handleScriptChange = (
    event: React.ChangeEvent<HTMLTextAreaElement>,
  ) => {
    setScript(event.target.value);
  };

  const handleDialogueChange = (index: number, value: string) => {
    const updatedDialogue = [...dialogue];
    updatedDialogue[index] = value;
    setDialogue(updatedDialogue);
  };

  const addDialogueLine = () => {
    setDialogue([...dialogue, ""]);
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Script Alignment</h1>
      <textarea
        className="w-full h-32 p-2 border border-gray-300 rounded"
        placeholder="Enter your script here..."
        value={script}
        onChange={handleScriptChange}
      />
      <div className="mt-4">
        <h2 className="text-xl font-semibold">Dialogue Lines</h2>
        {dialogue.map((line, index) => (
          <div key={index} className="flex items-center mb-2">
            <input
              type="text"
              className="flex-1 p-2 border border-gray-300 rounded"
              value={line}
              onChange={(e) => handleDialogueChange(index, e.target.value)}
            />
          </div>
        ))}
        <button
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded"
          onClick={addDialogueLine}
        >
          Add Dialogue Line
        </button>
      </div>
      <div className="mt-4">
        <h2 className="text-xl font-semibold">Associated Images</h2>
        {images.map((image, index) => (
          <img
            key={index}
            src={image}
            alt={`Storyboard Image ${index + 1}`}
            className="w-32 h-32 object-cover mb-2"
          />
        ))}
      </div>
    </div>
  );
};

export default ScriptAlignment;
