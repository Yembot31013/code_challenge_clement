import json

def handle_parsing_json(data: dict):
  internet_hubs = data.get('Internet_hubs', [])

  cleaned_internet_hubs = internet_hubs[1:9]
  
  serial_numbers = [f'C25CTW0000000000147{n}' for n in range(1, 9)]
  
  print([x['id'][-1] for x in cleaned_internet_hubs])
  reversed_cleaned_internet_hubs = sorted(cleaned_internet_hubs, key=lambda x: int(x['id'][-1]), reverse=True)
  
  new_internet_hub = []
  for internet_hub, serial_number in zip(reversed_cleaned_internet_hubs, serial_numbers):
    internet_hub['serial_number'] = serial_number
    new_internet_hub.append(internet_hub)
  
  updated_data = data.copy()
  
  updated_data['Internet_hubs'] = new_internet_hub
  
  return updated_data, data



data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
        {
            "id": "men1",
            "serial_number": "C25CTW00000000001470"
        },
        {
            "id": "mn1",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn2",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn3",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn4",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn5",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn6",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn7",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn8",
            "serial_number": "<serial number here>"
        },
        {
            "id": "mn9",
            "serial_number": "<serial number here>"
        }
    ]
}


edited_data, original_data = handle_parsing_json(data)
print("========================")
print(edited_data)
print("========================")
print(original_data)
