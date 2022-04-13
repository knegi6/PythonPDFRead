import fitz
import os
import pandas as pd


# os.chdir(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_7_2022\SPLIT\April 2022 AML 30-day Notice.pdf_SPLIT_FOLDER")
print(os.getcwd())

pdf_document = (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\done 4_7_2022\SPLIT\Deferred Comp and Defined Contribution Payout Letters.pdf_SPLIT_FOLDER\Deferred Comp and Defined Contribution Payout Letters-5.pdf")

def get_text_from_pdf_into_list(pdf_path):
    doc = fitz.open(pdf_path)
    #print ("number of pages: %i" % doc.pageCount)
    #print(doc.metadata)

    page = doc.load_page(0)
    page_text = page.get_text("text")
    print(page_text)

    #page_text_list = {}
    #page_text_list = page1text.list()

    #print(type(page_text))
    page_text_list = page_text.split("\n")
    # print(type(page_text_list))

    # print(page_text_list)
    return page_text_list
#agentCode = ""


def extract_agent_code_which_is_the_first_line_of_pdf(page_text_list):
    agentCode = page_text_list[0]
    agentCode = agentCode.strip()
    print(agentCode)
    return agentCode

# agent_code = extract_agent_code(get_text_from_pdf_into_list(pdf_document))
# list1 =get_text_from_pdf_into_list(pdf_document)
# print(extract_agent_code(list1))
#print(agent_code)
# print(agentCode.length())

# from os import chdir, listdir
# from os.path import isfile, join, exists, isdir
# import camelot

# # print("\\".join((r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")))
# # print(os.getcwd())
# # new_file_name = join(r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")
# # print(new_file_name)


# def get_files(path):
#     for file in listdir(path):
#         full_path = join(path, file)
#         if isfile(full_path):
#             if exists(full_path):
#                 yield full_path


# def get_directories(path):
#     for directory in listdir(path):
#         full_path = join(path, directory)
#         if isdir(full_path):
#             if exists(full_path):
#                 yield full_path


# # def get_files_recursively(directory):
# #     for file in get_files(directory):
# #         yield file
# #     for subdirectory in get_directories(directory):
# #         for file in get_files_recursively(subdirectory):
# #             yield file

# # simplified version of above function


# def get_files_recursively(directory):
#     yield from get_files(directory)
#     for subdirectory in get_directories(directory):
#         yield from get_files_recursively(subdirectory)


# files = get_files_recursively(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\done 4_7_2022\SPLIT\Deferred Comp and Defined Contribution Payout Letters.pdf_SPLIT_FOLDER")
# agent_code_dictionary={"Path":"Agent Code"}


# for file_path in files:
#     #agent_code = extract_agent_code(get_text_from_pdf_into_list(file_path))

#     agent_code_dictionary[file_path]= extract_agent_code(get_text_from_pdf_into_list(file_path))

# print(agent_code_dictionary)



# df = pd.DataFrame(data=agent_code_dictionary, index=[0])
# #df = pd.DataFrame(data=agent_code_dictionary)

# df = (df.T)
# print(df)

# df.to_excel(r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\done 4_7_2022\Input\Deferred Comp and Defined Contribution Payout Letters - by python.xlsx")

