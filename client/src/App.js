import { Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import ClusterEvalPlots from './components/ClusterEvalPlots';
import usePlots from './hooks/usePlots';
import DataOverviewPlots from './components/DataOverviewPlots';
import ClusterClassPlots from './components/ClusterClassPlots';
import DataExploration from './components/DataExploration';

function App() {
  const navigate = useNavigate();
  const { images } = usePlots();
  const handleClick = (route) => {
    navigate(`/${route}`)
  }
  return (
    <div className="App">
      <nav className='navbar'>
        <span className="nav-link" onClick={() => handleClick('')}>Data Overview Plots</span>
        <span className="nav-link" onClick={() => handleClick('DataExploration')}>Data Exploration</span>
        <span className="nav-link" onClick={() => handleClick('ClusterEvalPlots')}>Cluster Evalutaion Plots</span>
        <span className="nav-link" onClick={() => handleClick('ClusterClassPlots')}>Clustering And Classification Plots</span>
      </nav>
      <Routes>
        <Route path='/' element={<DataOverviewPlots images={images} />} />
        <Route path='/ClusterEvalPlots' element={<ClusterEvalPlots images={images} />}/>
        <Route path='/ClusterClassPlots' element={<ClusterClassPlots images={images} />} />
        <Route path='/DataExploration' element={<DataExploration images={images} />} />
      </Routes>
    </div>
  );
};
export default App;