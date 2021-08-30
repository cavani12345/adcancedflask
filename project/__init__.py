from flask import Flask, config
from project.main.routes import main
from project.admin.routes import admin
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "123456"
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'flaskapp'

db = MySQL()
db.init_app(app)


# registering blueprint
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')



