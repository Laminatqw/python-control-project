import ReactDOM from 'react-dom/client';
import {App} from './App';
import {RouterProvider} from "react-router-dom";
import {router} from "./router";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <RouterProvider router={router}/>
);