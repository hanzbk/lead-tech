import React, { useState } from 'react';
import axios from 'axios';
import Dropzone from 'react-dropzone';

import Card from 'react-bootstrap/Card';


import Container from 'react-bootstrap/Container';

function FileUploader() {
    //const [file, setFile] = useState(null);

    const [serverData, setServerData] = useState(null);


    const onDrop = (acceptedFiles) => {
        const formData = new FormData();
        formData.append('csv_file', acceptedFiles[0]);

        axios.post('http://127.0.0.1:5000/data', formData).then((response) => {
            console.log(response.data);
            setServerData(response.data.message);
        });
    };

    return (
        <Card> {/* Encierra tu componente en una tarjeta */}
            <Card.Body>
                

                
            
            </Card.Body>

            <Container className="p-3" style={dropzoneStyle}>
                <Container className="p-5 mb-4 bg-light rounded-3">
                
                
                
                <Dropzone onDrop={onDrop}>
                    {({ getRootProps, getInputProps }) => (
                        <div {...getRootProps()}>
                            <input {...getInputProps()} />
                            <h2>Arrastra y suelta un archivo CSV aquí, o haz clic para seleccionar uno.</h2>
                        </div>
                    )}
                </Dropzone><br></br>

                </Container>


                <div>

                {serverData && (
            <div>
                 
                    <pre>{JSON.stringify(serverData, null, 2)}</pre>
                </div>
            )}
                </div>
                {/* Muestra los datos del servidor */}
            
            </Container>
        </Card>

        
    );
}

const dropzoneStyle = {
    border: '2px dashed #cccccc',
    borderRadius: '4px',
    padding: '20px',
    textAlign: 'center',
};



export default FileUploader;