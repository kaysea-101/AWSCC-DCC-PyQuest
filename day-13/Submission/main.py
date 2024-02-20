from flask import Flask, jsonify
import csv

app = Flask(__name__)

# route for get request
@app.route('/', methods=['GET'])
def get_csv_data():
    csv_file_path = 'programming_languages.csv'  

    # open csv
    with open(csv_file_path, 'r') as file:
        # read csv file using DictReader
        reader = csv.DictReader(file)
        # convert to list
        data = list(reader)

    # return the data in JSON format
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
