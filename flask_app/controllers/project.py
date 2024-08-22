from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.controllers.projects import User # CHANGE FILE NAME

#Test to see if 'python server.py' is running with flask installed
@app.route('/')
def index():
    return render_template('index.html')


'''
EACH LINE FROM HERE IS SUBJECT TO CHANGE, 
BUT THIS IS A TEMPLATE FOR WHAT YOU WANT FOR EACH CRUD STEP 
'''
#CREATE
@app.route('/users/new')
def create_new():
    return render_template('create.html')

@app.route('/users/new/process', methods=['POST'])
def process_new():
    User.save(request.form)
    return redirect('/users')


#READ ALL
@app.route('/users')
def users():
    return render_template('read_all.html', users_list = User.get_all()) 


#READ ONE
@app.route('/users/<int:id>')
def read_one(id):
    return render_template('read_one.html', user = User.get_one(id))


#UPDATE
@app.route('/users/<int:id>/edit')
def user_edit(id):
    return render_template('update.html', user = User.get_one(id))

@app.route('/users/<int:id>/edit/process', methods=['POST'])
def update_user(id):
    form_data = {
        **request.form,
        'id' : id
    }
    User.update(form_data)
    return redirect('/users')

#DELETE
@app.route('/users/<int:id>/destroy', methods=['POST'])
def delete(id):
    User.delete(id)
    # return render_template('/test.html')
    print('anything')
    return redirect('/users')