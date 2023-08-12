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
    def __init__(self, workspace: str, train_path: str, test_path: str, labels: str):

        staging_path = os.path.join(workspace, "staging")
        if not os.path.exists(staging_path):
            os.mkdir(staging_path)

        self.label_repo = {}
        for label in labels:
            label_path = os.path.join(staging_path, label)
            if not os.path.exists(label_path):
                os.mkdir(label_path)
            self.label_repo[label] = ImageCollection(label_path, train_path, test_path)
        
        self.staging = ImagePartition(staging_path, *[os.path.join(staging_path, label) for label in labels])

    # OK
    def format_files(self, label_name: str):
        if not label_name in self.label_repo.keys():
            raise ObjectExistError(f"Label does not not exist in labels.")
        self.label_repo[label_name].format_data()

    # OK
    def format_files_all(self):
        for label_name in self.label_repo.keys():
            self.format_files(label_name)

    # OK
    def export_to_labels(self):
        self.staging.partition_equally()

    # OK
    def export_to_label(self, label_name: str):
        if not label_name in self.label_repo.keys():
            raise ObjectExistError(f"Label does not not exist in labels.")
        
        self.staging.partition_to(self.label_repo[label_name].get_path())

    # OK
    def split_train_test(self, train_to_test_ratio: int):
        for label_partition in self.label_repo.values():
            label_partition.partition_data(train_to_test_ratio)
    
    # OK
    def change_staging_area(self, new_path):
        self.staging.source_path = new_path

        for label_name, label in self.label_repo.value():
            label_path_new = os.path.join(new_path, label_name)
            if not os.path.exists(label_path_new):
                os.mkdir(label_path)
            label.change_source_path(label_path_new)
