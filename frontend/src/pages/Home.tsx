import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import StoryInput from "../components/StoryInput";

const Home: React.FC = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow flex items-center justify-center">
        <StoryInput />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
