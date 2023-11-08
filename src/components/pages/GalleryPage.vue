<script setup>
import { ElTimeline, ElTimelineItem, ElImage } from 'element-plus';
import {  } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage title="照片墙" :show-header="true" :show-sidebar="true">
		<ElTimeline>
			<ElTimelineItem timestamp="2022/3/27" placement="top">
				<ElImage src="/public/IMG_2464.PNG"></ElImage>
			</ElTimelineItem>
		</ElTimeline>
	</BasePage>
</template>

<style scoped>
.label-container {
	display: flex;
	align-items: center;
}

a {
	text-decoration: none;
	color: #409eff;
}
</style>
