from config import METADATA_FILE_PATH, HDF_FILE_PATH, DATASET_NAME
from metadata_parser import parse_metadata
from reader import read_hdf_data
from plotter import plot_data

def main():
    coordinates = parse_metadata(METADATA_FILE_PATH)
    print(f"Bounding Coordinates: {coordinates}")
    
    data = read_hdf_data(HDF_FILE_PATH, DATASET_NAME)
    print(f"Dataset Shape: {data.shape}")
    
    plot_data(data, coordinates, DATASET_NAME)

if __name__ == "__main__":
    main()
