from flask import Blueprint
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask import request,redirect,jsonify
from flask.wrappers import Response

main = Blueprint('main',__name__)


@main.route('/')
def home():

    # fetch all user from the database
    from project import db
    cur = db.connection.cursor()
    exec_query = cur.execute("SELECT * FROM user")
    if exec_query >0:

        results = cur.fetchall()
        return render_template('index.html',results=results)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/form' ,methods=['GET','POST'])
def data():
    if request.method == 'POST':

        name = request.form['name']
        email= request.form['email']

        from project import db
        cur = db.connection.cursor()
        cur.execute("INSERT INTO user (name,email) VALUES(%s,%s)",(name,email))
        cur.connection.commit()
        cur.close()
        flash('User sucessfully inserted')
        return redirect(url_for('main.home'))

    return render_template('form.html')

@main.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    from project import db

    if request.method=='POST':

        name = request.form['name']
        email = request.form['email']
        data = (name,email)

        cur = db.connection.cursor()
        results = cur.execute("UPDATE user SET name=%s, email=%s WHERE user_id=%s",(name,email,id))
        if results:
            cur.connection.commit()
            cur.close()
            flash('User Data Successfully updated')
            return redirect(url_for('main.home'))

    cur = db.connection.cursor()
    cur.execute(f'SELECT * FROM user Where user_id={id}')
    results = cur.fetchone()
    
    return render_template('edit.html',results=results)

@main.route('/delete/<id>')
def delete(id):

    from project import db
    try:

        cur = db.connection.cursor()
        result = cur.execute("DELETE FROM user WHERE user_id=%s",(id))
        if result:
            cur.connection.commit()
            cur.close()
            flash('User has successfully been deleted')
            return redirect(url_for('main.home'))
    except ProgrammingError:
        return redirect(url_for('main.home'))

    



    
