from constants import switch_industry, JOBERTY_FILE_PATH_TODAY
from utils import write_file, get_json


def scrap_joberty():
	companies_count = get_joberty_companies_count()
	company_list = []
	company_count = 0
	
	for page in range(get_joberty_page_count()):
		all_companies = get_json("https://backend-test.joberty.rs/api/v1/user/company/search?q=&p=" + str(page))
		for company in all_companies["items"]:

			company_id = company["id"]
			company_details = get_json("https://backend-test.joberty.rs/api/v1/user/company/" + str(company_id))

			json_object = {}
			json_object["id"] = company_id
			json_object["name"] = str(company_details["name"])
			json_object["industry"] = switch_industry(company["industryId"])
			#Promenjeno 11.09,  continue or pass? dodaje samo sa gradom
			try: json_object["city"] = str(company_details["city"])
			except: continue
			json_object["website"] = str(company_details["website"])
			json_object["employeeNumber"] = str(company_details["employeeNumber"])
			json_object["foundingYear"] = company_details["foundingYear"]
 
			company_list.append(json_object)
			company_count += 1
			print(">> " + str(company_count) + "/" + str(companies_count) + " companies added")

	return company_list

def get_joberty_page_count():
	data = get_json("https://backend-test.joberty.rs/api/v1/user/company/search?q=&p=0")
	return data['totalPage']

def get_joberty_companies_count():
	data = get_json("https://backend-test.joberty.rs/api/v1/user/company/search?q=&p=0")
	return data["totalElements"]


if __name__ == '__main__':
	data = scrap_joberty()
	write_file(JOBERTY_FILE_PATH_TODAY, data)