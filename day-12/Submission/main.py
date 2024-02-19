from flask import Flask, jsonify  

app = Flask(__name__)

data = {
    "name": "Your Name",
    "course_and_section": "Your course and section",
    "favorite_programming language": "Your programming language",
    "aws_service": "Give one AWS service you know"
}

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)