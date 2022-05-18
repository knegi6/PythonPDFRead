# Code for master excel input  file creation for Policy Number

import excel_others_operations as eoo
import pdf_read as pdfr
import glob
import os
import pdf_read_OCR as pocr
# from os.path import join


import pandas as pd
# master_csv= (r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\4_28_2022\Master_Excel_WCT_4_28_2022.csv")
# master_excel= (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\4_13_2022\Master_Excel_AgentB_4_13_2022.xlsx")

# df=pd.read_csv(master_csv)
# # df=pd.read_excel(master_excel)
# # df=pd.read_csv(master_excel)
# # print(df)


pdf_file = (r"\\Bpspfilnor401\BluePrism\GAFG\GAFG_AgentB_Indexing\New folder\B DENAULT.pdf")
pfr=pdfr.PdfRead()
eop=eoo.ExcelAndPandasOperation()

pdfr.get_data_after_colon_social_security_number(pocr.get_text_from_any_pdf_into_list(pdf_file))

# for index, row in df.iterrows():
#     # print (row["SPLITTED FOLDER NAME"], row["INPUT FILENAME"])
#     file_list = glob.glob(os.path.join(row["SPLITTED FOLDER NAME"],"*pdf"))
#     # print(file_list[0])
#     print(row["PDF NAME"])
#     agent_code_dict={"Path":"Policy Number"}
#     for file in file_list:
        
#         try:
#             # agent_code_dict[file]=pfr.get_policy_no_from_table(file)

#             agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pocr.get_text_from_any_pdf_into_list(file))
#         except Exception as e:
#             print("error")
#             print(e)
#             # agent_code_dict[file]= pfr.get_data_after_colon_agent_code(pfr.get_text_from_pdf_into_list(file))

#             agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pfr.get_text_from_pdf_into_list(file))
#             # agent_code_dict[file]=pfr.get_policy_no_from_table(file)

#             # agent_code_dict[file]=get_top_right_agent_code(file)
#         # else:
#         #     agent_code_dict[file]=pfr.get_policy_no_from_table(file)


    
#     df = pd.DataFrame(data=agent_code_dict, index=[0])

#     df = (df.T)

#     # print (df)

#     df.to_excel(row["INPUT FILENAME"])
#     eop.delete_first_row_from_Sheet1(row["INPUT FILENAME"])
#     print(row['INPUT FILENAME'])
#     # agent_code_dict={} 