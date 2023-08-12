import DataPartition
import DataFormat

class DataCollection:

    # Check data partition source path
    def __init__(self, workspace: str, dest_path_1: str, dest_path_2: str):
        self.partition = DataPartition(workspace, dest_path_1, dest_path_2)
        self.data_format = DataFormat(workspace)
    
    def format_data(self):
        self.data_format.convert_pdf_to_jpeg()
        self.data_format.rename_files_uuid()
    
    def partition_data(self, ratio: int):
        self.partition_split_two(ratio)