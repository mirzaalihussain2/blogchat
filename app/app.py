from flask import Flask, jsonify, request
from models import db, Character, Blog

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Routes
@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask App!")

@app.route('/characters', methods=['GET'])
def get_users():
    users = Character.query.all()
    return [user.name for user in users].__str__()

@app.route('/characters', methods=['POST'])
def add_user():
    data = request.json
    new_user = Character(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    return new_user.__str__(), 201

if __name__ == '__main__':
    app.run(debug=True)
