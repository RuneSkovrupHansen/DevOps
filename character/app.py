import json
from flask import Flask, request
from flask_restful import Resource, Api, abort

import character

# Documentation on flask_restful
# https://flask-restful.readthedocs.io/en/latest/index.html

app = Flask(__name__)
api = Api(app)

# Starting data
characters = [
    character.Character("Ross", 30),
    character.Character("Richard", 40),
    character.Character("Peter", 50),
    character.Character("Conner", 60)
]

# Create indexed dictionary
characters_indexed = {}
for index, character_ in enumerate(characters):
    characters_indexed[str(index)] = character_.export_to_json()[1]


def check_index(index):
    """Abort if index does not exist.

    Aborts API request if index of object does not exist.

    Args:
        index (int): Index of object.

    Returns:
        None.
    """

    if index not in characters_indexed:
        abort(404, message="Index {} does not exist".format(index))


class Character(Resource):

    def get(self, index):
        check_index(index)
        return characters_indexed[index]

    def delete(self, index):
        check_index(index)
        del characters_indexed[index]
        return '', 204


api.add_resource(Character, "/characters/<index>")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()

print(characters_indexed)

quit()
