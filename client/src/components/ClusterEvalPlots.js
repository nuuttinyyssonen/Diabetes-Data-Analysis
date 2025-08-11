
const ClusterEvalPlots = ({ images }) => {
    return (
        <div>
            <div>
                {images.elbowMethodPlot
                ? <img src={images.elbowMethodPlot} alt="Elbow Method Plot" />
                : <div>Loading Elbow Method Plot...</div>}
            </div>
            <div>
                {images.silhouetteScoresPlot
                ? <img src={images.silhouetteScoresPlot} alt="Elbow Method Plot" />
                : <div>Loading silhouette scores plot...</div>}
            </div>
        </div>
    );
}

export default ClusterEvalPlots;