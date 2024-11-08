import React from "react";
import ReactDom from 'react-dom/client'
import './index.css'
import App from './App.jsx'

const rootNode= document.getElementById("root");

ReactDom.createRoot(rootNode).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
