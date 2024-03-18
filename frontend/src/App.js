import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Home from './pages/Home';


export default function App() {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home />}></Route>
                <Route path='/onlogin' element={<Login />}></Route>
                <Route path='/onregister' element={<Register />}></Route>
            </Routes>
        </Router>
    );
}