import requests
import csv
import os
import pathlib

base_dir = pathlib.Path(__file__).parent


def get_address_by_customer_id(customer_number: int):
    try:
        response = requests.get(
            f'https://clemant_demo.com/address_inventory/{customer_number}',
            headers={'X-API-KEY': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'}
        )
        response.raise_for_status()
        data = response.json()
        if data:
            street = data.get('street', '').strip()
            postcode = data.get('postcode', '').strip()
            state = data.get('state', '').strip()
            country = data.get('country', '').strip()
            address = f'{street}, {postcode}, {state}, {country}'
            return address
        return ''
    except requests.exceptions.RequestException as e:
        print(f"Error fetching address for customer {customer_number}: {e}")
        return ''


# Get total customer numbers
total_customer_response = requests.get(
    'https://clemant_demo.com/customer_numbers',
    headers={'X-API-KEY': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'}
)
total_customer = int(total_customer_response.text)

# Get the file name input
input_name = input(
    "Enter the filename to save the CSV (default: 'customer_addresses.csv'): ").strip()

if input_name.count('.') > 1:
    print(f"Invalid filename '{input_name}'")
    exit()

if not input_name.endswith('.csv'):
    input_name = input_name.split('.')[0] + '.csv'

file_name = input_name if input_name else 'customer_addresses.csv'
saved_path = os.path.join(base_dir, file_name)

# Write customer addresses to CSV
with open(saved_path, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['address'])

    for customer_id in range(1, total_customer + 1):
        customer_address = get_address_by_customer_id(customer_id)
        csv_writer.writerow([customer_address])

print(f"Customer addresses have been stored in '{file_name}' at {saved_path}")
