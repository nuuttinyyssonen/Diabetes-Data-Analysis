
const DataExploration = ({ images }) => {
    return (
        <div className="container">
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
            <div className="plot-box">
                <p>
                <strong>Distribution of Outcome variable</strong><br />
                Provides some insight for data to see how many people with diabetes vs without diabetes
                </p>
                {images.outcomeDistribution
                ? <img src={images.outcomeDistribution} alt="Kmeans Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
        </div>
    );
};

export default DataExploration;