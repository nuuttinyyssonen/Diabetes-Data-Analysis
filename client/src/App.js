import { Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import ClusterEvalPlots from './components/ClusterEvalPlots';
import DataOverviewPlots from './components/DataOverviewPlots';
import ClusterClassPlots from './components/ClusterClassPlots';
import DataExploration from './components/DataExploration';

function App() {
  const navigate = useNavigate();
  const handleClick = (route) => {
    navigate(`/${route}`)
  }
  return (
    <div className="App">
      <nav className='navbar'>
        <span className="nav-link" onClick={() => handleClick('')}>Data Overview Plots</span>
        <span className="nav-link" onClick={() => handleClick('DataExploration')}>Data Exploration</span>
        <span className="nav-link" onClick={() => handleClick('ClusterEvalPlots')}>Cluster Evaluation Plots</span>
        <span className="nav-link" onClick={() => handleClick('ClusterClassPlots')}>Clustering And Classification Plots</span>
      </nav>
      <Routes>
        <Route index element={<DataOverviewPlots />} />
        <Route path='/ClusterEvalPlots' element={<ClusterEvalPlots />}/>
        <Route path='/ClusterClassPlots' element={<ClusterClassPlots />} />
        <Route path='/DataExploration' element={<DataExploration />} />
      </Routes>
    </div>
  );
};
export default App;