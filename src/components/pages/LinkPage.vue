<script setup>
import { ElCollapse, ElCollapseItem, ElIcon, ElText, ElButton, ElRow, ElLink, ElSpace } from 'element-plus';
import { School, ChromeFilled, Ship } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage title="友情链接" :show-header="true" :show-sidebar="true">
		<div class="container">
			<ElCollapse>
				<ElCollapseItem>
					<template #title>
						<ElText size="large" tag="b">
							<ElIcon>
								<School />
							</ElIcon>
							&nbsp;浙大相关
						</ElText>
					</template>
					<ElRow>
						<ElSpace size="large">
							<ElLink href="https://jwbinfosys.zju.edu.cn"><ElButton plain>教务网</ElButton></ElLink>
							<ElLink href="https://classroom.zju.edu.cn"><ElButton plain>智云课堂</ElButton></ElLink>
							<ElLink href="https://course.zju.edu.cn"><ElButton plain>学在浙大</ElButton></ElLink>
						</ElSpace>
					</ElRow>
				</ElCollapseItem>
				<ElCollapseItem>
					<template #title>
						<ElText size="large" tag="b">
							<ElIcon>
								<ChromeFilled />
							</ElIcon>
							&nbsp;XT 的网站
						</ElText>
					</template>
					<ElRow>
						<ElSpace size="large">
							<ElLink href="https://xtitx327.top"><ElButton plain>个人主页</ElButton></ElLink>
							<ElLink href="https://chat.xtitx327.top"><ElButton plain>ChatGPT 镜像站</ElButton></ElLink>
							<ElLink href="https://shop.xtitx327.top"><ElButton plain>ChatGPT 商城</ElButton></ElLink>
							<ElLink href="https://cloud.xtitx327.top"><ElButton plain>NextCloud 云盘</ElButton></ElLink>
						</ElSpace>
					</ElRow>
				</ElCollapseItem>
				<ElCollapseItem>
					<template #title>
						<ElText size="large" tag="b">
							<ElIcon>
								<Ship />
							</ElIcon>
							&nbsp;其他常用
						</ElText>
					</template>
					<ElRow>
						<ElSpace size="large">
							<ElLink href="https://cn.vuejs.org"><ElButton plain>Vue.js 中文文档</ElButton></ElLink>
							<ElLink href="https://github.com/xtitx0327"><ElButton plain>我的 GitHub</ElButton></ElLink>
						</ElSpace>
					</ElRow>
				</ElCollapseItem>
			</ElCollapse>
		</div>
	</BasePage>
</template>

<style scoped>
	.container {
		margin: 5rem 5rem;
	}
</style>
