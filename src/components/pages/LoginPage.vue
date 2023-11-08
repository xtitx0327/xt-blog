<script setup>
import { ElRow, ElCol, ElImage, ElForm, ElFormItem, ElInput } from 'element-plus';
import { Avatar, Lock } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage title="登录" :show-header="false" :show-sidebar="false">
		<ElRow >
			<ElCol :span="12">
				<ElImage src="/public/login.jpg" fit="scale-down"></ElImage>
			</ElCol>
			<ElCol :span="12">
				<div class="login-container">
					<ElForm label-position="top">
						<ElFormItem label="用户名">
							<ElInput size="large" placeholder="用户名" :prefix-icon="Avatar"></ElInput>
						</ElFormItem>
						<ElFormItem label="密码">
							<ElInput size="large" type="password" placeholder="密码" :prefix-icon="Lock" show-password></ElInput>
						</ElFormItem>
					</ElForm>
				</div>
			</ElCol>
		</ElRow>
	</BasePage>
</template>

<style scoped>
.login-container {
	padding: 8rem;
	margin: auto;
}
</style>
