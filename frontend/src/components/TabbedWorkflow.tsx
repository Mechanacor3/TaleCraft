import React, { useState } from "react";
import Overview from "./Overview";
import StoryInput from "./StoryInput";
import StoryOutline from "./StoryOutline";
import Storyboard from "./Storyboard";
import ImageGeneration from "./ImageGeneration";
import ScriptAlignment from "./ScriptAlignment";
import TextToSpeech from "./TextToSpeech";
import VideoAssembly from "./VideoAssembly";
import FinalProduction from "./FinalProduction";

const TabbedWorkflow: React.FC = () => {
  const tabs = [
    { id: "overview", label: "Overview", content: <Overview /> },
    {
      id: "story",
      label: "Story",
      content: (
        <div>
          <StoryInput />
          <StoryOutline />
        </div>
      ),
    },
    { id: "storyboard", label: "Storyboard", content: <Storyboard /> },
    { id: "image", label: "Images", content: <ImageGeneration /> },
    { id: "script", label: "Script", content: <ScriptAlignment /> },
    { id: "audio", label: "Audio", content: <TextToSpeech /> },
    { id: "video", label: "Video", content: <VideoAssembly /> },
    { id: "final", label: "Final", content: <FinalProduction /> },
  ];

  const [activeTab, setActiveTab] = useState(tabs[0].id);

  return (
    <div className="p-4">
      <div className="border-b mb-4">
        <ul className="flex flex-wrap -mb-px">
          {tabs.map((tab) => (
            <li key={tab.id} className="mr-2">
              <button
                className={`inline-block rounded-t px-4 py-2 border-b-2 ${activeTab === tab.id ? "border-blue-500 text-blue-600" : "border-transparent hover:text-blue-600 hover:border-gray-300"}`}
                onClick={() => setActiveTab(tab.id)}
              >
                {tab.label}
              </button>
            </li>
          ))}
        </ul>
      </div>
      <div>
        {tabs.map((tab) => (
          <div key={tab.id} className={activeTab === tab.id ? "" : "hidden"}>
            {tab.content}
          </div>
        ))}
      </div>
    </div>
  );
};

export default TabbedWorkflow;
