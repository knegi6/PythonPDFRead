

from os import chdir, listdir
from os.path import isfile, join, exists, isdir
# import camelot
import camelot as cam
import ghostscript
import os
import pandas as pd

def get_policy_no_from_table(pdf_path):
    table = cam.read_pdf(pdf_path , pages = '1', flavor = 'stream')
    policy_no = table[0].df[[0,1]].iat[2,1]
    print(policy_no)
    return policy_no

# print("\\".join((r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")))
# print(os.getcwd())
# new_file_name = join(r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")
# print(new_file_name)


def get_files(path):
    for file in listdir(path):
        full_path = join(path, file)
        if isfile(full_path):
            if exists(full_path):
                yield full_path


def get_directories(path):
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


def get_files_recursively(directory):
    yield from get_files(directory)
    for subdirectory in get_directories(directory):
        yield from get_files_recursively(subdirectory)


files = get_files_recursively(r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\4_8_2022\SPLIT\ck.pdf_SPLIT_FOLDER")
agent_code_dictionary={"Path":"Policy Number"}


for file_path in files:
    #agent_code = extract_agent_code(get_text_from_pdf_into_list(file_path))

    agent_code_dictionary[file_path]= get_policy_no_from_table(file_path)

#print(agent_code_dictionary)



df = pd.DataFrame(data=agent_code_dictionary, index=[0])
#df = pd.DataFrame(data=agent_code_dictionary)

df = (df.T)
print(df)

df.to_excel(r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\4_8_2022\Input\ck.pdf_WCT_Indexing_Input_File.xlsx")

