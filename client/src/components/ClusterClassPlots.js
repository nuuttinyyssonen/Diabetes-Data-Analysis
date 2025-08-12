import '../App.css'
import usePlots from '../hooks/usePlots';
const ClusterClassPlots = () => {
  const plotKeys = ["kmeansPlot", "clusterOutcomeHeatmap", "KNN"];
  const images = usePlots(plotKeys);
    return (
        <div className='Container'>
            <div className="plot-box">
                <p>
                  <strong>KMeans Clustering Visualization:</strong><br />
                  This plot shows the results of KMeans clustering on the dataset, with data points and cluster centroids visualized after dimensionality reduction.
                </p>
                {images.kmeansPlot
                ? <img src={images.kmeansPlot} alt="Kmeans Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
            <div className="plot-box">
                <p>
                  <strong>HeatMap of Cluster Assignments vs Outcome</strong><br />
                  This HeatMap shows the distribution of outcome variable (people with diabetes 1 and people without diabetes 0)
                  in 2 different clusters.
                </p>
                {images.heatMap
                ? <img src={images.heatMap} alt="heatMap Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
            <div className="plot-box">
                <p>
                  <strong>KNN Classification Accuracy:</strong><br />
                  This plot displays the classification accuracy of the K-Nearest Neighbors algorithm for different values of k, helping to identify the optimal number of neighbors for prediction.
                </p>
                {images.KNN
                ? <img src={images.KNN} alt="KNN Plot" />
                : <div>Loading KNN Plot...</div>}
            </div>
            <div className="plot-box confusionMatrix">
                <p>
                  <strong>Confusion Matrix:</strong><br />
                    This plot visualizes the performance of the K-Nearest Neighbors classifier by showing the number of correct and incorrect predictions for each class. 
                    The diagonal cells represent correct predictions, while off-diagonal cells indicate misclassifications.
                </p>
                {images.confusionMatrix
                ? <img className='confusionMatrix' src={images.confusionMatrix} alt="KNN Plot" />
                : <div>Loading Confusion Matrix Plot...</div>}
            </div>
        </div>
    );
}

export default ClusterClassPlots;