from app import db
import datetime
from datetime import date

class BlogPost(db.Model):

    __tablename__ = "posts"
    __table_args__ = {'extend_existing':True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    pub_date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)


    def __init__(self, title, description, pub_date=None):
        self.title = title
        if pub_date is None:
            pub_date = datetime.date.today()
        self.pub_date = pub_date
        self.description = description


    def __repr__(self):
        return '<{}>'.format(self.title)


