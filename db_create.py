from app import db
from models import BlogPost


#only run drop_all() in test, when adding a new column, this will delete previous date.
#db.drop_all()

#create database and db tables
db.create_all()

# insert
db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("Well","I\'m well."))
db.session.add(BlogPost("postgres","we setup a local postgres instance"))

# commit the changes
db.session.commit()
