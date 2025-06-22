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
  const demoMode = import.meta.env.VITE_DEMO_MODE === "true";

  const initialEnabled = new Set(["overview", "story"]);

  return (
    <div className="p-4">
      <div className="border-b mb-4">
        <ul className="flex flex-wrap -mb-px">
          {tabs.map((tab) => {
            const isInitial = initialEnabled.has(tab.id);
            const disabled = !demoMode && !isInitial;
            const demoDisabled = demoMode && !isInitial;

            let classes = "inline-block rounded-t px-4 py-2 border-b-2 ";
            if (activeTab === tab.id) {
              classes += "border-blue-500 text-blue-600";
            } else if (disabled) {
              classes += "border-transparent text-gray-400 cursor-not-allowed";
            } else if (demoDisabled) {
              classes += "border-red-300 text-red-400 hover:text-red-600";
            } else {
              classes +=
                "border-transparent hover:text-blue-600 hover:border-gray-300";
            }

            return (
              <li key={tab.id} className="mr-2">
                <button
                  className={classes}
                  disabled={disabled}
                  onClick={() => !disabled && setActiveTab(tab.id)}
                >
                  {tab.label}
                </button>
              </li>
            );
          })}
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
