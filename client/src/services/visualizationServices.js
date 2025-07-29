import axios from 'axios';

const baseUrl = "http://127.0.0.1:8000"

const getStartingColumns = async () => {
    const response = await axios.get(`${baseUrl}/columns`)
    return response.data
}

export default {
    getStartingColumns
}