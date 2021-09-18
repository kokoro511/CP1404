import shutil
import os

def main():
    file_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        
        extension = filename.split('.')[-1]
        if extension not in file_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            file_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(file_to_category[extension], filename))


main()
