from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from pipeline.buffer_file import get_text
from scripts.get_job_description import get_job_description
import spacy
from pipeline.ept2 import get_everything
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Entity Comparison API', description='API for comparing entities')
ns = api.namespace('compare', description='Entity Comparison Operations')

# Load the spaCy model (consider using an absolute path)
nlp = spacy.load("D:\\InterviewBot\\models\\model-last")

# Create a request parser
parser = reqparse.RequestParser()
parser.add_argument('video', location='files', type=FileStorage, required=True)
parser.add_argument('job_description', location='files', type=FileStorage, required=True)

@ns.route('/compare-entities')
class CompareEntities(Resource):
    @api.expect(parser)
    def post(self):
        try:
            args = parser.parse_args()
            video_file = args['video']
            job_desc_file = args['job_description']

            # Your existing code for handling the POST request goes here
            responses = get_everything(video_file, job_desc_file)
            return responses,200
        except Exception as e:
            return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
