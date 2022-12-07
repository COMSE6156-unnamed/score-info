import requests
from flask import Blueprint, request, Response, render_template, url_for
from utils.exts import db
from utils.model import Question, QuizQuestion, Quiz, UserAnswer
import json

bp = Blueprint("score", __name__, url_prefix="/score")


@bp.route("/", methods=["GET"])
def all_score():
  args = request.args
  recent_entry_num = args.get('recent_entry_num')
  resp = {}

  
  return Response(json.dumps(resp), status=200)