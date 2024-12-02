import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";
import {LoginPage} from "./pages/LoginPage";
import {CarPage} from "./pages/CarPage";
import OneCarPage from "./components/CarContainer/OneCarPage";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {
                index: true, element: <Navigate to={'login'}/>
            },
            {
                path: 'login', element: <LoginPage/>
            },
            {
                path: 'listing', element: <CarPage/>
            },
            {
                path: `listing/:id`, element: <OneCarPage/>
            }
        ]
    }
])

export {
    router
}