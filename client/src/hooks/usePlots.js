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
    KNN: null
  });

    useEffect(() => {
        const fetchImages = async () => {
        try {
          const [starting, zeros, outliers, elbow, silhouetteScores, kmeans, KNN] = await Promise.all([
          visualizationServices.getStartingColumns(),
          visualizationServices.getColumnsWithoutZeros(),
          visualizationServices.getColumnsWithoutOutliers(),
          visualizationServices.getElbowMethodPlot(),
          visualizationServices.getSilhouetteScorePlot(),
          visualizationServices.getKmeansPlot(),
          visualizationServices.getKNN()
        ]);
        setImages({
          startingColumns: starting.image ? `data:image/png;base64,${starting.image}` : null,
          columnsWithoutZeros: zeros.image ? `data:image/png;base64,${zeros.image}` : null,
          columnsWithoutOutliers: outliers.image ? `data:image/png;base64,${outliers.image}` : null,
          elbowMethodPlot: elbow.image ? `data:image/png;base64,${elbow.image}` : null,
          silhouetteScoresPlot: silhouetteScores.image ? `data:image/png;base64,${silhouetteScores.image}` : null,
          kmeansPlot: kmeans.image ? `data:image/png;base64,${kmeans.image}` : null,
          KNN: KNN.image ? `data:image/png;base64,${KNN.image}` : null,
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