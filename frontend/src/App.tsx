import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Outline from "./pages/Outline";
import Storyboard from "./components/Storyboard";
import ImageGeneration from "./components/ImageGeneration";
import ScriptAlignment from "./components/ScriptAlignment";
import TextToSpeech from "./components/TextToSpeech";
import VideoAssembly from "./components/VideoAssembly";
import FinalProduction from "./components/FinalProduction";

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/outline" element={<Outline />} />
            <Route path="/storyboard" element={<Storyboard />} />
            <Route path="/image-generation" element={<ImageGeneration />} />
            <Route path="/script-alignment" element={<ScriptAlignment />} />
            <Route path="/text-to-speech" element={<TextToSpeech />} />
            <Route path="/video-assembly" element={<VideoAssembly />} />
            <Route path="/final-production" element={<FinalProduction />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
