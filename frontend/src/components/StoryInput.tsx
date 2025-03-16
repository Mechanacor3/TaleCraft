import React, { useState } from 'react';

const StoryInput: React.FC = () => {
    const [storyIdea, setStoryIdea] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setStoryIdea(event.target.value);
    };

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Handle story idea submission (e.g., send to backend or update state)
        console.log('Story Idea Submitted:', storyIdea);
    };

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Input Your Story Idea</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    className="w-full h-32 p-2 border border-gray-300 rounded"
                    value={storyIdea}
                    onChange={handleInputChange}
                    placeholder="Type your story idea here..."
                />
                <button
                    type="submit"
                    className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
                >
                    Submit
                </button>
            </form>
        </div>
    );
};

export default StoryInput;