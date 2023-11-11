## 🎈 XTBlog 🎈

✨ **基于 Element Plus + Vue 3 + Flask，前后端分离的个人主页与个人博客网站.**

本项目完全由作者独立完成，也是作者的第一个 `Vue.js` 项目，开发本项目的主要目的是学习.

项目已经作为我的个人网站部署在 [https://xtitx327.top](https://xtitx327.top)，欢迎访问！🎇

### 目录

- [🎈 XTBlog 🎈](#-xtblog-)
  - [目录](#目录)
  - [安装与使用](#安装与使用)
  - [版本更新记录](#版本更新记录)
    - [测试版](#测试版)
  - [待更新内容](#待更新内容)
  - [关于项目](#关于项目)

### 安装与使用

1. 首先，确认你在服务器上安装了最新版本的 `Node.js` 和 `npm`，以及 `Python 3.7+`. 

2. 克隆仓库到本地：
```
git clone git@github.com:xtitx0327/xt-blog.git
cd xt-blog
```

3. 将前端项目打包：
```
npm run build
```

4. 安装后端的依赖：
```
cd server
pip install -r requirements.txt
```

5. 使用 Nginx 或其他方式进行部署.

### 版本更新记录

#### 测试版

- **v0.9.1**：2023/11/11 发布，修复了图片加载、文章中数学公式渲染的 BUG，更新了 `README.md`

- **v0.9.0**：2023/11/10 发布，完成了大多数基本功能

### 待更新内容

- [ ] 更新 API 文档（`/server/routes/document.md`）中的错误
- [ ] 管理员后台中更新账号密码的后端 API
- [ ] 管理员后台中的数据统计页面
- [ ] 文章的评论系统
- [ ] 优化文章的点击量统计方式
- [ ] 响应式设计，改进移动端浏览体验

### 关于项目

[![Star History Chart](https://api.star-history.com/svg?repos=xtitx0327/xt-blog&type=Date)](https://star-history.com/#xtitx0327/xt-blog&Date)