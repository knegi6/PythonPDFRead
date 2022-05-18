# Code for master excel input  file creation for agent codes

import excel_others_operations as eoo
import pdf_read as pdfr
import glob
import os
import camelot as cam
# from os.path import join

def get_top_right_agent_code(file):
    #source: file:///C://Users//kulra//OneDrive/Desktop/ilovepdf_split/12%202021%20120%20Day%20OS%20Checks%2005%2018%2021%20to%2008%2007%2021%20%20143%202%20pg-1.pdf
    table = cam.read_pdf(file, pages = '1', flavor = 'stream')
    print("table[0] ", table[0])
    top_right_agent_code = table[0].df.iat[0,1]
    if (top_right_agent_code == "" or top_right_agent_code == None):
        raise Exception("Agent Code Not found")
    else:
        print(table[0].df.iat[0,1])
        return top_right_agent_code

import pandas as pd
master_csv= (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\GAFG_Agentb_Master_Excel.csv")
master_excel= (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_13_2022\Master_Excel_AgentB_4_13_2022.xlsx")

df=pd.read_csv(master_csv)
# df=pd.read_excel(master_excel)
# df=pd.read_csv(master_excel)
# print(df)



pfr=pdfr.PdfRead()
eop=eoo.ExcelAndPandasOperation()

for index, row in df.iterrows():
    # print (row["SPLITTED FOLDER NAME"], row["INPUT FILENAME"])
    file_list = glob.glob(os.path.join(row["SPLITTED FOLDER NAME"],"*pdf"))
    # print(file_list[0])
    print("row[PDF NAME] ",row["PDF NAME"])
    agent_code_dict={"Path":"Agent Code"}
    for file in file_list:
        
        try:
            # agent_code_dict[file]=pfr.get_policy_no_from_table(file)

            agent_code_dict[file]= pfr.get_top_right_agent_code(file)
        except Exception as e:
            print("error")
            print(e)
            try:
                agent_code_dict[file]= pfr.get_data_after_colon_agent_code(pfr.get_text_from_pdf_into_list(file))
            except Exception as e2:
                print("error2")
                print(e2)
                try:
                    agent_code_dict[file]= pfr.extract_agent_code_which_is_the_first_line_of_pdf(pfr.get_text_from_pdf_into_list(file))
                except Exception as e3:
                    print("error3")
                    print(e3)
                    try:                    
                        agent_code_dict[file]= pfr.get_agent_code_after_confirmation_Maryland(pfr.get_text_from_pdf_into_list(file))
                    except Exception as e4:
                        print("error4")
                        print(e4)
            # agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pfr.get_text_from_pdf_into_list(file))
            # agent_code_dict[file]=pfr.get_policy_no_from_table(file)

            # agent_code_dict[file]=get_top_right_agent_code(file)
        # else:
        #     agent_code_dict[file]=pfr.get_policy_no_from_table(file)


    
    df = pd.DataFrame(data=agent_code_dict, index=[0])

    df = (df.T)

    # print (df)

    df.to_excel(row["INPUT FILENAME"])
    eop.delete_first_row_from_Sheet1(row["INPUT FILENAME"])
    print("row[INPUT FILENAME]" ,row['INPUT FILENAME'])
    # agent_code_dict={}    