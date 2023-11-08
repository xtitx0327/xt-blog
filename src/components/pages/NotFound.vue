<script setup>
import { ElEmpty, ElButton } from 'element-plus';
import { Back } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage title="404 Not Found" :show-header="true" :show-sidebar="true">
		<ElEmpty description="出错啦！" style="margin: auto auto;">
			<ElButton size="large" :icon="Back" @click="$router.back()">返回上一页</ElButton>
		</ElEmpty>
	</BasePage>
</template>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin-top: 25px;
	margin-bottom: 35px;
}

.card {
	border-radius: 10px;
	transition: all 0.3s;
	width: 18rem;
}

.card:hover {
	cursor: pointer;
	transform: scale(1.05);
}
</style>
