import axios from 'axios';

const baseUrl = "http://127.0.0.1:8000"

const getStartingColumns = async () => {
    const response = await axios.get(`${baseUrl}/startingColumns`);
    return response.data;
}

const getColumnsWithoutZeros = async () => {
    const response = await axios.get(`${baseUrl}/zeroValuesRemoved`);
    return response.data;
}

const getColumnsWithoutOutliers = async () => {
    const response = await axios.get(`${baseUrl}/outliersRemoved`);
    return response.data;
}

const getElbowMethodPlot = async () => {
    const response = await axios.get(`${baseUrl}/elbowMethod`);
    return response.data;
}

const getSilhouetteScorePlot = async () => {
    const response = await axios.get(`${baseUrl}/silhouetteScores`);
    return response.data;
}

const getKmeansPlot = async () => {
    const response = await axios.get(`${baseUrl}/kmeansPlot`);
    return response.data;
}

export default {
    getStartingColumns,
    getColumnsWithoutZeros,
    getColumnsWithoutOutliers,
    getElbowMethodPlot,
    getSilhouetteScorePlot,
    getKmeansPlot
}