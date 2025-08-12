import axios from 'axios';

const baseUrl = "http://127.0.0.1:8000";

const getData = async (route) => {
    const response = await axios.get(`${baseUrl}/${route}`);
    return response.data;
}

export default {
    getData
}