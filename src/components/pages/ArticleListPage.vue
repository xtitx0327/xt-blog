<script setup>
import { apiBase } from '../../config.js';
import { onBeforeMount, ref } from 'vue';
import { ElMessage, ElMenu, ElMenuItem, ElPagination, ElEmpty } from 'element-plus';
import BasePage from './BasePage.vue';
import { useRouter } from 'vue-router';

let articleList = ref([]), originList = [];
let currentPage = ref(1);
const pageSize = ref(8);
const router = useRouter();

onBeforeMount(() => {
	function convert(JSONList) {
		for (let item of JSONList) {
			if (item.type === 'article') {
				articleList.value.push(item);
			}
			else
				convert(item.children);
		}
	}

	fetch(apiBase + '/api/article/list')
		.then(response => response.json())
		.then(data => data.data)
		.then(list => {
			originList = list;
			convert(originList);
		})
		.catch(() => ElMessage.error('文章列表获取失败'));
});

function getParentLabel(id, list, label) {
	for (let item of list)
		if (item.id === id)
			return label;
		else if (item.type === 'folder') {
			let result = getParentLabel(id, item.children, item.label);
			if (result)
				return result;
		}
	return null;
}

function navigateToArticle(id) {
	router.push(`/article/${id}?title=${articleList.value.find(item => item.id === id).label}`);
}
</script>

<template>
	<BasePage title="文章列表" :show-header="true" :show-sidebar="true">
		<div class="page-container">
			<ElMenu style="width: 100%;">
				<ElMenuItem v-for="(item, index) of articleList.slice((currentPage - 1) * pageSize, currentPage * pageSize)" :key="index" @click="navigateToArticle(item.id)">
					<div class="item-row">
						<div class="folder-text">[{{ getParentLabel(item.id, originList, '') ? getParentLabel(item.id,
							originList, '') : '无分类' }}]</div>
						<div>{{ item.label }}</div>
						<div class="flex-grow">&nbsp;</div>
						<div style="font-size: 13px; color: #73767a">{{ item.last_modified_time }}</div>
					</div>
				</ElMenuItem>
				<ElEmpty v-if="articleList.length === 0" description="暂无文章"></ElEmpty>
			</ElMenu>
			<ElPagination layout="prev, pager, next" :total="articleList.length" :page-size="pageSize" v-model:current-page="currentPage" />
		</div>
	</BasePage>
</template>

<style scoped>
.folder-text {
	color: #79bbff;
	margin-right: 10px;
}

.page-container {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
	height: 95%;
}

.item-row {
	display: flex;
	flex-direction: row;
	align-items: center;
	width: 100%;
}

.flex-grow {
	flex-grow: 1;
}
</style>
