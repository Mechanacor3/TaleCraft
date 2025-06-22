import React from "react";

const Overview: React.FC = () => {
  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Workflow Overview</h2>
      <p className="mb-2">
        This app guides you through the entire short video creation process. Use
        the tabs above to move between stages. Start with the Story tab to craft
        your outline, then generate images and audio before assembling the final
        video.
      </p>
    </div>
  );
};

export default Overview;
