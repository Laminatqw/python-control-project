import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [cars, setCar] = useState([])

    useEffect(() => {
        axios.get(
            '/api/listing').then(({data}) => {
            setCar(data)
        })
    }, []);
    console.log('12312312');
    return (
        <div>
            <h1>Furniture</h1>
            {cars.map(car=><div key={car.id}>{JSON.stringify(car)}
            </div>)}
        </div>
    );
};

export {App};