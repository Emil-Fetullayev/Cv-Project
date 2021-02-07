from app import app
from flask import render_template,redirect,request,url_for
from . forms import ContactForm
from app.models import Post
from app import db
from admin import routes
from app.models import Cv1
from app.models import Cv2 
from app.models import Faydali1
from app.models import Faydali2
from app.models import Faydali3



@app.route('/')
def index():
    allPosts=Post.query.all()
    return render_template('index.html',content=allPosts)



@app.route('/delete/<int:id>')
def delete(id):
    user=Post.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/all')

@app.route('/delete2/<int:id>')
def delete2(id):
    user=Cv1.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/cvall')

@app.route('/delete3/<int:id>')
def delete3(id):
    user=Cv2.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/cvalltwo')

@app.route('/delete4/<int:id>')
def delete4(id):
    user=Faydali1.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/allfaydali')

@app.route('/delete6/<int:id>')
def delete6(id):
    user=Faydali2.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/allfaydali2')

@app.route('/delete7/<int:id>')
def delete7(id):
    user=Faydali3.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/allfaydali4')

@app.route('/update/<int:id>',methods=['GET','POST'])
def edit(id):
    user=Post.query.get(id)
    if request.method=='POST':
        
        newname=request.form['title']
        user.title=newname
        newname1=request.form['title2']
        user.title2=newname1
        newname2=request.form['content']
        user.content=newname2
        db.session.merge(user)
        db.session.flush()
        db.session.commit()
        return redirect('/')
    return render_template('admin/update.html',single=user)

@app.route('/basqa/<int:id>',methods=['GET','POST'])
def edit2(id):
    user2=Cv1.query.get(id)
    if request.method=='POST':
        
        cvkod=request.form['kod']
        user2.kod=cvkod
        cvaz=request.form['azSalary']
        user2.azSalary=cvaz
        cven=request.form['enSalary']
        user2.enSalary=cven
        db.session.merge(user2)
        db.session.flush()
        db.session.commit()
        return redirect('/')
    return render_template('admin/cvUpdate.html',single2=user2)

@app.route('/yeni/<int:id>',methods=['GET','POST'])
def edit3(id):
    user3=Cv2.query.get(id)
    if request.method=='POST':
        
        cvkod2=request.form['kod']
        user3.kod=cvkod2
        cvaz2=request.form['azSalary']
        user3.azSalary=cvaz2
        cven2=request.form['enSalary']
        user3.enSalary=cven2
        db.session.merge(user3)
        db.session.flush()
        db.session.commit()
        return redirect('/')
    return render_template('admin/cvUpdatetwo.html',single3=user3)


@app.route('/faydaliupdate/<int:id>',methods=['GET','POST'])
def edit5(id):
    user5=Faydali1.query.get(id)
    if request.method=='POST':
        
        faydali2=request.form['title']
        user5.title=faydali2
        faydali3=request.form['description']
        user5.description=faydali3
        db.session.merge(user5)
        db.session.flush()
        db.session.commit()
        return redirect('/')
    return render_template('admin/fayUpdate.html',single5=user5)

@app.route('/faydaupdate/<int:id>',methods=['GET','POST'])
def edit6(id):
    user6=Faydali2.query.get(id)
    if request.method=='POST':
        
        faydali5=request.form['title2']
        user6.title2=faydali5
        faydali6=request.form['description2']
        user6.description2=faydali6
        db.session.merge(user6)
        db.session.flush()
        db.session.commit()
        return redirect('/')
    return render_template('admin/faydaUpda.html',single6=user6)




@app.route('/cv')
def cv1():
    allPosts=Cv1.query.all()
    return render_template('cv.html',content=allPosts)

@app.route('/sing/<int:id>',methods=['GET','POST'])
def singPost(id):
    singPost=Cv1.query.get(id)
    return render_template('sales.html',post=singPost)

@app.route('/singtwo/<int:id>',methods=['GET','POST'])
def singlePost2(id):
    singlePost2=Cv2.query.get(id)
    return render_template('sales2.html',post=singlePost2)

@app.route('/cvtwo')
def cv2():
    allPosts=Cv2.query.all()
    return render_template('cv2.html',content=allPosts)
    
@app.route('/faydali')
def Faydali():
    faydalipost=Faydali1.query.all()
    faydalipost2=Faydali2.query.all()
    faydalipost3=Faydali3.query.all()
    return render_template('movzu1.html',content=faydalipost,con=faydalipost2,cone=faydalipost3)





@app.route('/fayda')
def Faydali6():
   
    return render_template('movzu2.html')


@app.route('/haqqimizda')
def haqqinda():
 
    return render_template('haqqimizda.html')

@app.route('/about')
def about():
    form=ContactForm()
    return render_template('about.html',form=form)

