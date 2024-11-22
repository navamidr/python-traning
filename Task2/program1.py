import pandas as pd 

data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob White', 'Charlie Green'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
    'Salary': [50000, 55000, 60000, 45000, 47000],
    'Joining_Date': ['2022-01-15', '2023-03-10', '2021-06-23', '2022-09-01', '2022-12-05']
}

# convert dataframe

output= pd.DataFrame(data)

print(output) 

# data cleaning

output["Joining_Date"] = pd.to_datetime(output['Joining_Date'])

print(output.to_string())

# replacing

output.fillna('None', inplace = True) 

print(output.to_string())

# excel file

file_name='employee_data.xlsx'
output.to_excel(file_name,index=False)
print(f"successfullly exported to {file_name}")

