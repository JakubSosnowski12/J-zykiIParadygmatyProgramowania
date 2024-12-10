class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Imię: {self.name}, Nazwisko: {self.age}, Pensja: {self.salary}"

class EmployeesManager:
    def __init__(self):
        self.employees = []  # Lista przechowująca pracowników

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        if not self.employees:
            print("Brak pracowników.")
        for emp in self.employees:
            print(emp)

    def remove_employees_by_age(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    def search_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                print(emp)
                return
        print("Nie ma takiego pracownika.")

    def update_salary(self, name, new_salary):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                emp.salary = new_salary
                print(f"Pensja {emp.name} została zaktualizowana.")
                return
        print("Pracownik nie istnieje.")

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def start(self):
        while True:
            print("\nMenu:")
            print("1. Dodaj nowego pracownika")
            print("2. Wyświetl wszystkich pracowników")
            print("3. Usuń pracowników w określonym przedziale wiekowym")
            print("4. Wyszukaj pracownika")
            print("5. Zaktualizuj wynagrodzenie pracownika")
            print("6. Zakończ")

            choice = input("Wybierz opcję 1-6: ")

            if choice == "1":
                name = input("Imię i nazwisko: ")
                age = int(input("Wiek: "))
                salary = float(input("Pensja: "))
                employee = Employee(name, age, salary)
                self.manager.add_employee(employee)
            elif choice == "2":
                self.manager.display_all_employees()
            elif choice == "3":
                min_age = int(input("Minimalny wiek: "))
                max_age = int(input("Maksymalny wiek: "))
                self.manager.remove_employees_by_age(min_age, max_age)
            elif choice == "4":
                name = input("Imię i nazwisko: ")
                self.manager.search_employee(name)
            elif choice == "5":
                name = input("Imię i nazwisko: ")
                new_salary = float(input("Nowe wynagrodzenie: "))
                self.manager.update_salary(name, new_salary)
            elif choice == "6":
                print("Zakończono.")
                break
            else:
                print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.start()