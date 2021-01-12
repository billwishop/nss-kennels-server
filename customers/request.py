CUSTOMERS = [
    {
        "email": "will@aol.com",
        "password": "YES",
        "name": "Will Bishop",
        "id": 1
    },
    {
        "email": "reginal@aol.com",
        "password": "YES",
        "name": "Reginald Reggie",
        "id": 2
    },
    {
        "email": "tony@aol.com",
        "password": "YES",
        "name": "Tony Tanner",
        "id": 3
    },
    {
        "email": "tonya@aol.com",
        "password": "YES",
        "name": "Tonya Tanner",
        "id": 4
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in Javascript.
    for customer in CUSTOMERS:
        # Dictionaries in Pythos use [] notation to find a key
        # instead of the dot notation that Javascript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer