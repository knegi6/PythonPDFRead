import pandas as pd
import openpyxl as opxl
import files_folder_operations as ffo
#from files_folder_operations import FilesAndFolderOperations as ffo
import glob
from pdf_read import PdfRead as pr

class ExcelAndPandasOperation:

    def delete_first_row_from_Sheet1(self, excel_file_path):
        excel_file = opxl.load_workbook(excel_file_path)
        excel_sheet = excel_file['Sheet1']

        # delete column
        excel_sheet.delete_rows(idx=1) # row 1 is deleted]
        excel_file.save(excel_file_path)


    
    
    files = ffo.get_files_recursively(r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\4_8_2022\SPLIT\ck.pdf_SPLIT_FOLDER")
    agent_code_dictionary={"Path":"Agent Code"}
    policy_number_dictionary={"Path":"Policy Number"}


    for file_path in files:
        #agent_code = extract_agent_code(get_text_from_pdf_into_list(file_path))

        agent_code_dictionary[file_path]= pr.get_policy_no_from_table(file_path)

    #print(agent_code_dictionary)



    df = pd.DataFrame(data=agent_code_dictionary, index=[0])
    #df = pd.DataFrame(data=agent_code_dictionary)

    df = (df.T)
    print(df)

    df.to_excel(r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\4_8_2022\Input\ck.pdf_WCT_Indexing_Input_File.xlsx")

