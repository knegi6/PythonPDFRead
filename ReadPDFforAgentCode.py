import fitz
import os
import pandas as pd

# def get_policy_number_drom_table(pdf_path)


# os.chdir(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_7_2022\SPLIT\April 2022 AML 30-day Notice.pdf_SPLIT_FOLDER")
print(os.getcwd())

pdf_document = (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_7_2022\SPLIT\April 2022 AML 30-day Notice.pdf_SPLIT_FOLDER\April 2022 AML 30-day Notice-1.pdf")

def get_text_from_pdf_into_list(pdf_path):
    doc = fitz.open(pdf_path)
    print ("number of pages: %i" % doc.pageCount)
    #print(doc.metadata)

    page = doc.load_page(0)
    page_text = page.get_text("text")
    #print(page_text)

    #page_text_list = {}
    #page_text_list = page1text.list()

    #print(type(page_text))
    page_text_list = page_text.split("\n")
    # print(type(page_text_list))

    # print(page_text_list)
    return page_text_list
#agentCode = ""

def find_agent_code_line(page_text_list):
    for item in page_text_list:
        if item.startswith("Agent Code:"):
            agent_code_line = item
            return agent_code_line
            break
    #return agentCode

def extract_agent_code(page_text_list):
    agentCode = find_agent_code_line(page_text_list)
    print(agentCode)
    agentCode = agentCode.replace("Agent Code: ","")
    agentCode = agentCode.strip()
    return agentCode

agent_code = extract_agent_code(get_text_from_pdf_into_list(pdf_document))

print(agent_code)
# print(agentCode.length())

from os import chdir, listdir
from os.path import isfile, join, exists, isdir
import camelot

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


files = get_files_recursively(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_7_2022\SPLIT\April 2022 AML Term Notice_Clean-up.pdf_SPLIT_FOLDER")
agent_code_dictionary={"Path":"Agent Code"}


for file_path in files:
    #agent_code = extract_agent_code(get_text_from_pdf_into_list(file_path))

    agent_code_dictionary[file_path]= extract_agent_code(get_text_from_pdf_into_list(file_path))

#print(agent_code_dictionary)



df = pd.DataFrame(data=agent_code_dictionary, index=[0])
#df = pd.DataFrame(data=agent_code_dictionary)

df = (df.T)
print(df)

df.to_excel(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_7_2022\Input\April 2022 AML Notice_Clean-up.xlsx")


