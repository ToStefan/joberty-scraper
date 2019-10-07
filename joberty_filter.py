import sys
sys.path.append("..")

import json

from utils import clear, write_file
from constants import JOBERTY_FILE_PATH_TODAY, switch_employee_numbers, switch_empy_num_variation


def filter_by_city(data, city):
	companies = ""
	company_number = 1
	for company in data:
		if(str(company["city"]).lower() == city.lower()):
			companies += "{}) {} ({}) /{}\n".format(company_number, company["name"], company["website"], company["employeeNumber"])
			company_number += 1
	return companies

def filter_company_cities(data):
	cities = {}
	cities_variation = {}
	companies_without_city = 0
	companies_num = 0
	for company in data:
		city = str(company["city"])
		employeeNumber = company["employeeNumber"]
		if(city != "None"):
			companies_num += 1
			if city in cities:
				cities[city] = cities[city] + switch_employee_numbers(employeeNumber)
				cities_variation[city] = cities_variation[city] + switch_empy_num_variation(employeeNumber)
			else:
				cities[city] = switch_employee_numbers(employeeNumber)
				cities_variation[city] = switch_empy_num_variation(employeeNumber)
		else:
			companies_without_city += 1


	total_empy_num = str(sum(cities[item] for item in cities))
	for key, value in cities_variation.items():
		cities[key] = str(cities[key]) + " (+/-" + str(cities_variation[key]) + ")"
	for key, value in cities.items():
		print(">{: ^12} ~{}".format(key, value))
	print("{:_<32}\n".format(""))
	print("Cities: " + str(len(cities)))
	print("Employee number:  ~" + total_empy_num)
	print("Total companies: " + str(companies_num + companies_without_city) + " (" \
				+ str(companies_num) + ")")
	print("Companies without city: " + str(companies_without_city))

	
if __name__ == '__main__':
	clear()
	f = open(JOBERTY_FILE_PATH_TODAY, encoding="utf-8")
	json_list = json.load(f)
	if(sys.argv[1].lower() == "city"):
		filter_company_cities(json_list)
	else:
		print(filter_by_city(json_list, sys.argv[1]))