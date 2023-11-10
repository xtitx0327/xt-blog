import { createApp } from 'vue';

import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

import 'highlight.js/styles/atom-one-dark.css';
import hljs from 'highlight.js';

import App from './App.vue';

import * as VueRouter from 'vue-router';

import HomePage from './components/pages/HomePage.vue';
import ContactPage from './components/pages/ContactPage.vue';
import LinkPage from './components/pages/LinkPage.vue';
import GalleryPage from './components/pages/GalleryPage.vue';
import ArticlePage from './components/pages/ArticlePage.vue';
import EditPage from './components/pages/EditPage.vue';
import AdminPage from './components/pages/AdminPage.vue';
import ArticleListPage from './components/pages/ArticleListPage.vue';
import LoginPage from './components/pages/LoginPage.vue';

import NotFound from './components/pages/NotFound.vue';

const routes = [
    { path: '/', component: HomePage },
    { path: '/link', component: LinkPage },
    { path: '/contact', component: ContactPage },
    { path: '/gallery', component: GalleryPage },
    { path: '/admin', component: AdminPage },
    { path: '/article/:id', component: ArticlePage },
    { path: '/articles', component: ArticleListPage },
    { path: '/edit/:id', component: EditPage },
    { path: '/login', component: LoginPage },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
];

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
});

const app = createApp(App);

app.directive('highlight', function (el) {
    let blocks = el.querySelectorAll('pre code');
    blocks.forEach((block) => {
        hljs.highlightBlock(block);
    })
})

app.use(router);
app.use(ElementPlus);
app.mount('#app');