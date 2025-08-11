
const DataOverviewPlots = ({ images }) => {
    return (
        <div>
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
        </div>
    )
};

export default DataOverviewPlots;