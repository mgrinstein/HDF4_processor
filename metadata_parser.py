import xml.etree.ElementTree as ET

def parse_metadata(metadata_file):
    """Parse XML metadata file and extract bounding coordinates."""
    tree = ET.parse(metadata_file)
    root = tree.getroot()
    
    coordinates = {
        "west": float(root.find('.//WestBoundingCoordinate').text),
        "east": float(root.find('.//EastBoundingCoordinate').text),
        "north": float(root.find('.//NorthBoundingCoordinate').text),
        "south": float(root.find('.//SouthBoundingCoordinate').text)
    }
    return coordinates