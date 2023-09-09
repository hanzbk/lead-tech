import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import Table from 'react-bootstrap/Table';
import './App.css';

const DataDisplay = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showTableHeader, setShowTableHeader] = useState(false); // Estado para controlar la visibilidad del encabezado de la tabla

  const fetchData = async () => {
    setLoading(true);

    try {
      const response = await axios.get('http://127.0.0.1:5000/data');
      setData(response.data);
      setShowTableHeader(true); // Mostrar el encabezado después de consultar los datos
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div class="container" id="mi_tabla">
      <h2>Consultar Datos</h2>
      <Button variant="contained" onClick={fetchData}>Consultar</Button>
      {loading && <p>Cargando datos...</p>}
      <Table responsive striped bordered hover  class="table table-hover table-dark tableFixHead" >
        {showTableHeader && ( // Mostrar el encabezado solo cuando showTableHeader es verdadero
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Show ID</th>
              <th scope="col">Tipo</th>
              <th scope="col">Título</th>
              <th scope="col">Director</th>
              <th scope="col">País</th>
              <th scope="col">Fecha Agregada</th>
              <th scope="col">Año de Lanzamiento</th>
              <th scope="col">Clasificación</th>
              <th scope="col">Duración</th>
              <th scope="col">Lista en</th>
              <th scope="col">Descripción</th>
            </tr>
          </thead>
        )}
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.show_id}</td>
              <td>{item.type}</td>
              <td>{item.title}</td>
              <td>{item.director}</td>
              <td>{item.country}</td>
              <td>{item.date_added}</td>
              <td>{item.release_year}</td>
              <td>{item.rating}</td>
              <td>{item.duration}</td>
              <td>{item.listed_in}</td>
              <td>{item.description}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default DataDisplay;
