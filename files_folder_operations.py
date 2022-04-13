from os import chdir, listdir
from os.path import isfile, join, exists, isdir
import camelot
import glob


class FilesAndFolderOperations:
# class ffo:

    file_list = glob.glob("F:\Shinchan\*mp4")

    # print("\\".join((r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")))
    # print(os.getcwd())
    # new_file_name = join(r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")
    # print(new_file_name)


    def get_files(self, path):
        for file in listdir(path):
            full_path = join(path, file)
            if isfile(full_path):
                if exists(full_path):
                    yield full_path


    def get_directories(self, path):
        for directory in listdir(path):
            full_path = join(path, directory)
            if isdir(full_path):
                if exists(full_path):
                    yield full_path


    # def get_files_recursively(directory):
    #     for file in get_files(directory):
    #         yield file
    #     for subdirectory in get_directories(directory):
    #         for file in get_files_recursively(subdirectory):
    #             yield file

    # simplified version of above function


    def get_files_recursively(self, directory):
        yield from self.get_files(directory)
        for subdirectory in self.get_directories(directory):
            yield from self.get_files_recursively(subdirectory)

