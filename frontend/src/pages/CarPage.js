import {CarForm} from "../components/CarContainer/CarForm";
import {Cars} from "../components/CarContainer/Cars";

const CarPage = () => {
    return (
        <div>
            <CarForm/>
            <hr/>
            <Cars/>
            <hr/>
        </div>
    );
};

export {CarPage};