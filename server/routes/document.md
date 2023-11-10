### 文章管理系统 API 文档

#### 概述
本 API 文档提供了文章管理系统的接口描述。系统允许用户进行文章的增删改查等操作。

---

#### API 接口列表

1. 获取文章列表
2. 获取文章详情
3. 创建文章
4. 创建文件夹
5. 更新文章内容
6. 更新文章结构
7. 重命名文章或文件夹
8. 删除文章

---

#### 1. 获取文章列表

- **请求 URL**: `/article/list`
- **请求方法**: GET
- **权限**: 需要 JWT 认证
- **请求参数**: 无

**成功响应**:
```json
{
    "code": 200,
    "data": [/* 文章列表 */],
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 500,
    "data": [],
    "message": "错误信息"
}
```

---

#### 2. 获取文章详情

- **请求 URL**: `/article/detail`
- **请求方法**: GET
- **权限**: 需要 JWT 认证
- **请求参数**: 
  - `id`: 文章的唯一标识符

**成功响应**:
```json
{
    "code": 200,
    "data": "文章内容",
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 500,
    "data": "",
    "message": "文章内容为空或读取文章时出错"
}
```

---

#### 3. 创建文章

- **请求 URL**: `/article/createArticle`
- **请求方法**: POST
- **权限**: 需要 JWT 认证
- **请求参数**: 
  - `parent_id`: 父级目录的 ID
  - `title`: 文章标题

**成功响应**:
```json
{
    "code": 200,
    "data": {
        "id": "新文章的 ID"
    },
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 500,
    "data": {},
    "message": "错误信息"
}
```

---

#### 4. 创建文件夹

- **请求 URL**: `/article/createFolder`
- **请求方法**: POST
- **权限**: 需要 JWT 认证
- **请求参数**: 
  - `parent_id`: 父级目录的 ID
  - `title`: 文件夹标题

**成功响应**:
```json
{
    "code": 200,
    "data": {
        "id": "新文件夹的 ID"
    },
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 500,
    "data": {},
    "message": "错误信息"
}
```

---

#### 5. 更新文章内容

- **请求 URL**: `/article/update`
- **请求方法**: PUT
- **权限**: 需要 JWT 认证
- **请求参数**: JSON 格式
  - `id`: 文章的唯一标识符
  - `content`: 文章内容

**成功响应**:
```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 404,
    "data": "",
    "message": "文章不存在"
}
```

---

#### 6. 更新文章结构

- **请求 URL**: `/article/updateSturcture`
- **请求方法**: PUT
- **权限**: 需要 JWT 认证
- **请求参数**: JSON 格式
  - `data`: 文章结构数据

**成功响应**:
```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 500,
    "data": {},
    "message": "错误信息"
}
```

---

#### 7. 重命名文章或文件夹

- **请求 URL**: `/article/rename`
- **请求方法**: PUT
- **权限**: 需要 JWT 认证
- **表单参数**:
  - `id`: 文章或文件夹的唯一标识符
  - `title`: 新标题

**成功响应**:
```json
{
   

 "code": 200,
    "data": "",
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 404,
    "data": "",
    "message": "文章不存在"
}
```

---

#### 8. 删除文章

- **请求 URL**: `/article/delete`
- **请求方法**: DELETE
- **权限**: 需要 JWT 认证
- **请求参数**:
  - `id`: 文章的唯一标识符

**成功响应**:
```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

**失败响应**:
```json
{
    "code": 404,
    "data": "",
    "message": "文章不存在"
}
```

---

**注**: 所有接口的 `code` 字段代表 HTTP 状态码，`data` 字段为返回的数据，`message` 字段为返回的消息文本。在使用 API 时，应检查 `code` 字段以确定请求是否成功。