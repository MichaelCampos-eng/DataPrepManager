from pdf2image import convert_from_path
from CustomExceptions import DirectoryError, FileTypeError
import os
import uuid
import shutil
import numpy as np
from PIL import Image

class ImageFormat:

    # OK
    def __init__ (self, source_path: str):
        self.source_path = source_path

    # OK 
    def resize_images(self, factor: int):
        for file_name in os.listdir(self.source_path):
            if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
                file_path = os.path.join(self.source_path, file_name)
                image = Image.open(file_path)
                width, height = image.size
                target_size = (int(width//factor), int(height//factor))
                resized_image = image.resize(target_size, Image.LANCZOS)
                resized_image.save(file_path)

    # OK
    def rename_files_uuid(self):
        if not os.path.exists(self.source_path):
            raise DirectoryError("Directory {} does not exist!".format(self.source_path))

        files = os.listdir(self.source_path)
        for file in files:
            folder_name = os.path.basename(self.source_path)
            if not (file.endswith(".jpg") or file.endswith(".jpeg")):
                raise FileTypeError("Invalid file type. Remove or convert to jpeg.")
            imgnameNew = os.path.join(self.source_path, folder_name + '.' + '{}.jpeg'.format(str(uuid.uuid1())))
            imgnameOld = os.path.join(self.source_path, file)
            os.rename(imgnameOld, imgnameNew)        

    # OK
    def convert_pdf_to_jpeg(self):
        if not os.path.exists(self.source_path):
            raise DirectoryError("Images raw directory {} does not exist!".format(self.source_path))

        if len(os.listdir(self.source_path)) == 0:
            raise DirectoryError("Empty directory {}! Add files to it.".format(self.source_path))
        

        for file in os.listdir(self.source_path):
            if '.pdf' in file:
                filePath = os.path.join(self.source_path, file)
                images = convert_from_path(filePath)
                for i, image in enumerate(images):
                    jpgName = os.path.join(self.source_path, f'page_{i + 1}.jpeg') 
                    image.save(jpgName, 'JPEG')
                os.remove(filePath)
    
    