import { useEffect, useRef, useState } from "react";
import visualizationServices from "../services/visualizationServices";

const usePlots = (plotKeys) => {
  const [images, setImages] = useState({});
  const effectRan = useRef(false);

  useEffect(() => {
    if(effectRan.current == false) {
      const fetchImages = async () => {
        try {
          const results = await Promise.all(
            plotKeys.map(key => visualizationServices.getData(key))
          );
          const newImages = {};
          plotKeys.forEach((key, index) => {
          const data = results[index];
          newImages[key] = data.image ? `data:image/png;base64,${data.image}` : null;
          if (key === "KNN" && data.confusion_matrix) {
            newImages.confusionMatrix = `data:image/png;base64,${data.confusion_matrix}`;
          }
          if (key === "clusterOutcomeHeatmap") {
            newImages.heatMap = data.image
              ? `data:image/png;base64,${data.image}`
              : null;
          }
        });
        setImages(newImages);
        console.log("effect ran")
        } catch (err) {
          console.error("Error fetching images:", err);
        }
      };
      fetchImages();
      return () => { 
        effectRan.current = true;
      };
    }
   }, [plotKeys.join(",")]);
  return images;
};

export default usePlots;