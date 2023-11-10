import os
import json

# 通用函数

def getPathByID(id):
    def search(item, id, curPath):
        # print('#######')
        # print(item, id, curPath, sep='\n')
        # print('#######')
        if item['id'] == id:
            return curPath
        else:
            if 'children' in item:
                for child in item['children']:
                    return search(child, id, os.path.join(curPath, child['id']))
    
    try:
        if os.path.exists('./data/articles.json'):
            with open('./data/articles.json', 'r') as file:
                tree = json.load(file)
        else:
            tree = []
        
        for item in tree:
            result = search(item, id, os.path.join('./data/articles', item['id']))
            if result:
                return result
        
        return None
    except Exception as e:
        print(e)
        return None

def getParent(JSONList, id):
    for item in JSONList:
        if item['id'] == id:
            return item['parent_id']
        else:
            if item['children']:
                result = getParent(item['children'], id)
                if result:
                    return result
    return None

def search(JSONList, parentId, appendValue):
    if parentId is None:
        JSONList.append(appendValue)
        return True
    for child in JSONList:
        if child['id'] == parentId:
            child['children'].append(appendValue)
            return True
        else:
            if search(child['children'], parentId, appendValue):
                return True
    return False