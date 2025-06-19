import React from "react";

const FinalProduction: React.FC = () => {
  const handleExport = () => {
    // Logic for exporting the final video
  };

  const handleUpload = () => {
    // Logic for uploading the video to ShortVideo
  };

  return (
    <div className="final-production">
      <h1 className="text-2xl font-bold">Final Production</h1>
      <p className="mt-4">
        Preview your final video and choose your export options.
      </p>
      <div className="mt-6">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={handleExport}
        >
          Export Video
        </button>
        <button
          className="bg-green-500 text-white px-4 py-2 rounded ml-4"
          onClick={handleUpload}
        >
          Upload to ShortVideo
        </button>
      </div>
    </div>
  );
};

export default FinalProduction;
