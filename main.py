from combiner import Combiner
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', help='Path to the folder containing your pictures and your logo if you want to use one', required=True)
parser.add_argument('--logo_name', help='The name of your logo file if you want to user one', required=False)
parser.add_argument('--logo_width', help='The width of the logo that will be used when pasted on the final picture', required=False)
parser.add_argument('--logo_height', help='The height of the logo that will be used when pasted on the final picture', required=False)
args = parser.parse_args()

if (args.logo_name is not None and args.logo_width is None):
    raise Exception('Must specify a logo_width for the logo')
if (args.logo_name is not None and args.logo_height is None):
    raise Exception('Must specify a logo_height for the logo')

logo_width = None
logo_height = None
if args.logo_name is not None:
    logo_width = int(args.logo_width)
    logo_height = int(args.logo_height)



if __name__ == "__main__":
    logo = None
    combiner = Combiner(args.folder_path, args.logo_name, logo_width, logo_height)
    if args.logo_name is not None:
        logo = combiner.get_resized_logo()
    pictures_list = combiner.get_pictures_list()
    combiner.combine_pictures(pictures_list, logo)





