<template>
	<div class="md-container">
		<ElRow>
			<ElSpace size="large" alignment="center" style="margin-bottom: 1rem;">
				<ElText tag="b">渲染选项：</ElText>
				<ElCheckbox v-model="autoRender">自动渲染</ElCheckbox>
				<ElButton @click="MathJax.doRender">重新渲染</ElButton>
			</ElSpace>
		</ElRow>
		<div class="md-content" v-html="renderedContent" v-highlight></div>
	</div>
</template>

<script>

</script>

<script setup>
import { ElButton, ElCheckbox, ElRow, ElSpace, ElText } from 'element-plus';
import { computed, watch, ref } from 'vue';
import { marked } from 'marked';
import MathJax from './MathJax.js'
import hljs from 'highlight.js';

const props = defineProps(['content']);

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
</script>

<style scoped>
.md-content {
	border-radius: 5px;
	border: 1px solid #ebebeb;
	background-color: #f4f4f4;
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