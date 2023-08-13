from CustomExceptions import DirectoryError, InputSizeError
import numpy as np
import os
import shutil

class ImagePartition:

    # OK
    def __init__ (self, source_path: str, *partitions_paths):
        if not os.path.exists(source_path):
            raise DirectoryError("Directory {} does not exist!".format(source_path))
        for part_path in partitions_paths:
            if not os.path.exists(part_path):
                raise DirectoryError("Directory {} does not exist!".format(part_path))
        
        self.source_path = source_path
        self.partitions_paths = partitions_paths
    
    # OK
    def partition_to(self, path: str):
        if not os.path.exists(self.source_path):
            raise DirectoryError("Directory {} does not exist!".format(self.source_path))
        
        if not os.path.exists(path):
            raise DirectoryError("Directory {} does not exist!".format(path))
        
        for file in os.listdir(self.source_path):
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                shutil.move(os.path.join(self.source_path, file), path)

    # OK
    def partition_equally(self):
        file_names = np.array([file for file in os.listdir(self.source_path) if os.path.isfile(os.path.join(self.source_path, file))])
        num_files = len(file_names)
        num_partitions = len(self.partitions_paths)

        print(self.source_path)
        
        part_file_names = np.array_split(file_names, num_partitions)
        for i in range(num_partitions):
            for file_name in part_file_names[i]:
                shutil.move(os.path.join(self.source_path, file_name), os.path.join(self.partitions_paths[i], file_name))

    # OK
    def partition_split_two(self, ratio_one_two: int):

        if ratio_one_two < 0 or ratio_one_two > 1:
            raise InputSizeError(f"Ratio {ratio_one_two} outside range [0, 1]")
        if len(self.partitions_paths) != 2:
            raise InputSizeError(f"No. of partitions {len(self.partitions_paths)} is not 2.")

        if not os.path.exists(self.source_path):
            raise DirectoryError("Directory {} does not exist!".format(self.source_path))
        if not os.path.exists(self.partitions_paths[0]):
            raise DirectoryError("Directory {} does not exist!".format(self.partitions_paths[0]))
        if not os.path.exists(self.partitions_paths[1]):
            raise DirectoryError("Directory {} does not exist!".format(self.partitions_paths[1]))

        # Clears old folders
        self.__delete_contents(self.partitions_paths[0])
        self.__delete_contents(self.partitions_paths[1])

        files = os.listdir(self.source_path)
        count = len(files) * ratio_one_two
        for file in files:
            file_path = os.path.join(self.source_path, file)
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                if count == 0:
                    self.__move_to(file_path, self.partitions_paths[1])
                else:
                    self.__move_to(file_path, self.partitions_paths[0])
                    count -= 1
    
    # Generalize this
    def __move_to(self, img_path, location_path):
        xml_path = img_path.replace(".jpeg", ".xml") if img_path.endswith(".jpeg") else img_path.replace(".jpg", ".xml")

        if not os.path.exists(img_path):
            raise DirectoryError("Image File {} does not exist!".format(img_path))

        if not os.path.exists(xml_path):
            raise DirectoryError("Label file {} does not exist! Format or create file.".format(xml_path))
        
        if not os.path.exists(location_path):
            raise DirectoryError("Destination folder {} does not exist!".format(location_path))

        shutil.move(img_path, location_path)
        shutil.move(xml_path, location_path)

    # OK    
    def __delete_contents(self, p):
        for file in os.listdir(p):
            os.remove(os.path.join(p, file))