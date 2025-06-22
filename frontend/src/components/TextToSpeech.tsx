import React, { useState } from "react";
import { apiFetch } from "../api";

const TextToSpeech: React.FC = () => {
  const [voice, setVoice] = useState<string>("default");
  const [text, setText] = useState<string>("");
  const [audioUrl, setAudioUrl] = useState<string | null>(null);

  const handleTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  const handleVoiceChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setVoice(event.target.value);
  };

  const generateAudio = async () => {
    // Placeholder for audio generation logic
    // This should call the TTS API and set the audio URL
    const response = await apiFetch("/tts/generate_audio", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text, voice }),
    });
    const data = await response.json();
    setAudioUrl(data.audioUrl);
  };

  return (
    <div className="text-to-speech">
      <h2 className="text-lg font-bold">Text to Speech</h2>
      <textarea
        value={text}
        onChange={handleTextChange}
        placeholder="Enter text to convert to speech"
        className="w-full p-2 border rounded"
      />
      <select
        value={voice}
        onChange={handleVoiceChange}
        className="mt-2 p-2 border rounded"
      >
        <option value="default">Default Voice</option>
        <option value="voice1">Voice 1</option>
        <option value="voice2">Voice 2</option>
        {/* Add more voice options as needed */}
      </select>
      <button
        onClick={generateAudio}
        className="mt-2 p-2 bg-blue-500 text-white rounded"
      >
        Generate Audio
      </button>
      {audioUrl && (
        <div className="mt-4">
          <audio controls>
            <source src={audioUrl} type="audio/mpeg" />
            Your browser does not support the audio element.
          </audio>
        </div>
      )}
    </div>
  );
};

export default TextToSpeech;
