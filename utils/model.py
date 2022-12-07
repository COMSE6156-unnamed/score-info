from utils.exts import db
import datetime

class UserQuiz(db.Model):
  __tablename__ = "user_quiz"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer)
  quiz_id = db.Column(db.Integer)
  score = db.Column(db.Float)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)

  def __init__(self, user_id: int, quiz_id: int, score: float):
    self.user_id = user_id
    self.quiz_id = quiz_id
    self.score = score
