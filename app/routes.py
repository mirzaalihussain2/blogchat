from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/characters', methods=['GET'])
def get_characters():
    return {"characters": ["Paul Graham", "Naval Ravikant"]}