import requests
from flask import Blueprint, request, Response, render_template, url_for
from utils.exts import db
from utils.model import UserQuiz
from sqlalchemy import func
import json

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<int:user_id>/quiz/avg_score", methods=["GET"])
def user_quiz_average_score(user_id: int):
  resp = {"quiz_ids": [], "avg_scores": []}
  for entry in db.session.query(UserQuiz.quiz_id, func.avg(UserQuiz.score).label("avg_score")) \
        .filter(UserQuiz.user_id == user_id) \
        .group_by(UserQuiz.quiz_id).order_by(UserQuiz.quiz_id):
      resp["quiz_ids"].append(entry.quiz_id)
      resp["avg_scores"].append(round(entry.avg_score, 2))
  return Response(json.dumps(resp), status=200)