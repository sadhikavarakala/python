import heapq

# using list of salaries

salaries = [3000, 4000, 5000, 7000, 34000, 56000, 8000]

top_3_salaries = heapq.nlargest(3, salaries)

print("Top 3 salaries:", top_3_salaries)

# using dictionary of employee names and salaries

employee = [
    {'name': 'Alice', 'salary': 3000},
    {'name': 'Bob', 'salary': 4000},
    {'name': 'Charlie', 'salary': 5000},
    {'name': 'David', 'salary': 7000},
    {'name': 'Eve', 'salary': 34000},
    {'name': 'Frank', 'salary': 56000},
    {'name': 'Grace', 'salary': 8000}
]

top_employees = heapq.nlargest(3, employee, key=lambda x: x['salary'])

print("Top 3 employees by salary:")
for emp in top_employees:
    print(f"{emp['name']} - ${emp['salary']}")