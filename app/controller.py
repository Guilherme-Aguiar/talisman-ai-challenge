import os, json
from flask_restful import Resource
from app.utils import gpt_helpers, processing, file_check
from app.prompt_text import initial_petition_text
from flask import request, jsonify
from tika import parser
from app.errors import errors

class ParsePDFAndRunPrompt(Resource):
  def post(self):
    file = request.files['file']

    path_to_pdf = f"temp/{file.filename}"
    file.save(path_to_pdf)

    if(not file_check.is_pdf(path_to_pdf)):
      return errors['FileIsNotPDF'], 415
      
    parsed_pdf = parser.from_file(path_to_pdf)
    os.remove(path_to_pdf)
    text_content = parsed_pdf['content']
    transformed_text_content = processing.transform_text(text_content, blacklist=["Assinado eletronicamente", "Praça Olegário Ferreira"])
    transformed_text_content = transformed_text_content + " " + initial_petition_text

    response = gpt_helpers.generate_openai_response(transformed_text_content)
    
    return jsonify({'answer': response})