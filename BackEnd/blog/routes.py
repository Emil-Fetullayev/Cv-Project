from flask import Blueprint


blog=Blueprint('blog',__name__,url_prefix='/blog')




@blog.route('/')
def blogIndex():
    return 'This is blog page'

@blog.route('/single')
def blogSingle():
    return 'This is single blog page'
