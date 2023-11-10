<template>
	<div class="md-container">
		<ElRow v-if="props.showOptions">
			<ElSpace size="large" alignment="center" style="margin-bottom: 1rem;">
				<ElButton @click="updateArticle">保存更改</ElButton>
				<ElDivider direction="vertical"></ElDivider>
				<ElText tag="b">渲染选项：</ElText>
				<ElCheckbox v-model="autoRender">自动渲染</ElCheckbox>
				<ElButton @click="MathJax.doRender">重新渲染</ElButton>
			</ElSpace>
		</ElRow>
		<div class="md-content" v-html="renderedContent" v-highlight></div>
	</div>
</template>

<script setup>
import { apiBase } from '../../config.js';
import { ElButton, ElCheckbox, ElDivider, ElRow, ElSpace, ElText, ElMessage } from 'element-plus';
import { computed, watch, ref } from 'vue';
import { marked } from 'marked';
import MathJax from './MathJax.js'
import hljs from 'highlight.js';

const props = defineProps(['content', 'showOptions', 'id']);

MathJax.initMathjaxConfig();

marked.setOptions({
	highlight: (code, lang) => {
		return hljs.highlightAuto(code, [lang]).value;
	},
});

const autoRender = ref(true);

const renderedContent = computed(() => {
	if (autoRender.value)
		return marked.parse(props.content);
	else
		return props.content;
});

watch(renderedContent, () => {
	if (autoRender.value)
		MathJax.doRender();
	return;
});

function updateArticle() {
	console.log(props.id, props.content)
	fetch(apiBase + '/api/article/update', {
		method: 'POST',
		body: JSON.stringify({
			id: props.id,
			content: props.content
		}),
		headers: {
			'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
			'Content-Type': 'application/json'
		}
	})
		.then(response => response.json())
		.then(responseData => {
			if (responseData.code === 200) {
				ElMessage({
					message: '保存成功',
					type: 'success'
				});
			} else
				ElMessage({
					message: '保存失败',
					type: 'error'
				});
		})
		.catch(() => {
			ElMessage({
				message: '保存失败',
				type: 'error'
			})
		});
}
</script>

<style scoped>
.md-content {
	border-radius: 5px;
	padding: 10px;
	overflow-y: auto;
	max-height: 100%;
}

.md-container {
	align-items: center;
	justify-content: center;
	max-height: 75vh;
	overflow-y: auto;
}

code {
	font-size: 16px;
}
</style>