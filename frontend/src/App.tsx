import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import TabbedWorkflow from "./components/TabbedWorkflow";

const App: React.FC = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">
        <TabbedWorkflow />
      </main>
      <Footer />
    </div>
  );
};

export default App;
