
const DataExploration = ({ images }) => {
    return (
        <div className="plot-box">
            <p>
                <strong>Correlations Among Input variables</strong><br />
                Values close to 1.00 indicates strong correlation and values close to 0 indicates no
                correlation at all.
            </p>
                {images.correlationHeatMap
                ? <img src={images.correlationHeatMap} alt="Kmeans Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
    );
};

export default DataExploration;