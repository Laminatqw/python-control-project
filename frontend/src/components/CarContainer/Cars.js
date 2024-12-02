import { useEffect, useState } from "react";
import { carServices } from "../../services/carServices";
import { useNavigate } from "react-router-dom";

const Cars = () => {
    const [cars, setCars] = useState([]);
    const [trigger, setTrigger] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        carServices.getAll().then(({ data }) => setCars(data));
    }, [trigger]);

    const handleClick = (id) => {
        navigate(`/listing/${id}`);
    };

    return (
        <div>
            {cars.map((auto) => (
                <div key={auto.id}>
                    {auto.id}. {auto.price} - {auto.car.brand}
                    <button onClick={() => handleClick(auto.id)}>View Details</button>
                </div>
            ))}
        </div>
    );
};

export { Cars };
