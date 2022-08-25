import cv2
import numpy
from os import listdir, makedirs
from os.path import isfile, join
from PIL import Image

class Combiner:
    OUTPUT_FOLDER = 'output'
    def __init__(self, folder_path, logo_name=None, logo_width=None, logo_height=None) -> None:
        if folder_path[-1] == '/' or folder_path[-1] == '\\':
            raise Exception(f'folder path must not end with slash or back slash but got {folder_path}')
        self.folder_path = folder_path
        self.logo_name = logo_name
        self.logo_width = logo_width
        self.logo_height = logo_height

    def get_resized_logo(self):
        logo_path = join(self.folder_path, self.logo_name)
        logo = Image.open(logo_path)
        return logo.resize((self.logo_width,self.logo_height))

    def get_pictures_list(self):
        pictures_list = [file for file in listdir(self.folder_path) if isfile(join(self.folder_path, file))]
        pictures_list.sort()
        if self.logo_name is not None:
            pictures_list.remove(self.logo_name)
        if len(pictures_list) % 2 != 0:
            raise Exception('Number of pictures in the folder must be even but there are {} pictures'.format(len(pictures_list)))
        return pictures_list

    def combine_pictures(self, pictures_list, logo=None):

        makedirs(self.OUTPUT_FOLDER, exist_ok=True)
        for i in range(0, len(pictures_list), 2):
            left_picture = cv2.imread(join(self.folder_path, pictures_list[i]))
            right_picture = cv2.imread(join(self.folder_path, pictures_list[i+1]))
            combined = numpy.concatenate((left_picture, right_picture), axis=1)
            combined = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)
            pil_combined = Image.fromarray(numpy.uint8(combined)).convert('RGB')
            pil_combined = Image.fromarray(combined.astype('uint8'), 'RGB')
            if logo is not None:
                pil_combined.paste(logo, (pil_combined.width-logo.width, pil_combined.height-logo.height),logo)
            pil_combined.save(f'{self.OUTPUT_FOLDER}/IMG_COMB_{i}.jpg')
