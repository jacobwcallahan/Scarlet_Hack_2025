import React from "react";
function App() {
  console.log("====================================");
  console.log("rendering");
  console.log("====================================");
  return <div className="App">
    <h1 className="text-3xl underline" style={{backgroundColor:'red'}}>
    💖 Hello world!
    </h1>
     <p>Welcome to your Electron application.</p>
  </div>;
}

export default App;
