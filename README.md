# Code Challenge Clement

## Overview

This repository contains the solutions to two coding tasks which are the clement coding challenge. The tasks involve parsing and modifying JSON data and interacting with a REST API to retrieve customer addresses and store them in a CSV file.

## Task 1: Parsing and Updating JSON Data

### Objective

The goal of this task was to parse a JSON object containing a list of internet hubs, reorder the hubs based on specific criteria, assign new serial numbers, and update the JSON object with these new values.

### Implementation Details

- **Function**: `handle_parsing_json`
  - **Parameters**: 
    - `data` (dict): The JSON object containing the list of internet hubs.
  - **Returns**: 
    - `updated_data` (dict): The modified JSON object with updated internet hubs.

### Steps:
1. **Retrieve Internet Hubs**: The function extracts the list of internet hubs from the provided JSON data.
2. **Clean the Data**: It removes the first and last hubs, focusing only on those that need serial numbers updated (i.e., `mn1` to `mn8`).
3. **Sort the Hubs**: The hubs are sorted in descending order based on the last digit of their ID.
4. **Assign New Serial Numbers**: New serial numbers are generated and assigned to the hubs.
5. **Update the JSON Object**: The original JSON object is updated with the newly sorted and serialized internet hubs.

### Code Example:
```python
def handle_parsing_json(data: dict):
    internet_hubs = data.get('Internet_hubs', [])
    cleaned_internet_hubs = internet_hubs[1:9]
    serial_numbers = [f'C25CTW0000000000147{n}' for n in range(1, len(cleaned_internet_hubs) + 1)]
    reversed_cleaned_internet_hubs = sorted(cleaned_internet_hubs, key=lambda x: int(x['id'][-1]), reverse=True)
    
    for internet_hub, serial_number in zip(reversed_cleaned_internet_hubs, serial_numbers):
        internet_hub['serial_number'] = serial_number

    updated_data = data.copy()
    updated_data['Internet_hubs'] = reversed_cleaned_internet_hubs

    return updated_data
```

### Example Usage:
```python
data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
        {"id": "men1", "serial_number": "C25CTW00000000001470"},
        {"id": "mn1", "serial_number": "<serial number here>"},
        # ... other hubs
        {"id": "mn9", "serial_number": "<serial number here>"}
    ]
}

edited_data = handle_parsing_json(data)
print(edited_data)
```

---

## Task 2: Retrieving and Storing Customer Addresses

### Objective

The objective of this task was to retrieve customer addresses from an API and store them in a CSV file. The file name is provided by the user, and the program should handle errors gracefully, such as invalid file names.

### Implementation Details

- **Function**: `get_address_by_customer_id`
  - **Parameters**: 
    - `customer_number` (int): The ID of the customer whose address is to be retrieved.
  - **Returns**: 
    - `address` (str): The formatted address of the customer, or an empty string if the address could not be retrieved.
  
### Steps:
1. **Retrieve Customer Numbers**: Make a request to retrieve the total number of customers.
2. **Fetch Addresses**: For each customer, make an API call to retrieve their address.
3. **Save to CSV**: Write the retrieved addresses to a CSV file, handling user input for file naming and ensuring valid file names.

### Code Example:
```python
import requests, csv, os
import pathlib

base_dir = pathlib.Path(__file__).parent

def get_address_by_customer_id(customer_number: int):
    try:
        response = requests.get(
            f'https://clemant_demo.com/address_inventory/{customer_number}', 
            headers={'X-API-KEY': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'}
        )
        data = response.json()
        if data:
            street = data.get('street', '').strip()
            postcode = data.get('postcode', '').strip()
            state = data.get('state', '').strip()
            country = data.get('country', '').strip()
            address = f'{street}, {postcode}, {state}, {country}'
            return address
        else:
            return ''
    except:
        return ''

total_customer_response = requests.get(
    'https://clemant_demo.com/customer_numbers', 
    headers={'X-API-KEY': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'}
)
total_customer = int(total_customer_response.text)

input_name = input("Enter the filename to save the CSV (default: 'customer_addresses.csv'): ").strip()

if input_name.count('.') > 1:
    print(f"Invalid filename {input_name}")
    exit()

if not input_name.endswith('.csv'):
    input_name = input_name.split('.')[0] + '.csv'
  
file_name = input_name or 'customer_addresses.csv'
saved_path = os.path.join(base_dir, file_name)

with open(saved_path, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['addresses'])
  
    for customer_id in range(1, total_customer + 1):
        customer_address = get_address_by_customer_id(customer_id)
        csv_writer.writerow([customer_address])
    
print(f"Customer addresses have been stored in '{file_name}' at {saved_path}")
```

### Example Usage:
- When the script is run, it prompts the user for a file name.
- After providing a valid file name, the script retrieves the customer addresses and stores them in the specified CSV file.

---

## Requirements

To run the code provided in this repository, you need:

- Python 3.x
- `requests` library (install via `pip install requests`)

## Running the Tasks

1. **Task 1**: Simply call the `handle_parsing_json` function with the provided JSON data.
2. **Task 2**: Run the script, provide a valid filename when prompted, and the script will generate the CSV file with customer addresses.

