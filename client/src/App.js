import { Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import ClusterEvalPlots from './components/ClusterEvalPlots';
import usePlots from './hooks/usePlots';
import DataOverviewPlots from './components/DataOverviewPlots';
import ClusterClassPlots from './components/ClusterClassPlots';

function App() {
  const navigate = useNavigate();
  const { images } = usePlots();
  const handleClick = (route) => {
    navigate(`/${route}`)
  }
  return (
    <div className="App">
      <div>
        <button onClick={() => handleClick('')}>1</button>
        <button onClick={() => handleClick('ClusterEvalPlots')}>2</button>
        <button onClick={() => handleClick('ClusterClassPlots')}>3</button>
      </div>
      <Routes>
        <Route path='/' element={<DataOverviewPlots images={images} />} />
        <Route path='/ClusterEvalPlots' element={<ClusterEvalPlots images={images} />}/>
        <Route path='/ClusterClassPlots' element={<ClusterClassPlots images={images} />} />
      </Routes>
    </div>
  );
};
export default App;