import React, { useState } from 'react';

const ScriptAlignment: React.FC = () => {
    const [script, setScript] = useState<string>('');
    const [timing, setTiming] = useState<number>(0);

    const handleScriptChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setScript(event.target.value);
    };

    const handleTimingChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTiming(Number(event.target.value));
    };

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Script Alignment</h1>
            <textarea
                className="w-full h-40 p-2 border border-gray-300 rounded"
                value={script}
                onChange={handleScriptChange}
                placeholder="Edit your script here..."
            />
            <div className="mt-4">
                <label className="block mb-2">Adjust Timing (in seconds):</label>
                <input
                    type="number"
                    className="border border-gray-300 rounded p-2"
                    value={timing}
                    onChange={handleTimingChange}
                />
            </div>
            <div className="mt-4">
                <h2 className="text-xl font-semibold">Current Script:</h2>
                <p>{script}</p>
                <p>Timing: {timing} seconds</p>
            </div>
        </div>
    );
};

export default ScriptAlignment;