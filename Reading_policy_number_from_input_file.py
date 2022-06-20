# Code for master excel input  file creation for Policy Number

from http.client import CONTINUE
import excel_others_operations as eoo
import pdf_read as pdfr
import glob
import os
import pdf_read_OCR as pocr
# from os.path import join



import pandas as pd
master_csv= (r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\WCT_Master_Excel.csv")

# master_csv= (r"\\Bpspfilnor401\BluePrism\GAFG\Correspb\GAFG_Correspb_Master_Excel.csv")

master_excel= (r"\\Bpspfilnor401\BluePrism\WCT\Correspb Indexing\WCT_Master_Excel.xlsx")

df=pd.read_csv(master_csv)
# df=pd.read_excel(master_excel)
# df=pd.read_csv(master_excel)
print(df)

pfr=pdfr.PdfRead()
eop=eoo.ExcelAndPandasOperation()

for index, row in df.iterrows():
    if row["STATUS"]=="PENDING":
        # print (row["SPLITTED FOLDER NAME"], row["INPUT FILENAME"])
        file_list = glob.glob(os.path.join(row["SPLITTED FOLDER NAME"],"*pdf"))
        # print(file_list[0])
        print(row["PDF NAME"])
        agent_code_dict={"Path":"Policy Number"}
        for file in file_list:
            
            try:
                # agent_code_dict[file]=pfr.get_policy_no_from_table(file)
                agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pfr.get_text_from_pdf_into_list(file))         

                # agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pocr.get_text_from_any_pdf_into_list(file))
            except Exception as e:
                print("error")
                print(e)
                try:
                # agent_code_dict[file]= pfr.get_data_after_colon_agent_code(pfr.get_text_from_pdf_into_list(file))
                    agent_code_dict[file]=pfr.get_policy_no_from_table(file)
                except Exception as ex:
                    print("error2")
                    print(ex)
                    try:

                        agent_code_dict[file]=pfr.extract_contract_number_from_2nd_page(file)
                    except Exception as exc:
                        print("error3")
                        print(exc)
                        agent_code_dict[file]= pfr.get_data_after_colon_policy_number(pfr.get_text_from_pdf_into_list(file))

                # agent_code_dict[file]= pfr.get_data_after_colon_contract_number(pfr.get_text_from_pdf_into_list(file))
                # agent_code_dict[file]=pfr.get_policy_no_from_table(file)

                # agent_code_dict[file]=get_top_right_agent_code(file)
            # else:
            #     agent_code_dict[file]=pfr.get_policy_no_from_table(file)

            df.at[index, "STATUS"] = "INPUT FILE CREATED"

    else:
        print(row["PDF NAME"])
        print(row["SPLITTED FOLDER NAME"])
        print("Skipped because status is not pending.")
        continue


    df.to_excel(master_excel)

    eop.delete_first_column_from_Sheet1(master_excel)
    df1 = pd.DataFrame(data=agent_code_dict, index=[0])

    df1 = (df1.T)

    # print (df)

    df1.to_excel(row["INPUT FILENAME"])
    eop.delete_first_row_from_Sheet1(row["INPUT FILENAME"])
    print(row['INPUT FILENAME'])
    # agent_code_dict={} 