import {useForm} from "react-hook-form";
import {authServices} from "../services/authServices";
import {useNavigate} from "react-router-dom";

const LoginPage = () => {
    const {handleSubmit, register} = useForm();
    const navigate = useNavigate();

    const onSubmit = async (user) => {
        await authServices.login(user)
        navigate('/listing')
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder={'email'} {...register('email')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <button>login</button>
        </form>
    );
};

export {LoginPage};