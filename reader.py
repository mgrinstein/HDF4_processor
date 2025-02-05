from pyhdf.SD import SD, SDC

def read_hdf_data(hdf_file, dataset_name):
    """Read dataset from an HDF4 file."""
    hdf = SD(hdf_file, SDC.READ)
    dataset = hdf.select(dataset_name)
    data = dataset[:]
    hdf.end()
    return data