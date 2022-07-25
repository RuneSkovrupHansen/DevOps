from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

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


parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("level", type=int)

"""For a given resource it seems common to have two endpoints,
one with and index, and one without, example:

/resource/index
/resource

The endpoint with the index supports the methods GET, PUT 
and DELETE which all use the index. The endpoint can
support several methods, but if it makes sense include them
all which supports getting one or more. The flask_restful
refers to this endpoint as ResourceList.
"""


class Character(Resource):

    def get(self, index):
        check_index(index)
        return characters_indexed[index]

    def delete(self, index):
        check_index(index)
        del characters_indexed[index]
        return '', 204

    def put(self, index):
        """curl command to call endpoint:
        curl -X PUT http://127.0.0.1:5000/characters/0 -H 'Content-Type: application/json' -d '{"name":"rune", "level":100}'
        """

        args = parser.parse_args()
        name = args['name']
        level = args['level']

        ret, char = character.Character(name, level).export_to_json()

        if not ret:
            abort(400, message="Invalid character data")

        characters_indexed[index] = char
        return characters_indexed[index], 201


api.add_resource(Character, "/characters/<index>")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()

print(characters_indexed)

quit()
