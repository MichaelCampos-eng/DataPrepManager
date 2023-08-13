from ImagePartition import ImagePartition
from ImageFormat import ImageFormat
import os

class ImageCollection:

    # OK
    def __init__(self, source_path: str, *args):
        self.source_path = source_path
        self.partition = ImagePartition(source_path, *args)
        self.data_format = ImageFormat(source_path)
    
    # OK
    def format_data(self):
        self.data_format.convert_pdf_to_jpeg()
        self.data_format.rename_files_uuid()
    
    # OK
    def partition_data(self, ratio: int):
        self.partition.partition_split_two(ratio)
    
    def change_source_path(self, new_path: str):
        self.source_path = new_path
        self.partition.source_path = new_path
        self.data_format.source_path = new_path
    
    # OK 
    def get_path(self):
        return self.source_path