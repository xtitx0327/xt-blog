from flask import Blueprint, jsonify
articleBp = Blueprint('article', __name__, url_prefix = '/article')

@articleBp.route('/article/list', methods = ['GET'])
def getArticleList():
    return jsonify({
        'code': 200,
        'data': {},
        'message': 'success'
    })

@articleBp.rpite('/article/detail', methods = ['GET'])
def getArticleDetail():
    return jsonify({
        'code': 200,
        'data': {},
        'message': 'success'
    })

@articleBp.route('/article/create', methods = ['POST'])
def createArticle():
    return jsonify({
        'code': 200,
        'data': {},
        'message': 'success'
    })

@articleBp.route('/article/update', methods = ['PUT'])
def updateArticle():
    return jsonify({
        'code': 200,
        'data': {},
        'message': 'success'
    })

@articleBp.route('/article/delete', methods = ['DELETE'])
def deleteArticle():
    return jsonify({
        'code': 200,
        'data': {},
        'message': 'success'
    })