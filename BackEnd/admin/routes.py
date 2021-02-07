from flask import Blueprint,render_template,redirect,request,url_for
from app.models import Post
from app import db
import os
from app import app
from app.models import Cv1
from app.models import Cv2
from app.models import Faydali1
from app.models import Faydali2
from app.models import Faydali3




admin=Blueprint(
    'admin',
     __name__,
     url_prefix='/admin',
     template_folder='templates',
     static_folder='static')

@admin.route('/')
def adminIndex():
    return render_template('admin/index.html')

@admin.route('/add',methods=['GET','POST'])
def adminAdd():
    if request.method=='POST':
        f = request.files['newsPhoto']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
      
        post=Post(title=request.form['newsHeading'],title2=request.form['newsHeading1'],content=request.form['newsContent'],img=f.filename)
        
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/all')
    return render_template('admin/addPost.html')

@admin.route('/all')
def adminAll():
    allPosts=Post.query.all()
    return render_template('admin/allPosts.html',content=allPosts)


@admin.route('/cvadd',methods=['GET','POST'])
def adminCv():
    if request.method=='POST':
        f = request.files['cvPhoto']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        
        cv=Cv1(kod=request.form['cvKod'],azSalary=request.form['cvAz'],enSalary=request.form['cvEn'],img=f.filename)
        db.session.add(cv)
        db.session.commit()
        return redirect('/admin/cvall')
    return render_template('admin/addCv.html')


@admin.route('/cvall')
def adminCv1():
    allCv=Cv1.query.all()
    return render_template('admin/allCv.html',conten=allCv)

@admin.route('/cvaddtwo',methods=['GET','POST'])
def adminCv2():
    if request.method=='POST':
        f = request.files['cvPhoto2']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        
        cv=Cv2(kod=request.form['cvKod2'],azSalary=request.form['cvAz2'],enSalary=request.form['cvEn2'],img=f.filename)
        db.session.add(cv)
        db.session.commit()
        return redirect('/admin/cvalltwo')
    return render_template('admin/addCv2.html')

@admin.route('/cvalltwo')
def adminCv3():
    allCv2=Cv2.query.all()
    return render_template('admin/allCv2.html',conten=allCv2)


@admin.route('/addfaydali',methods=['GET','POST'])
def adminFaydali1():
    if request.method=='POST':
        f = request.files['faydaliPhoto']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        
        faydali=Faydali1(title=request.form['title'],description=request.form['description'],img=f.filename)
        db.session.add(faydali)
        db.session.commit()
        return redirect('/admin/allfaydali')
    return render_template('admin/addFaydali.html')

@admin.route('/allfaydali')
def adminFaydali2():
    fayda=Faydali1.query.all()
    return render_template('admin/allFaydali.html',conten=fayda)


@admin.route('/addfaydali2',methods=['GET','POST'])
def adminFaydali3():
    if request.method=='POST':
        f = request.files['Photo2']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        
        faydali2=Faydali2(title2=request.form['title2'],description2=request.form['description2'],img=f.filename)
        db.session.add(faydali2)
        db.session.commit()
        return redirect('/admin/allfaydali2')
    return render_template('admin/addFaydali2.html')


@admin.route('/allfaydali2')
def adminFaydali4():
    fayda2=Faydali2.query.all()
    return render_template('admin/allFaydali2.html',content=fayda2)


@admin.route('/addfaydali3',methods=['GET','POST'])
def adminFaydali5():
    if request.method=='POST':
        f = request.files['Photo3']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        
        faydali3=Faydali3(title3=request.form['title3'],description3=request.form['description3'],img=f.filename)
        db.session.add(faydali3)
        db.session.commit()
        return redirect('/admin/allfaydali4')
    return render_template('admin/addFaydali3.html')


@admin.route('/allfaydali4')
def adminFaydali6():
    fayda3=Faydali3.query.all()
    return render_template('admin/allFaydali3.html',content=fayda3)



# @admin.route('/single')
# def adminSingle():
#     return render_template('addPost.html')