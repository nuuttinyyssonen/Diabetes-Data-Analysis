import '../App.css'
const ClusterClassPlots = ({ images }) => {
    return (
        <div className='Container'>
            <div className="plot-box">
                <p>
                  <strong>KMeans Clustering Visualization:</strong><br />
                  This plot shows the results of KMeans clustering on the dataset, with data points and cluster centroids visualized after dimensionality reduction.
                </p>
                {images.kmeansPlot
                ? <img src={images.kmeansPlot} alt="Elbow Method Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
            <div className="plot-box">
                <p>
                  <strong>KNN Classification Accuracy:</strong><br />
                  This plot displays the classification accuracy of the K-Nearest Neighbors algorithm for different values of k, helping to identify the optimal number of neighbors for prediction.
                </p>
                {images.KNN
                ? <img src={images.KNN} alt="Elbow Method Plot" />
                : <div>Loading KNN Plot...</div>}
            </div>
        </div>
    );
}

export default ClusterClassPlots;