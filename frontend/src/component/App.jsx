import React, { useState, useEffect } from "react";
import Typewriter from "typewriter-effect";
import "./App.css";

const App = () => {
  const testText = 'You will need to bundle the javascript before it can be used, this can be done using npm run build:dev for development or npm run build:prod for production.You will need to bundle the javascript before it can be used, this can be done using npm run build:dev for development or npm run build:prod for production.You will need to bundle the javascript before it can be used, this can be done using npm run build:dev for development or npm run build:prod for production.'

  return (
    <div className="app-container">
      <div className="leftGradientbox">
        <button className="primary-btn">Translation</button>

        <div className="typing-container">
          <Typewriter
            onInit={(typewriter) => {
              typewriter
                .typeString(testText)
                .callFunction(() => {
                  console.log("String typed out!");
                })
                .pauseFor(2500)
                // .deleteAll()
                .callFunction(() => {
                  console.log("All strings were deleted");
                })
                .start();
            }}
          />
        </div>
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: "3rem" }}>
        <div
          // }}
          className="rightGradientBox"
        >
          <button className="primary-btn">Emergency Words</button>
        </div>
        <div
          // }}
          className="rightGradientBox"
        >
          <button className="primary-btn">Caller Information</button>
        </div>
      </div>
    </div>
  );
};

export default App;
