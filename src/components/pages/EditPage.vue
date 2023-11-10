<script setup>
import { apiBase } from '../../config.js';
import { ElRow, ElCol, ElInput, ElMessage, ElMessageBox } from 'element-plus';
import { useRouter, onBeforeRouteLeave } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import BasePage from './BasePage.vue';
import RenderMarkdown from '../common/RenderMarkdown.vue';

const content = ref('获取文章内容失败');

const router = useRouter();

let articleID = ref('');

onBeforeMount(() => {
	articleID.value = router.currentRoute.value.params.id;
	fetch(apiBase + `/api/article/detail?id=${articleID.value}`)
		.then(response => response.json())
		.then(data => data.data)
		.then(data => {
			content.value = data.content;
		})
		.catch(() => { ElMessage.error('获取文章内容失败'); });
});

onBeforeRouteLeave((to, from, next) => {
	ElMessageBox.confirm('是否确认离开？所有未保存的更改都将丢失。', '提示', {
		type: 'warning',
		confirmButtonText: '确认离开',
		cancelButtonText: '取消',
	}).then(() => {
		next();
	}).catch(() => {
		next(false);
	});
});
</script>

<template>
	<BasePage title="编辑文章" :show-header="false" :show-sidebar="true">
		<ElRow style="height: 100%; max-height: 70vh;">
			<ElCol :span="12">
				<ElInput type="textarea" v-model="content" style="min-height: 100%; font-size: 18px;"></ElInput>
			</ElCol>
			<ElCol :span="1">
			</ElCol>
			<ElCol :span="11">
				<RenderMarkdown :content="content" :id="articleID" :show-options="true"></RenderMarkdown>
			</ElCol>
		</ElRow>
	</BasePage>
</template>

<style>
textarea {
	resize: none;
	min-height: 75%;
}
</style>
