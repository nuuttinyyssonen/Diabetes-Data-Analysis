import { useEffect, useState } from "react";
import visualizationServices from "../services/visualizationServices";

const usePlots = () => {
    const [images, setImages] = useState({
    startingColumns: null,
    columnsWithoutZeros: null,
    columnsWithoutOutliers: null,
    elbowMethodPlot: null,
    silhouetteScoresPlot: null,
    kmeansPlot: null,
    KNN: null,
    heatMap: null,
    correlationHeatMap: null,
    outcomeDistribution: null,
    confusionMatrix: null
  });

    useEffect(() => {
        const fetchImages = async () => {
        try {
          const [starting, 
            zeros, 
            outliers, 
            elbow, 
            silhouetteScores, 
            kmeans, 
            KNN,
            heatMap, 
            correlationHeatMap, 
            outcomeDistribution
          ] = await Promise.all([
          visualizationServices.getStartingColumns(),
          visualizationServices.getColumnsWithoutZeros(),
          visualizationServices.getColumnsWithoutOutliers(),
          visualizationServices.getElbowMethodPlot(),
          visualizationServices.getSilhouetteScorePlot(),
          visualizationServices.getKmeansPlot(),
          visualizationServices.getKNN(),
          visualizationServices.getHeatMap(),
          visualizationServices.getCorrelationsHeatMap(),
          visualizationServices.getOutcomeDistribution()
        ]);
        setImages({
          startingColumns: starting.image ? `data:image/png;base64,${starting.image}` : null,
          columnsWithoutZeros: zeros.image ? `data:image/png;base64,${zeros.image}` : null,
          columnsWithoutOutliers: outliers.image ? `data:image/png;base64,${outliers.image}` : null,
          elbowMethodPlot: elbow.image ? `data:image/png;base64,${elbow.image}` : null,
          silhouetteScoresPlot: silhouetteScores.image ? `data:image/png;base64,${silhouetteScores.image}` : null,
          kmeansPlot: kmeans.image ? `data:image/png;base64,${kmeans.image}` : null,
          KNN: KNN.image ? `data:image/png;base64,${KNN.image}` : null,
          confusionMatrix: KNN.confusion_matrix ? `data:image/png;base64,${KNN.confusion_matrix}` : null,
          heatMap: heatMap.image ? `data:image/png;base64,${heatMap.image}` : null,
          correlationHeatMap: correlationHeatMap.image ? `data:image/png;base64,${correlationHeatMap.image}` : null,
          outcomeDistribution: outcomeDistribution.image ? `data:image/png;base64,${outcomeDistribution.image}` : null
        });
        } catch (error) {
          console.error("Error fetching images:", error);
        }
      };
      fetchImages();
    }, []);

  return {images};
}

export default usePlots;