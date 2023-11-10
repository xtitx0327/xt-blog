<script setup>
import { apiBase } from '../../config.js';
import { ref } from 'vue';
import { ElRow, ElImage, ElForm, ElFormItem, ElInput, ElMessage } from 'element-plus';
import { Avatar, Lock } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref(''), password = ref('');

function navigateBack() {
	router.back();
}

function handleLogin() {
	if (username.value === '' || password.value === '') {
		ElMessage.error('用户名和密码不能为空');
		return;
	}

	fetch(apiBase + '/api/auth/login', {
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
				ElMessage.success('登录成功');
				window.localStorage.setItem('token', responseData.data.token);
				router.push('/admin');
			} else {
				ElMessage.error('用户名或密码错误');
				return;
			}
		})
		.catch(() => {
			ElMessage.error('未知异常，登录失败');
		});
}
</script>

<template>
	<BasePage title="登录" :show-header="false" :show-sidebar="false" :main-no-padding="true">
		<ElRow>
			<ElImage src="/public/login.jpg" style="height: 85vh; max-width: calc(100% - 500px);"></ElImage>
			<div class="login-container">
				<ElForm label-position="top">
					<ElFormItem label="用户名">
						<ElInput v-model="username" size="large" placeholder="用户名" :prefix-icon="Avatar" style="width: 300px;"></ElInput>
					</ElFormItem>
					<ElFormItem label="密码">
						<ElInput v-model="password" size="large" type="password" placeholder="密码" :prefix-icon="Lock" show-password style="width: 300px;"></ElInput>
					</ElFormItem>
					<ElFormItem style="margin-top: 25px;">
						<ElButton type="primary" size="large" @click="handleLogin">登录</ElButton>
						<ElButton type="secondary" size="large" @click="navigateBack">返回上一页</ElButton>
					</ElFormItem>
				</ElForm>
			</div>
		</ElRow>
	</BasePage>
</template>

<style scoped>
.login-container {
	padding: 15px;
	margin: auto auto;
	height: min-content;
	width: max-content;
}

</style>
