<script setup>
import { ElRow, ElCol, ElInput } from 'element-plus';
import {  } from '@element-plus/icons-vue';
import { ref, onMounted } from 'vue';
import BasePage from './BasePage.vue';
import RenderMarkdown from '../common/RenderMarkdown.vue';

const content = ref('');

onMounted(() => {
	const textareaElement = document.querySelector('textarea');
	setTimeout(() => {textareaElement.style.height = textareaElement.parentElement.computedStyleMap().height;}, 1000);
	
});
</script>

<template>
	<BasePage title="编辑文章" :show-header="true" :show-sidebar="true">
		<ElRow style="height: 100%; max-height: 70vh;">
			<ElCol :span="12">
				<ElInput type="textarea" v-model="content" style="min-height: 100%; font-size: 18px;"></ElInput>
			</ElCol>
			<ElCol :span="1"></ElCol>
			<ElCol :span="11">
				<RenderMarkdown :content="content"></RenderMarkdown>
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
