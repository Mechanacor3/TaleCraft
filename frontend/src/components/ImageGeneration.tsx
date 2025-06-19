import React, { useState } from "react";

const ImageGeneration: React.FC = () => {
  const [prompt, setPrompt] = useState("");
  const [images, setImages] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleGenerateImages = async () => {
    setLoading(true);
    try {
      // Call the DALL·E API to generate images based on the prompt
      const response = await fetch("/images/generate-image", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });
      const data = await response.json();
      setImages(data.images);
    } catch (error) {
      console.error("Error generating images:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="image-generation">
      <h2 className="text-2xl font-bold mb-4">Image Generation</h2>
      <textarea
        className="w-full p-2 border border-gray-300 rounded mb-4"
        rows={4}
        placeholder="Enter your image generation prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={handleGenerateImages}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Images"}
      </button>
      <div className="mt-4">
        {images.length > 0 && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {images.map((image, index) => (
              <img
                key={index}
                src={image}
                alt={`Generated ${index}`}
                className="w-full h-auto rounded"
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default ImageGeneration;
