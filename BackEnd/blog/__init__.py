from app import app,db


from blog.routes import blog


app.register_blueprint(blog)