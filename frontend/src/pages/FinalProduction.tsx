import React from "react";

const FinalProduction: React.FC = () => {
  return (
    <div className="final-production">
      <h1 className="text-2xl font-bold mb-4">Final Production</h1>
      <p className="mb-4">
        Assemble your final video and export it for sharing!
      </p>
      <div className="video-preview">
        {/* Video preview component will go here */}
      </div>
      <div className="export-options">
        <button className="bg-blue-500 text-white px-4 py-2 rounded">
          Preview Video
        </button>
        <button className="bg-green-500 text-white px-4 py-2 rounded">
          Export Video
        </button>
        <button className="bg-yellow-500 text-white px-4 py-2 rounded">
          Upload to YouTube
        </button>
      </div>
    </div>
  );
};

export default FinalProduction;
