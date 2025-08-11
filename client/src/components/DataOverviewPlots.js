import '../App.css';
const DataOverviewPlots = ({ images }) => {
    return (
        <div className='Container'>
            <div className="plot-box">
                <p>
                  <strong>Raw Data Distributions: </strong>  
                   These plots show the distribution of each feature in the original dataset, including all raw values.
                </p>
                {images.startingColumns
                ? <img src={images.startingColumns} alt="Starting Columns" />
                : <div>Loading Starting Columns...</div>}
            </div>
            <div className="plot-box">
                <p>
                  <strong>Zero Values Handled: </strong>  
                  Here, zero values in key features have been replaced with the median of each column, providing a more realistic view of the data distributions.
                </p>
                {images.columnsWithoutZeros
                ? <img src={images.columnsWithoutZeros} alt="Without Zeros" />
                : <div>Loading Without Zeros...</div>}
            </div>
            <div className="plot-box">
                <p>
                  <strong>Outliers Removed: </strong>  
                  These plots display the distributions after removing statistical outliers, giving a clearer picture of the typical data range.
                </p>
                {images.columnsWithoutOutliers
                ? <img src={images.columnsWithoutOutliers} alt="Without Outliers" />
                : <div>Loading Without Outliers...</div>}
            </div>
        </div>
    )
};

export default DataOverviewPlots;