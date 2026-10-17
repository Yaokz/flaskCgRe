
from flask import request, jsonify, session, Blueprint, render_template
# from numpy.f2py.symbolic import as_ge

from models import User
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
@auth_bp.route('/login')
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if not username and password:
        return jsonify({
            "success": False,
            "message": "用户名或密码错误",
        })
    user = User.select().where(User.name == username).first()
    if not user:
        return jsonify({
            "success": False,
            "message": "用户名不存在",
        })
    bool = check_password_hash(user.password, password)
    if bool:
        session['username'] = user.name
        session['user_id'] = user.id
        # session['password'] = password
        return jsonify({
            "success": True,
            "message": "登录成功",
        })
    else:
        return jsonify({
            "success": False,
            "message": "密码不正确",
        })

@auth_bp.route('/session')
def get_session():
    if 'username' in session:
        return jsonify({
            "success": True,
            "username":session['username'],
        })

@auth_bp.route('/register')
def register():
    return render_template('register.html')

@auth_bp.route('/register/addUser', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['userName']
    age = data['age']
    password = data['password']
    if not username:
        return jsonify({
            "success": False,
            "message":"请输入用户名"
        })
    if not password:
        return jsonify({
            "success": False,
            "message": "请输入密码"
        })
    user = User.select().where(User.name == username).first()
    if user:
        return jsonify({
            "success": False,
            "message": "用户已存在"

        })
    user = User.create(name=username, age=age,role=0,password=generate_password_hash(password))
    return jsonify({
        "success": True,
        "message":user.name,
    })

@auth_bp.route('/logout',methods=['POST'])
def logout():
    session.clear()
    return jsonify({
        "success": True,
    })