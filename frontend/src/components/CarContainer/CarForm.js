import React from 'react';
import {useForm} from "react-hook-form";
import {carServices} from '../../services/carServices'

const CarForm = () => {
     const {register, handleSubmit, reset} = useForm();

    const save = async (furniture) => {
        await carServices.create(furniture)
        reset()
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type="text" placeholder={'brand'} {...register('brand')}/>
            <input type="text" placeholder={'model'} {...register('model')}/>

            <button>save</button>
        </form>
    );
};

export {CarForm};