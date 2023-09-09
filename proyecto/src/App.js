//import logo from './logo.svg';
import React from 'react';
import './App.css';
import FileUpload from './FileUpload';
import DataDisplay from './DataDisplay';
import 'bootstrap/dist/css/bootstrap.min.css';




function App() {
  return (
    
    <div className="App"style={{ 
      backgroundImage: `url("https://verne-comfenalco.buho.media/static/dist/img/fondo-estrellas.svg")` 
    }}>
      
      <FileUpload />
      <DataDisplay />
    </div>
  );
}





export default App;
