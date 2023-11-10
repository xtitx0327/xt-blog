<script setup>
import { apiBase } from '../../config.js';
import { ElDivider, ElMessage } from 'element-plus';
import { useRouter } from 'vue-router';
import { onBeforeMount, ref } from 'vue';
import BasePage from './BasePage.vue';
import RenderMarkdown from '../common/RenderMarkdown.vue';

const router = useRouter();
const id = ref(router.currentRoute.value.params.id);
const title = ref(router.currentRoute.value.query.title);
let content = ref('');
let visits = ref(''), lastModified = ref('');

onBeforeMount(() => {
	fetch(apiBase + '/api/article/detail?id=' + id.value + '&visit=1')
		.then(response => response.json())
		.then(data => data.data)
		.then(articleData => {
			content.value = articleData.content;
			visits.value = articleData.visits;
			lastModified.value = articleData.last_modified_time;
		})
		.catch(() => ElMessage.error('文章内容获取失败'));
});
</script>

<template>
	<BasePage title="文章详情" :show-header="true" :show-sidebar="true">
		<div class="article-container">
			<h2 style="text-align: center;">{{ title }}</h2>
			<span style="font-size: 13px; text-align: center;"><b>点击量：</b>{{ visits }}&nbsp;&nbsp;&nbsp;&nbsp;<b>修改日期：</b>{{ lastModified }}</span>
			<ElDivider type="horizon"></ElDivider>
			<RenderMarkdown :content="content" :show-options="false" :id="id"></RenderMarkdown>
		</div>
	</BasePage>
</template>

<style scoped>
.article-container {
	display: flex;
	justify-content: center;
	flex-direction: column;
}
</style>
