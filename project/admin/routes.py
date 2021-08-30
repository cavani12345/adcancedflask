from flask import Blueprint

admin = Blueprint('admin',__name__)

@admin.route('/')
def home():
    return 'admin home page'