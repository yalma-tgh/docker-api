from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-users/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Yalma",
        "email": "yalma@gmail.com"
    }

    name = request.args.get("name")
    if name:
        user_data["name"] = name
        user_data["email"] = f"{str.lower(name)}@gmail.com"

    return jsonify(user_data),200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    return jsonify(data),201

 
if __name__ == "__main__":
    app.run(debug=True) 