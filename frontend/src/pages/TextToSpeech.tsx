import React, { useState } from "react";

const TextToSpeech: React.FC = () => {
  const [voiceStyle, setVoiceStyle] = useState<string>("default");
  const [text, setText] = useState<string>("");
  const [audioUrl, setAudioUrl] = useState<string | null>(null);

  const handleTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  const handleVoiceChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setVoiceStyle(event.target.value);
  };

  const generateAudio = async () => {
    // Placeholder for audio generation logic
    // This would typically involve calling a TTS API with the selected voice style and text
    const response = await fetch("/api/generate-audio", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text, voiceStyle }),
    });

    if (response.ok) {
      const data = await response.json();
      setAudioUrl(data.audioUrl);
    } else {
      console.error("Failed to generate audio");
    }
  };

  return (
    <div className="text-to-speech">
      <h1 className="text-2xl font-bold">Text to Speech</h1>
      <textarea
        value={text}
        onChange={handleTextChange}
        placeholder="Enter text to convert to speech"
        className="w-full h-32 p-2 border border-gray-300 rounded"
      />
      <select
        value={voiceStyle}
        onChange={handleVoiceChange}
        className="mt-2 p-2 border border-gray-300 rounded"
      >
        <option value="default">Default Voice</option>
        <option value="voice1">Voice Style 1</option>
        <option value="voice2">Voice Style 2</option>
        {/* Add more voice styles as needed */}
      </select>
      <button
        onClick={generateAudio}
        className="mt-2 p-2 bg-blue-500 text-white rounded"
      >
        Generate Audio
      </button>
      {audioUrl && (
        <div className="mt-4">
          <audio controls src={audioUrl}>
            Your browser does not support the audio element.
          </audio>
        </div>
      )}
    </div>
  );
};

export default TextToSpeech;
