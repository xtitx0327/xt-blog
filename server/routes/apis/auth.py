import os
from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta

authBp = Blueprint('auth', __name__, url_prefix = '/auth')

@authBp.route('/login', methods = ['POST'])
def doLogin():
    givenUsername = request.get_json().get('username')
    givenPassword = request.get_json().get('password')

    with open('./data/auth', 'r') as file:
        username, password = file.read().splitlines()
    
    if givenUsername == username and check_password_hash(password, givenPassword):
        token = create_access_token(identity = {'username': username}, expires_delta = timedelta(days = 3))
        response = make_response(jsonify({
            'code': 200,
            'data': {'success': True, 'token': token},
            'message': '登陆成功'
        }))
        response.set_cookie('access_token_cookie', token)
        return response
    else:
        return jsonify({
            'code': 200,
            'data': {'success': False},
            'message': '用户名或密码错误'
        })

@authBp.route('/register', methods = ['POST'])
def register():
    username = request.get_json().get('username')
    password = request.get_json().get('password')

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

@authBp.route('/status', methods = ['GET'])
def getAuthStatus():
    try:
        jwt_header, jwt_data = verify_jwt_in_request()
        print(jwt_data)
        username = jwt_data['sub']['username']
        return jsonify({
            'code': 200,
            'data': {'success': True, 'username': username},
            'message': '已登录'
        })
    except Exception as e:
        print(e)
        if os.path.exists('./data/auth'):
            return jsonify({
                'code': 200,
                'data': {'success': False},
                'message': '未登录'
            })
        else:
            return jsonify({
                'code': 200,
                'data': {'success': False},
                'message': '未注册'
            })