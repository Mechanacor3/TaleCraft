import React from 'react';
import StoryInput from '../components/StoryInput';
import StoryOutline from '../components/StoryOutline';

const Outline: React.FC = () => {
    return (
        <div className="flex flex-col items-center p-4">
            <h1 className="text-2xl font-bold mb-4">Interactive Story Outline</h1>
            <StoryInput />
            <StoryOutline />
        </div>
    );
};

export default Outline;