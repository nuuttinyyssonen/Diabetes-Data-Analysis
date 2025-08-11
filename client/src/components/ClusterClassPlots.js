const ClusterClassPlots = ({ images }) => {
    return (
        <div>
            <div>
                {images.kmeansPlot
                ? <img src={images.kmeansPlot} alt="Elbow Method Plot" />
                : <div>Loading kmenas Plot...</div>}
            </div>
            <div>
                {images.KNN
                ? <img src={images.KNN} alt="Elbow Method Plot" />
                : <div>Loading KNN Plot...</div>}
            </div>
        </div>
    );
}

export default ClusterClassPlots;