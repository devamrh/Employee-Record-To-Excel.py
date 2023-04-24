import pandas as pd

employee_data = pd.read_excel('emprec.xlsx') # emprec.xlsx is the excel file

def add_emp():
    global employee_data 
    if len(employee_data)>=15:
        print('Employee record limit reached')
        return
    name = input('Enter employee name :')
    department = input('Enter employee department: ')
    department_no = input('Enter employee department no: ')
    salary = input('Enter employee salary: ')
    
    new_employee = pd.DataFrame(
        {
            'Name': [name],
            'Department': [department],
            'Department No.': [department_no],
            'Salary': [salary]
        }
    )
    
    employee_data = pd.concat([employee_data, new_employee], ignore_index=True)
    employee_data.to_excel('emprec.xlsx',index=False) # index=False means there's should be no index written 
    print('Employee record added successfully') 
    

def display_emp():
    print(employee_data)
    
    
while True:
    choice = input('Enter 1 to add new employee or 2 to display all employee\n')
    if choice== '1':
        add_emp()
    elif choice=='2':
        display_emp()
        break
    else:
        print('Invalid choice. Please try again')
