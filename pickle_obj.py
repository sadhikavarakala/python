import pickle
import os

# python obj to serialze

employee_data = {
    'id': 101,
    'name': 'John Doe',
    'department': 'Finance',
    'salary': 75000,
    'skills': ['Excel', 'Financial Analysis', 'Budgeting']
}

#serialize with pickle

output_path = "/Users/sadhikavarakala/Practice/employee_data.pickle"

with open(output_path, 'wb') as file:
    pickle.dump(employee_data, file)
    print(f"Employee data serialized and saved to {output_path}")

#Deserialize with pickle

with open(output_path, 'rb') as file:
    loaded_data = pickle.load(file)
    print("Deserialized employee data:")
    print(loaded_data)