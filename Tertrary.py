import DataPartition
import DataFormat
import CustomExceptions


# Consider: 
# Images
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
# - test_fodler
# - train_folder

class Tertrary:

    # Check data partition source path
    def __init__(self, workspace: str, train_path: str, test_path: str, labels: str):

        self.repo = {}
        for label in labels:
            label_path = os.path.join(workspace, label)
            if not os.path.exists(label_path):
                os.makedirs(label_path)
            self.repo[label] = DataPartition(label_path, train_path, test_path)
            # DataFormat(label_path)

        
        staging_path = os.path.join(image_path,"staging")
        if not os.path.exists(staging_path):
            os.makedirs(staging_path)
        
        self.data_format = DataFormat(staging_path)

    # TODO: Resize files if the are too fucking big
    def format_files(self, label_name:str):
        if not label_name in self.labels:
            raise ObjectExistError(f"Label {label_name} is not an existing label.")
        self.data_format.convert_pdf_to_jpeg()
        self.data_format.rename_files_uuid(label_name)
    
    # TODO
    def format_all_labels_files(self):
        self.data_format.convert_pdf_to_jpeg()
        self.data_format.rename_files_uuid_all(self.labels)
    
    # TODO
    def move_to_labels(self):
        dir = os.path.dirname(self.staging_area)
        label_path = [os.path.join(dir, label) for label in labels]
        partition = DataPartition(self.staging_area, *label_path)
        partiton.distribute_by_basename()
    
    # TODO
    def move_to_label(self, label_name: str):
        if not label in self.labels:
            raise ObjectExistError(f"Label does not not exist in labels: {self.labels}")
        
        label_path = os.path.join(os.path.dirname(self.staging_area), label_name)
        partition = DataPartition(self.staging_area, label_path, None)
        partition.move_to_partition_1()
        self.clear_staging_area()

    # TODO
    def split_train_test(train_to_test_ratio: int):
        for label_partition in self.repo:
            label_partition.partition_split_two(train_to_test_ratio)
    
    # TODO
    def clear_staging_area(self):
        partition = DataPartition(self.staging_area)
        partition.clear_source()