import os
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta
authBp = Blueprint('auth', __name__, url_prefix = '/auth')

# Auth API

@authBp.route('/auth/login', methods = ['POST'])
def login():
    givenUsername = request.form.get('username')
    givenPassword = request.form.get('password')

    with open('./data/auth', 'r') as file:
        username, password = file.read().splitlines()
    
    if givenUsername == username and check_password_hash(password, givenPassword):
        return jsonify({
            'code': 200,
            'data': {'success': True, 'token': create_access_token(identity = {'username': username}, expires_delta = timedelta(days = 3))},
            'message': '登陆成功'
        })
    else:
        return jsonify({
            'code': 200,
            'data': {'success': False},
            'message': '用户名或密码错误'
        })

@authBp.route('/auth/register', methods = ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == '' or password == '':
        return jsonify({
            'code': 200,
            'data': {'success': False},
            'message': '用户名和密码不能为空'
        })

    if os.path.exists('./data/auth'):
        return jsonify({
            'code': 200,
            'data': {'success': False},
            'message': '请勿重复注册'
        })

    with open('./data/auth', 'w') as file:
        file.write(username + '\n' + generate_password_hash(password))
    
    return jsonify({
        'code': 200,
        'data': {'success': True, 'token': create_access_token(identity = {'username': username}, expires_delta = timedelta(days = 3))},
        'message': '注册成功'
    })