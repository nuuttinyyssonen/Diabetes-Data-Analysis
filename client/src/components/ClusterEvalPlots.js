import '../App.css'
import usePlots from '../hooks/usePlots';
const ClusterEvalPlots = () => {
    const plotKeys = ["elbowMethodPlot", "silhouetteScoresPlot"];
    const images = usePlots(plotKeys)
    return (
        <div className='Container'>
            <div className="plot-box">
                <p>
                    <strong>Elbow method: </strong>
                    This plot shows the elbow point which gives use the optimal
                    number of K's to use in Kmeans. The elbow point is at around 2 which we can prove
                    more with Silhouette method below.
                </p>
                {images.elbowMethodPlot
                ? <img src={images.elbowMethodPlot} alt="Elbow Method Plot" />
                : <div>Loading Elbow Method Plot...</div>}
            </div>
            <div className="plot-box">
                <p>
                    <strong>Silhouette scores: </strong>
                    This plot shows the highest silhouette score for k = 2.
                </p>
                {images.silhouetteScoresPlot
                ? <img src={images.silhouetteScoresPlot} alt="Elbow Method Plot" />
                : <div>Loading silhouette scores plot...</div>}
            </div>
        </div>
    );
}

export default ClusterEvalPlots;