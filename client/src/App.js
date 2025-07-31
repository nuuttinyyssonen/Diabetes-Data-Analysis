import { useEffect, useState } from "react";
import visualizationServices from "./services/visualizationServices";
import './App.css';

function App() {
  const [images, setImages] = useState({
    startingColumns: null,
    columnsWithoutZeros: null,
    columnsWithoutOutliers: null,
    elbowMethodPlot: null,
    silhouetteScoresPlot: null,
    kmeansPlot: null
  });

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const [starting, zeros, outliers, elbow, silhouetteScores, kmeans] = await Promise.all([
        visualizationServices.getStartingColumns(),
        visualizationServices.getColumnsWithoutZeros(),
        visualizationServices.getColumnsWithoutOutliers(),
        visualizationServices.getElbowMethodPlot(),
        visualizationServices.getSilhouetteScorePlot(),
        visualizationServices.getKmeansPlot()
      ]);
      setImages({
        startingColumns: starting.image ? `data:image/png;base64,${starting.image}` : null,
        columnsWithoutZeros: zeros.image ? `data:image/png;base64,${zeros.image}` : null,
        columnsWithoutOutliers: outliers.image ? `data:image/png;base64,${outliers.image}` : null,
        elbowMethodPlot: elbow.image ? `data:image/png;base64,${elbow.image}` : null,
        silhouetteScoresPlot: silhouetteScores.image ? `data:image/png;base64,${silhouetteScores.image}` : null,
        kmeansPlot: kmeans.image ? `data:image/png;base64,${kmeans.image}` : null

      });
      } catch (error) {
        console.error("Error fetching images:", error);
      }
    };
    fetchImages();
  }, []);

  return (
    <div className="App">
      <div>
        {images.startingColumns
          ? <img src={images.startingColumns} alt="Starting Columns" />
          : <div>Loading Starting Columns...</div>}
      </div>
      <div>
        {images.columnsWithoutZeros
          ? <img src={images.columnsWithoutZeros} alt="Without Zeros" />
          : <div>Loading Without Zeros...</div>}
      </div>
      <div>
        {images.columnsWithoutOutliers
          ? <img src={images.columnsWithoutOutliers} alt="Without Outliers" />
          : <div>Loading Without Outliers...</div>}
      </div>
      <div>
        {images.elbowMethodPlot
          ? <img src={images.elbowMethodPlot} alt="Elbow Method Plot" />
          : <div>Loading Elbow Method Plot...</div>}
      </div>
      <div>
        {images.silhouetteScoresPlot
          ? <img src={images.silhouetteScoresPlot} alt="Elbow Method Plot" />
          : <div>Loading Elbow Method Plot...</div>}
      </div>
      <div>
        {images.kmeansPlot
          ? <img src={images.kmeansPlot} alt="Elbow Method Plot" />
          : <div>Loading Elbow Method Plot...</div>}
      </div>
    </div>
  );
}

export default App;
