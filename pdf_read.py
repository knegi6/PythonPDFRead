# from typing_extensions import Self
import fitz
import camelot as cam
import re

class PdfRead:

    def get_text_from_pdf_into_list(self,pdf_path):
        doc = fitz.open(pdf_path)
        # print ("number of pages: %i" % doc.pageCount)
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
            
    def find_agent_code_line(self, page_text_list):
        for item in page_text_list:
            if item.startswith("Agent Code"):
                agent_code_line = item
                return agent_code_line
                break
        #return agentCode

    def extract_agent_code(self, page_text_list):
        agent_code = self.find_agent_code_line(page_text_list)
        # print(agent_code)
        # if re.search("Agent Code: ", agent_code):
        #     agent_code = agent_code.replace("Agent Codes: ","")        
        # elif re.search("Agent Codes: ", agent_code):
        #     agent_code = agent_code.replace("Agent Code: ","")
        agent_code = agent_code.replace("Agent Code: ","")
        agent_code = agent_code.strip()
        return agent_code

    def find_policy_number_line(self, page_text_list):
        for item in page_text_list:
            if item.startswith("Policy Number:"):
                policy_number_line = item
                return policy_number_line
                break
        #return agentCode

    def find_contract_number_line(self, page_text_list):
        for item in page_text_list:
            if item.startswith("Contract"):
                contract_number_line = item
                print(contract_number_line)
                return contract_number_line
                break

    def get_data_after_colon_agent_code(self, text_list):
        agent_code = self.find_agent_code_line(text_list)
        print(agent_code)
        agent_code = agent_code.partition(":")[2]
        # agent_code = agent_code.split(":")[1]
        agent_code = agent_code.strip()
        return agent_code 

    def get_data_after_colon_contract_number(self, text_list):
        contract_code = self.find_contract_number_line(text_list)
        print(contract_code)
        # contract_code = contract_code.partition(":")[2]
        contract_code = contract_code.split(":")[1]
        contract_code = contract_code.strip()
        return contract_code 

        
    def extract_policy_number(self, page_text_list):
        policy_number = self.find_policy_number_line(page_text_list)
        print(policy_number)
        policy_number = policy_number.replace("Policy Number: ","")
        policy_number = policy_number.strip()
        return policy_number

    def extract_contract_number_from_2nd_page(self, pdf_path):
        table = cam.read_pdf(pdf_path, pages = '2', flavor = 'stream')

        #print(table[0].df[4])
        #table[0].df[[4,4]].to_excel("camelot_demo.xls")
        print(table[0].df[[4,4]].iat[6,1])
        #table[0].df[[4]]
        #print(table[0].df[4][table[0].df[4].str.strip().astype(bool)])
        #table[0].df[4][table[0].df[4].str.strip().astype(bool)].to_excel("camelot_demo.xls")
        #print(type(table[0].df[4][table[0].df[4].str.strip().astype(bool)]))

        contract_number = table[0].df[[4,4]].iat[6,1]
        return contract_number
    
        
    def extract_agent_code_which_is_the_first_line_of_pdf(self, page_text_list):
        agent_code = page_text_list[0]
        agent_code = agent_code.strip()
        print(agent_code)
        return agent_code

    def get_policy_no_from_table(self, pdf_path):
        table = cam.read_pdf(pdf_path , pages = '1', flavor = 'stream')
        policy_no = table[0].df[[0,1]].iat[2,1]
        print(policy_no)
        return policy_no    