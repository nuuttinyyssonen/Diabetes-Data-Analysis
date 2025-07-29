import { useEffect, useState } from "react";
import visualizationServices from "./services/visualizationServices";

function App() {
  const [imageSrc, setImageSrc] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await visualizationServices.getStartingColumns();
        if(response.image) {
          setImageSrc(`data:image/png;base64,${response.image}`)
        }
      } catch (error) {
        console.error(error)
      }
    }
    fetchData();
  }, [])

  return (
    <div className="App">
      <img src={imageSrc}/>
    </div>
  );
}

export default App;
