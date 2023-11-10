from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import os
import json

from uuid import uuid1
from datetime import datetime
from utils import getPathByID, search

articleBp = Blueprint('article', __name__, url_prefix = '/article')

@articleBp.route('/list', methods = ['GET'])
def getArticleList():
    try:
        if os.path.exists('./data/articles.json'):
            with open('./data/articles.json', 'r') as file:
                articles = json.load(file)
        else:
            articles = []

        return jsonify({
            'code': 200,
            'data': articles,
            'message': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': [],
            'message': str(e)
        })

@articleBp.route('/detail', methods = ['GET'])
def getArticleDetail():
    try:
        id = request.args.get('id')
        path = getPathByID(id)

        visit = request.args.get('visit')
        if path and os.path.exists(path):
            with open(os.path.join(path, 'content.md'), 'r') as file:
                article = file.read()
            with open(os.path.join(path, 'data.json'), 'r') as file:
                articleData = json.load(file)
            if visit == '1':
                articleData['visits'] += 1
                with open(os.path.join(path, 'data.json'), 'w') as file:
                    json.dump(articleData, file, ensure_ascii = False, indent = 4)
            articleData.update({'content': article})
            if articleData:
                return jsonify({
                    'code': 200,
                    'data': articleData,
                    'message': 'success'
                })
            else:
                return jsonify({
                    'code': 500,
                    'data': '',
                    'message': '读取文章时出错'
                })
        else:
            return jsonify({
                'code': 404,
                'data': '',
                'message': '文章不存在'
            })
        
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': '',
            'message': str(e)
        })

@articleBp.route('/createArticle', methods = ['POST'])
@jwt_required()
def createArticle():
    try:
        parent_id = request.get_json().get('parent')
        title = request.get_json().get('title')

        if parent_id is None:
            path = './data/articles/'
        else:
            path = getPathByID(parent_id)
        
        if path is None:
            return jsonify({
                'code': 404,
                'data': '',
                'message': '父级目录不存在'
            })
        
        id = str(uuid1())
        os.mkdir(os.path.join(path, id))
        with open(os.path.join(path, id, 'content.md'), 'w') as file:
            file.write('## New article\n\nWrite something here...')
        with open(os.path.join(path, id, 'data.json'), 'w') as file:
            json.dump({
                'id': id,
                'label': title,
                'create_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'last_modified_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'visits': 0,
            }, file, ensure_ascii = False, indent = 4)
        with open('./data/articles.json', 'r') as file:
            articles = json.load(file)
        search(articles, parent_id, {
            'id': id,
            'label': title,
            'type': 'article',
            'last_modified_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        })
        with open('./data/articles.json', 'w') as file:
            json.dump(articles, file, ensure_ascii = False, indent = 4)

        return jsonify({
            'code': 200,
            'data': {
                'id': id
            },
            'message': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': {},
            'message': str(e)
        })

@articleBp.route('/createFolder', methods = ['POST'], endpoint = 'create_folder')
@jwt_required()
def createFolder():
    try:
        print(request.get_json())
        parent_id = request.get_json().get('parent')
        title = request.get_json().get('title')

        if parent_id is None:
            path = './data/articles/'
        else:
            path = getPathByID(parent_id)
        print(path)
        
        if path is None:
            return jsonify({
                'code': 404,
                'data': '',
                'message': '父级目录不存在'
            })
        
        id = str(uuid1())
        os.mkdir(os.path.join(path, id))
        with open('./data/articles.json', 'r') as file:
            articles = json.load(file)
        search(articles, parent_id, {
            'id': id,
            'label': title,
            'type': 'folder',
            'children': [],
        })
        with open('./data/articles.json', 'w') as file:
            json.dump(articles, file, ensure_ascii = False, indent = 4)

        return jsonify({
            'code': 200,
            'data': {
                'id': id
            },
            'message': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': {},
            'message': str(e)
        })

@articleBp.route('/update', methods = ['POST'], endpoint = 'update_article')
@jwt_required()
def updateArticle():
    content = request.get_json().get('content')
    id = request.get_json().get('id')
    print(content, id)

    path = getPathByID(id)
    if path and os.path.exists(path):
        with open(os.path.join(path, 'content.md'), 'w') as file:
            file.write(content)
        with open(os.path.join(path, 'data.json'), 'r') as file:
            data = json.load(file)
        data['last_modified_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(os.path.join(path, 'data.json'), 'w') as file:
            json.dump(data, file, ensure_ascii = False, indent = 4)
        return jsonify({
            'code': 200,
            'data': '',
            'message': 'success'
        })
    else:
        return jsonify({
            'code': 404,
            'data': '',
            'message': '文章不存在'
        })

@articleBp.route('/updateSturcture', methods = ['POST'], endpoint = 'update_struct')
@jwt_required()
def updateSturcture():
    try:
        data = request.get_json().get('data')

        with open('./data/articles.json', 'w') as file:
            json.dump(data, file, ensure_ascii = False, indent = 4)
        
        return jsonify({
            'code': 200,
            'data': '',
            'message': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': {},
            'message': str(e)
        })

@articleBp.route('/rename', methods = ['POST'], endpoint = 'do_rename')
@jwt_required()
def rename():
    def doRename(list, id, newName):
        for item in list:
            if item['id'] == id:
                item['label'] = newName
                return True
            else:
                if item.get('children'):
                    if doRename(item['children'], id, newName):
                        return True

    try:
        id = request.get_json().get('id')
        title = request.get_json().get('title')

        path = getPathByID(id)
        if path and os.path.exists(path):
            try:
                with open(os.path.join(path, 'data.json'), 'r') as file:
                    data = json.load(file)
                data['label'] = title
                data['last_modified_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with open(os.path.join(path, 'data.json'), 'w') as file:
                    json.dump(data, file, ensure_ascii = False, indent = 4)
            except:
                pass

            with open('./data/articles.json', 'r') as file:
                articles = json.load(file)
            doRename(articles, id, title)
            print(articles)
            with open('./data/articles.json', 'w') as file:
                json.dump(articles, file, ensure_ascii = False, indent = 4)

            return jsonify({
                'code': 200,
                'data': '',
                'message': 'success'
            })
        else:
            return jsonify({
                'code': 404,
                'data': '',
                'message': '文章不存在'
            })
    
    except Exception as e:
        return jsonify({
            'code': 500,
            'data': {},
            'message': str(e)
        })

@articleBp.route('/delete', methods = ['POST'], endpoint = 'delete_article')
@jwt_required()
def deleteArticle():
    id = request.args.get('id')

    path = getPathByID(id)
    if path and os.path.exists(path):
        os.remove(os.path.join(path, 'content.md'))
        os.remove(os.path.join(path, 'data.json'))
        os.rmdir(path)
        return jsonify({
            'code': 200,
            'data': '',
            'message': 'success'
        })
    else:
        return jsonify({
            'code': 404,
            'data': '',
            'message': '文章不存在'
        })