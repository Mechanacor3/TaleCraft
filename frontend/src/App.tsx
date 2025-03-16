import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import Outline from './pages/Outline';
import Storyboard from './pages/Storyboard';
import ImageGeneration from './pages/ImageGeneration';
import ScriptAlignment from './pages/ScriptAlignment';
import TextToSpeech from './pages/TextToSpeech';
import VideoAssembly from './pages/VideoAssembly';
import FinalProduction from './pages/FinalProduction';

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header />
        <main className="flex-grow">
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/outline" component={Outline} />
            <Route path="/storyboard" component={Storyboard} />
            <Route path="/image-generation" component={ImageGeneration} />
            <Route path="/script-alignment" component={ScriptAlignment} />
            <Route path="/text-to-speech" component={TextToSpeech} />
            <Route path="/video-assembly" component={VideoAssembly} />
            <Route path="/final-production" component={FinalProduction} />
          </Switch>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;