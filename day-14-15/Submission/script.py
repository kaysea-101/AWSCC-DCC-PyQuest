import requests

base_url = 'http://127.0.0.1:5000'

# Hello route
response = requests.get(base_url)
print(response.json())

# Get All Services route
response = requests.get(f'{base_url}/aws_services/get_all')
print(response.json())

# Add Service route
new_service_data = {"service": "Elastic Compute Cloud (EC2)"}
response = requests.post(f'{base_url}/aws_services/add_service', json=new_service_data)
print(response.json())

# Get Service by ID route
service_id = 1  # Assuming service ID 1 exists
response = requests.get(f'{base_url}/aws_services/{service_id}')
print(response.json())

# Update Service by ID route
updated_service_data = {"service": "Updated Service Name"}
response = requests.put(f'{base_url}/aws_services/update_service/{service_id}', json=updated_service_data)
print(response.json())

# Delete Service by ID route
response = requests.delete(f'{base_url}/aws_services/delete_service/{service_id}')
print(response.json())
