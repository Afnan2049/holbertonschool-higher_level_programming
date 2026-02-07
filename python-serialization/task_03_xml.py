#!/usr/bin/env python3
import xml.etree.ElementTree as ET

"""
Module for serializing and deserializing dictionaries using XML.
"""

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.
    
    Args:
        dictionary (dict): The data to serialize.
        filename (str): The output filename.
    """
    # Create the root element <data>
    root = ET.Element("data")
    
    # Iterate through dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML only stores text
    
    # Create the tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    
    Args:
        filename (str): The XML file to read.
        
    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from child elements
        # Note: All values will be strings by default in XML
        return {child.tag: child.text for child in root}
        
    except (FileNotFoundError, ET.ParseError):
        return None
