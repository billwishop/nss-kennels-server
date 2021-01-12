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
        "name": "Skinner",
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