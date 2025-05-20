import pandas as pd
from models import Person, Student, Worker
from enums import MenuOption


total_age = 0
record_count = 0

def format_option(name: str) -> str:
    name = name.replace("_", " ").title()
    name = name.replace("Id", "ID").replace("Csv", "CSV")
    return name

def display_menu() -> MenuOption:
    for option in MenuOption:
        print(f"{option.value}. {format_option(option.name)}")
    try:
        choice = int(input("Please enter your choice: "))
        return MenuOption(choice)
    except (ValueError, KeyError):
        raise ValueError("Invalid menu choice.")


def save_new_entry(records: dict, record_ids: list):
    id_number = input("ID: ")
    if id_number in records:
        print("Error: ID already exists.")
        return

    name = input("Name: ")
    age_input = input("Age: ")
    if not age_input.isdigit():
        print("Age must be a number.")
        return
    age = int(age_input)

    print("Choose type: 1 - Person, 2 - Student, 3 - Worker")
    type_choice = input("Choice: ")

    person_obj = None

    if type_choice == "1":
        person_obj = Person(name, age)
    elif type_choice == "2":
        field_of_study = input("Field of Study: ")
        year_input = input("Year of Study: ")
        if not year_input.isdigit():
            print("Year of study must be a number.")
            return
        year_of_study = int(year_input)
        score_input = input("Score Average: ")
        try:
            score_avg = float(score_input)
        except ValueError:
            print("Score average must be a number.")
            return
        person_obj = Student(name, age, field_of_study, year_of_study, score_avg)
    elif type_choice == "3":
        field_of_work = input("Field of Work: ")
        salary_input = input("Salary: ")
        if not salary_input.isdigit():
            print("Salary must be a number.")
            return
        salary = int(salary_input)
        person_obj = Worker(name, age, field_of_work, salary)
    else:
        print("Invalid type choice.")
        return

    records[id_number] = person_obj
    record_ids.append(id_number)
    global total_age, record_count
    total_age += person_obj.age
    record_count += 1
    print("Entry saved successfully.")



def search_by_id(records: dict):
    id_number = input("Enter ID to search: ")
    if id_number in records:
        print(records[id_number].display())
    else:
        print("ID not found.")

def print_average_age():
    global total_age, record_count
    if record_count == 0:
        print(0)
    else:
        avg = total_age / record_count
        print(f"Average age: {avg:.2f}")


def print_all_names(records: dict):
    for person in records.values():
        print(person.name)

def print_all_ids(records: dict):
    for id_number in records.keys():
        print(id_number)

def print_all_entries(records: dict):
    for person in records.values():
        print(person.display())
        print("---")

def print_by_index(records: dict, record_ids: list):
    index_input = input("Enter index: ")
    if not index_input.isdigit():
        print("Index must be a number.")
        return

    index = int(index_input)
    if 0 <= index < len(record_ids):
        id_number = record_ids[index]
        print(records[id_number].display())
    else:
        print("Index out of range.")

def save_to_csv(records: dict):
    df = pd.DataFrame([person.to_dict() for person in records.values()])
    df.to_csv("output.csv", index=False)
    print("CSV saved successfully.")

def main():
    records = {}
    record_ids = []
    try:
        while True:
            try:
                option = display_menu()
            except ValueError as ve:
                print(ve)
                input("Press enter to continue")
                continue

            if option == MenuOption.SAVE_ENTRY:
                save_new_entry(records, record_ids)
            elif option == MenuOption.SEARCH_BY_ID:
                search_by_id(records)
            elif option == MenuOption.PRINT_AVERAGE_AGE:
                print_average_age()
            elif option == MenuOption.PRINT_ALL_NAMES:
                print_all_names(records)
            elif option == MenuOption.PRINT_ALL_IDS:
                print_all_ids(records)
            elif option == MenuOption.PRINT_ALL_ENTRIES:
                print_all_entries(records)
            elif option == MenuOption.PRINT_BY_INDEX:
                print_by_index(records, record_ids)
            elif option == MenuOption.SAVE_TO_CSV:
                save_to_csv(records)
            elif option == MenuOption.EXIT:
                print("Goodbye!")
                break
            input("Press enter to continue")

    except KeyboardInterrupt:
        print("\nProgram exited by user (Ctrl+C). Goodbye!")

if __name__ == "__main__":
    main()