from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class LinePredictor(Resource):
    def get(self):
        if request.args.get("description") is None:
            return "Invalid request. Please use GET with \"description\" query parameter."

        try:
            return prediction.predict_lines(request.args.get("description"))
        except Exception as e:
            return "Unknown error occurred. Please try again later."

api.add_resource(LinePredictor, '/predict')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
