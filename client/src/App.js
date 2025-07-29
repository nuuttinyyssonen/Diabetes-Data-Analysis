import { useEffect, useState } from "react";
import visualizationServices from "./services/visualizationServices";
import './App.css';

function App() {
  const [startingColumnsSrc, setStartingColumnsSrc] = useState(null);
  const [columnsWithoutZerosSrc, setColumnsWithoutZerosSrc] = useState(null);
  const [columnsWithoutOutliersSrc, setColumnsWithoutOutliersSrc] = useState(null);

  const starting = async () => {
    try {
      const starting = await visualizationServices.getStartingColumns();
      if (starting.image) setStartingColumnsSrc(`data:image/png;base64,${starting.image}`);
    } catch (error) {
      console.error("Error fetching starting columns:", error);
    }
  }

  const zeros = async () => {
    try {
      const zeros = await visualizationServices.getColumnsWithoutZeros();
      if (zeros.image) setColumnsWithoutZerosSrc(`data:image/png;base64,${zeros.image}`);
    } catch (error) {
      console.error("Error fetching columns without zeros:", error);
    }
  }

  const outliers = async () => {
    try {
      const outliers = await visualizationServices.getColumnsWithoutOutliers();
      if (outliers.image) setColumnsWithoutOutliersSrc(`data:image/png;base64,${outliers.image}`);
    } catch (error) {
      console.error("Error fetching columns without outliers:", error);
    }
  }

  useEffect(() => {
    starting();
    zeros();
    outliers();
  }, [])

  return (
    <div className="App">
      {startingColumnsSrc && <img className="plt" src={startingColumnsSrc} alt="Starting Columns" />}
      {columnsWithoutZerosSrc && <img className="plt" src={columnsWithoutZerosSrc} alt="Columns Without Zeros" />}
      {columnsWithoutOutliersSrc && <img className="plt" src={columnsWithoutOutliersSrc} alt="Columns Without Outliers" />}
    </div>
  );
}

export default App;
