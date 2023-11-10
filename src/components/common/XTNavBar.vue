<script setup>
import 'element-plus/theme-chalk/dark/css-vars.css';
import 'element-plus/theme-chalk/dark/css-vars.css';
import { apiBase } from '../../config.js';
import { ref } from 'vue';
import { useDark, useToggle } from '@vueuse/core';
import { useRouter, onBeforeRouteLeave } from 'vue-router';
import { ElMenu, ElMenuItem, ElButton, ElSwitch, ElMessage, ElDialog, ElForm, ElFormItem, ElInput } from 'element-plus';
import { Search, Sunny, Moon, Avatar, Lock } from '@element-plus/icons-vue';
import XTLogo from './XTLogo.vue';

const isDark = useDark();
const toggleDark = useToggle(isDark);

const router = useRouter();

const registerDialog = ref(false);

onBeforeRouteLeave((to, from, next) => {
    if (to.path === '/admin') {
        fetch(apiBase + '/api/auth/status', {
            headers: {
                'Authorization': 'Bearer ' + window.localStorage.getItem('token')
            }
        })
            .then(response => response.json())
            .then(responseData => {
                console.log(responseData);
                if (responseData.data.success)
                    next();
                else {
                    if (responseData.message === '未登录')
                        router.push('/login');
                    else {
                        ElMessage.info('管理员身份信息不存在，请先注册');
                        registerDialog.value = true;
                    }
                }
            })
            .catch(() => {
                ElMessage.error('登录状态异常，请重新登录');
                router.push('/login');
            });
    } else
        next();
});

const username = ref(''), password = ref(''), confirmPassword = ref('');

function handleRegister() {
    if (username.value === '' || password.value === '' || confirmPassword.value === '') {
        ElMessage.error('用户名和密码不能为空');
        return;
    }
    if (password.value !== confirmPassword.value) {
        ElMessage.error('两次输入的密码不一致');
        return;
    }
    fetch(apiBase + '/api/auth/register', {
        method: 'POST',
        body: JSON.stringify({
            username: username.value,
            password: password.value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(responseData => {
            if (responseData.data.success) {
                ElMessage.success('注册成功！');
                router.push('/login');
            } else
                ElMessage.error('注册失败');
        })
        .catch(() => { ElMessage.error('注册失败！'); });
}
</script>

<template>
    <ElMenu mode="horizontal" :ellipsis="false" :router="true">
        <ElMenuItem index="/" class="ml-3">
            <XTLogo></XTLogo>
        </ElMenuItem>
        <div class="flex-grow"></div>
        <div class="menu-container">
            <ElButton round :icon="Search">&nbsp;&nbsp;&nbsp;搜索…&nbsp;&nbsp;&nbsp;</ElButton>
            &nbsp;&nbsp;&nbsp;
        </div>
        <ElMenuItem index="/admin" class="ml-5">&nbsp;管理后台&nbsp;</ElMenuItem>
        <ElMenuItem index="/contact" class="ml-5">&nbsp;联系作者&nbsp;</ElMenuItem>
        <div class="menu-container">
            &nbsp;&nbsp;&nbsp;
            <ElSwitch class="mr-5" :model-value="isDark" @click="toggleDark()" :active-icon="Moon" :inactive-icon="Sunny"
                inline-prompt></ElSwitch>
            &nbsp;&nbsp;&nbsp;
        </div>
    </ElMenu>
    <ElDialog v-model="registerDialog" title="注册信息" :align-center="true" :close-on-click-modal="false">
        <ElForm label-position="top">
            <ElFormItem label="用户名">
                <ElInput v-model="username" size="large" placeholder="用户名" :prefix-icon="Avatar">
                </ElInput>
            </ElFormItem>
            <ElFormItem label="密码">
                <ElInput v-model="password" size="large" type="password" placeholder="密码" :prefix-icon="Lock" show-password ></ElInput>
            </ElFormItem>
            <ElFormItem label="确认密码">
                <ElInput v-model="confirmPassword" size="large" type="password" placeholder="密码" :prefix-icon="Lock" show-password ></ElInput>
            </ElFormItem>
            <ElFormItem style="margin-top: 25px;">
                <ElButton type="primary" size="large" @click="handleRegister">注册</ElButton>
            </ElFormItem>
        </ElForm>
    </ElDialog>
</template>

<style scoped>
.flex-grow {
    flex-grow: 1;
}

.menu-container {
    display: flex;
    align-items: center;
    margin-bottom: 0;
}
</style>
