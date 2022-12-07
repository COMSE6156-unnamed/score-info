import requests
from flask import Blueprint, request, Response, render_template, url_for
from utils.exts import db
from utils.model import UserQuiz
import json

bp = Blueprint("score", __name__, url_prefix="/score")


@bp.route("/", methods=["GET"])
def all_score():
  args = request.args
  recent_entry_num = args.get('recent_entry_num', None)
  resp = {"users":[]}
  
  query = db.session.query(UserQuiz) \
    .order_by(UserQuiz.created_at.desc()) \
  
  if recent_entry_num:
    query = query.limit(int(recent_entry_num))

  query = query.order_by(UserQuiz.score.desc())

  for user_quiz in query:
    resp["users"].append({
      "user_id": user_quiz.user_id,
      "quiz_id": user_quiz.quiz_id,
      "score": user_quiz.score,
      "quiz_taken_at": str(user_quiz.created_at),
    })

  return Response(json.dumps(resp), status=200)