from datetime import date


JOBERTY_FILE_PATH_TODAY = "data/joberty_companies_" + date.today().strftime("%d-%m-%Y") + ".json"


def switch_industry(identifier):
    switcher = {
        1: "Biotechnology",
        2: "Commerce",
        3: "Consumer Electronics",
        4: "Data and Analytics",
        5: "Design",
        6: "Education",
        7: "Energy",
        8: "Engineering",
        9: "Financial Services",
        10: "Gambling",
        11: "Gaming",
        12: "Hardware",
        13: "Internet Services",
        14: "IOT",
        15: "IT Services",
        16: "Marketing",
        17: "Media",
        18: "Software Outsourcing",
        19: "Professional Services",
        20: "Public Sector",
        21: "Science",
        22: "Software",
        23: "Telecommunications",
        24: "Other"
    }
    return switcher.get(identifier, "")

def switch_employee_numbers(number):
    switcher = {
        "<20": 10,
        "20-50": 35,
        "51-100": 75,
        "101-250": 175,
        "251-500": 375,
        "501-1000": 750,
        "1000+": 1050
    }
    return switcher.get(number, 0)

def switch_empy_num_variation(number):
    switcher = {
        "<20": 10,
        "20-50": 15,
        "51-100": 25,
        "101-250": 75,
        "251-500": 125,
        "501-1000": 250,
        "1000+": 200
    }
    return switcher.get(number, 0)  