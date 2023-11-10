## 关于配置文件和数据文件

### 博客文章

所有文章和文章目录的总信息存放在 `articles.json` 中，格式为

```json
[
    {
        "id": "1", // 文章或文章目录的 ID
        "label": "sample title 1", // 文章或文章目录的名称
        "type": "article", // 枚举类型，只能为 article 或 folder,
        "children": [ ... ] // 仅文件夹需要提供该参数，列举所有子文件夹和子文章
    }, {
        "id": "2",
        "label": "sample title 2",
        "type": "article",
        "last_modified_time": "2023-11-8 12:34:56" // 最后修改时间
    }
]
```

文章和目录的具体信息存放在 `./articles` 目录下，该目录下的每个文件夹代表一篇文章或一个文章目录，文件夹的名称应当为文章或文章目录的 ID. 

若文件夹代表文章，则该文件夹下应有 `content.md`（存储文章内容）、`data.json`（存储文章数据）和 `comments.json`（存储评论内容）这三个文件. 其中，`data.json` 的内容格式如下：
```json
{
    "id": "100", // 文章 ID
    "label": "Sample Article", // 文章标题
    "create_time": "2023-11-8 12:34:56", // 创建时间
    "last_modified_time": "2023-11-8 12:34:56", // 最后修改时间
    "visits": 114514, // 点击量
}
```

`comments.json` 的内容格式如下：
```json
[
    {
        "uid": "a5976bdb-285e-3a0e-b34e-d70a0a7a8149", // 评论 ID，使用 UUID
        "content": "评论内容",
        "from": "192.168.1.1", // 评论者 IP
        "time": "1919-8-10 11:45:14" // 评论时间
    }, {
        ...
    }
]
```

若文件夹代表文章目录，则其下只含有零个或若干个子文件夹，每个文件夹的名称为文章目录的 ID.