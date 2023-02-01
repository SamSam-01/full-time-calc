from pprint import pprint

entreprises = {}

class PartTime:
    def __init__(self, start_date, end_date, coefficient):
        self.start_date = start_date
        self.end_date = end_date
        self.coefficient = coefficient

class Employe:
    def __init__(self, name, birtday, entry_date, end_date):
        self.name = name
        self.birtday = birtday
        self.entry_date = entry_date
        self.end_date = end_date
        self.part_time = []
    def add_part_time(self, start_date, end_date, coefficient):
        self.part_time.append(PartTime(start_date, end_date, coefficient))

class Entreprise:
    def __init__(self, name):
        self.name = name
        self.employees = {}
    def add_employee(self, employee_id, name, birtday, entry_date, end_date):
        self.employees[employee_id] = Employe(name, birtday, entry_date, end_date)

def get_part_time(line, entreprise_id, employee_id):
    string = line.split(":")[1].strip()
    start_date = string.split(",")[0].strip()
    end_date = string.split(",")[1].strip()
    coefficient = string.split(",")[2].strip()
    entreprises[entreprise_id].employees[employee_id].add_part_time(start_date, end_date, coefficient)

def get_employees(line, entreprise_id):
    string = line.split(":")[1].strip()
    employee_id = int(string.split(",")[0].strip())
    name = string.split(",")[1].strip()
    birthday = string.split(",")[2].strip()
    entry_date = string.split(",")[3].strip()
    end_date = string.split(",")[4].strip()
    entreprises[entreprise_id].add_employee(employee_id, name, birthday, entry_date, end_date)
    return employee_id

def get_entreprise_info(line, entreprise_id, employee_id):
    if ("salarié" in line):
        string = line.split(":")[1].strip()
        employee_id = int(string.split(",")[0].strip())
        return get_employees(line, entreprise_id)
    if (employee_id > 0):
        if ("temps partiel" in line):
            get_part_time(line, entreprise_id, employee_id)
    return employee_id

def parse_file(file_name):
    entreprise_id = 0
    employee_id = 0

    with open(file_name) as file:
        file.content = file.readlines()
    for line in file.content:
        if ("entreprise" in line):
            string = line.split(":")[1].strip()
            entreprise_id = int(string.split(",")[0].strip())
            entreprises[entreprise_id] = Entreprise(string.split(",")[1].strip())
        if (entreprise_id > 0) :
            employee_id = get_entreprise_info(line, entreprise_id, employee_id)
    return file.content

def print_entreprises():
    for entreprise in entreprises:
        print(entreprise, ' : ', entreprises[entreprise].name)
        print("nb employés : ", len(entreprises[entreprise].employees))
        for employee in entreprises[entreprise].employees:
            print('\t', employee, ' : ', entreprises[entreprise].employees[employee].name)
            print('\t', entreprises[entreprise].employees[employee].birtday, ' | ', entreprises[entreprise].employees[employee].entry_date, ' | ', entreprises[entreprise].employees[employee].end_date)
            for part_time in entreprises[entreprise].employees[employee].part_time:
                print('\t\t', part_time.start_date, ' | ', part_time.end_date, ' | ', part_time.coefficient)

def print_entreprise_info(entreprise_id):
    if entreprises[entreprise_id].employees == {}:
        print("Aucun employé dans cette entreprise")
        return
    for employee in entreprises[entreprise_id].employees:
        print(employee, ':')
        print('\tname : ', entreprises[entreprise_id].employees[employee].name)
        print('\tbirthday : ', entreprises[entreprise_id].employees[employee].birtday)
        print('\tentry_date : ', entreprises[entreprise_id].employees[employee].entry_date)
        print('\tend_date : ', entreprises[entreprise_id].employees[employee].end_date)
        print('\tpart_time :')
        for part_time in entreprises[entreprise_id].employees[employee].part_time:
            print('\t\tstart_date : ', part_time.start_date)
            print('\t\tend_date : ', part_time.end_date)
            print('\t\tcoefficient :', part_time.coefficient)
            print('\t\t', '-' * 20)

def main():
    parse_file("Test.txt")
    print_entreprise_info(1)

if __name__ == "__main__":
    main()