from flask import Flask, jsonify, request

app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    }
]

# base url
@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, welcome to the AWS Services API!"})

# /aws_services/get_all
@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify({"services": aws_services})

# /aws_services/<int:service_id>
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((item for item in aws_services if item["id"] == service_id), None)
    if service:
        return jsonify({"service": service})
    else:
        return jsonify({"error": "Service not found"}), 404

# /aws_services/add_service
@app.route('/aws_services/add_service', methods=['GET','POST'])
def add_service():
    if request.method == 'POST':
        new_service = {"id": len(aws_services) + 1, "service": request.json.get("service")}
        aws_services.append(new_service)
        return jsonify({"message": "Service added successfully", "service": new_service}), 201

    else:
        return jsonify({"message": "Use POST request to add a new service"}), 405
    
# /aws_services/delete_service/<int:service_id>
@app.route('/aws_services/delete_service/<int:service_id>', methods=['GET', 'DELETE'])
def delete_service(service_id):
    global aws_services
    if request.method == 'DELETE':
        aws_services = [item for item in aws_services if item["id"] != service_id]
        return jsonify({"message": f"Service with ID {service_id} deleted successfully"})
    else:
        return jsonify({"error": "Method not allowed"}), 405


# /aws_services/update_service/<int:service_id>
@app.route('/aws_services/update_service/<int:service_id>', methods=['GET', 'PUT'])
def update_service(service_id):
    global aws_services
    service = next((item for item in aws_services if item["id"] == service_id), None)
    if service:
        if request.method == 'PUT':
            service["service"] = request.json.get("service", service["service"])
            return jsonify({"message": f"Service with ID {service_id} updated successfully", "service": service})
        else:
            return jsonify({"error": "Method not allowed"}), 405
    else:
        return jsonify({"error": "Service not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
