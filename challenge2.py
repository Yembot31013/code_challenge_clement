import requests, csv, os
import pathlib

base_dir = pathlib.Path(__file__).parent

def get_address_by_customer_id(customer_number: int):
  try:
    response = requests.get(
        f'https://clemant_demo.com/address_inventory/{customer_number}', headers={'X-API-KEy': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'})
    
    data = response.json()
    if data:
      street = data.get('street', '')
      postcode = data.get('postcode', '')
      state = data.get('state', '')
      country = data.get('country', '')
      
      address = f'{street}, {postcode}, {state}, {country}'
      
      return address
    else:
      return ''
  except:
    return ''
    

total_customer_response = requests.get(
    'https://clemant_demo.com/customer_numbers', headers={'X-API-KEy': 'ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl'})

total_customer = int(total_customer_response.text)

input_name = input(
    "enter the filename to save the csv (default: 'customer_addresses.csv')")

if input_name.count('.') > 1:
  print(f"invalid filename {input_name}")
  exit()

input_name = input_name.strip() 
if not input_name.endswith('.csv'):
  input_name = input_name.split('.')[0]
  input_name = f'{input_name}.csv'
  
file_name = input_name

saved_path = os.path.join(base_dir, file_name)

with open('customer_addresses.csv', 'w') as f:
  csv_writer = csv.writer(f)
  csv_writer.writerow('addresses')
  
  for customer_id in range(1, total_customer+1):
    customer_address = get_address_by_customer_id(customer_id)
    csv_writer.writerow(customer_address)
    
print(f"customer addresses have been stored in '{file_name}' at {saved_path}")
