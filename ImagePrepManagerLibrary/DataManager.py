from ImagePartition import ImagePartition
from ImageFormat import ImageFormat
from ImageCollection import ImageCollection
from CustomExceptions import ObjectExistError
import os

# Example: 
# your_workspace
# - staging_area
# - - label_folder1
# - - label_folder2
#                 .
#                 .
#                 .
# - - raw_file1.jpg
#                 ,
#                 .
#                 .
# - test_folder
# - train_folder

class DataManager:

    # OK
    def __init__(self, workspace: str, dest_path_1: str, dest_path_2: str, labels: str):

        staging_path = os.path.join(workspace, "staging")
        if not os.path.exists(staging_path):
            os.mkdir(staging_path)

        self.folders = {}
        for label in labels:
            label_path = os.path.join(staging_path, label)
            if not os.path.exists(label_path):
                os.mkdir(label_path)
            self.folders[label] = ImageCollection(label_path, dest_path_1, dest_path_2)
        
        self.staging = ImagePartition(staging_path, *[os.path.join(staging_path, label) for label in labels])

    # OK
    def format_files(self, folder_name: str):
        if not folder_name in self.folders.keys():
            raise ObjectExistError(f"Label does not not exist in labels.")
        self.folder[folder_name].format_data()

    # OK
    def format_files_all(self):
        for folder_name in self.folders.keys():
            self.format_files(label_name)

    # OK
    def export_to_folders(self):
        self.staging.partition_equally()

    # OK
    def export_to_folder(self, folder_name: str):
        if not folder_name in self.folders.keys():
            raise ObjectExistError(f"Label does not not exist in labels.")
        
        self.staging.partition_to(self.folders[folder_name].get_path())

    # OK
    def split_train_test(self, train_to_test_ratio: int):
        for label_partition in self.folders.values():
            label_partition.partition_data(train_to_test_ratio)
    
    # OK
    def change_staging_area(self, new_path):

        # Make directories and update label image collection
        for folder_name, folder_collection in self.folders.items():
            folder_path_new = os.path.join(new_path, folder_name)
            if not os.path.exists(folder_path_new):
                os.mkdir(folder_path_new)
            folder_collection.change_source_path(folder_path_new)

        self.staging = ImagePartition(new_path, *[os.path.join(new_path, label) for label in self.folders.keys()])

    # OK 
    def get_staging_path(self):
        return self.staging.source_path