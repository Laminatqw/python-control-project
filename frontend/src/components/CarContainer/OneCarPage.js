import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import {carServices} from '..//..//services/carServices'

const UserDetails =() => {

    const { id } = useParams();
    const [car, setCar] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (id) {
            Promise.all([carServices.getOneCar(Number(id))])
                .then(([carResponse]) => {
                    setCar(carResponse.data);
                    setLoading(false);
                })
                .catch(error => {
                    setError('Error fetching data');
                    setLoading(false);
                });
        }
    }, [id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!car) {
        return <div>No user data</div>;
    }

    return (
        <div>
            <h1>User Details</h1>
            <p>Username: {car.price} - {car.car.brand}</p>

        </div>
    );
};

export default UserDetails;