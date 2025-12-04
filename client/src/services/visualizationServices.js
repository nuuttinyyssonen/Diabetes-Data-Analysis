import axios from 'axios';

// Use relative paths so it works both locally and on Render
// Locally: http://localhost:8000/api → http://localhost:8000/api
// On Render: https://your-service.onrender.com/api → https://your-service.onrender.com/api
const getData = async (route) => {
    const response = await axios.get(`/${route}`);
    return response.data;
}

export default {
    getData
}