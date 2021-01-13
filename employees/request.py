EMPLOYEES = [
    {
        "id": 1,
        "name": "Alex Krycek",
        "animalId": 2,
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Fox Mulder",
        "animalId": 1,
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Dana Scully",
        "animalId": 1,
        "locationId": 1
    },
    {
        "name": "Frohike",
        "locationId": 1,
        "animalId": 6,
        "id": 4
    },
    {
        "name": "Walter Skinner",
        "locationId": 2,
        "animalId": 9,
        "id": 5
    }
]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in Javascript.
    for employee in EMPLOYEES:
        # Dictionaries in Pythod user [] notation to find a key
        # instead of the dot notation that Javascript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEE list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)