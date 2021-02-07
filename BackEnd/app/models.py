from app import db

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    title2=db.Column(db.String)
    content=db.Column(db.String)
    img=db.Column(db.Integer)

class Cv1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    kod=db.Column(db.String)
    azSalary=db.Column(db.String)
    enSalary=db.Column(db.String)
    img=db.Column(db.Integer)

class Cv2(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    kod=db.Column(db.String)
    azSalary=db.Column(db.String)
    enSalary=db.Column(db.String)
    img=db.Column(db.Integer)

class Faydali1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Integer)
    title=db.Column(db.String)
    description=db.Column(db.String)

class Faydali2(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Integer)
    title2=db.Column(db.String)
    description2=db.Column(db.String)

class Faydali3(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Integer)
    title3=db.Column(db.String)
    description3=db.Column(db.String)

class Haqqimizda(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String)