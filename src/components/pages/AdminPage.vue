<script setup>
import { ref } from 'vue';
import { ElTabPane, ElTabs, ElButton, ElTree, ElTooltip, ElInput } from 'element-plus';
import { Plus, Delete, Edit, EditPen } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

const data = [
	{
		id: 1,
		label: '文件夹1',
		type: 'folder',
		children: [
			{ id: 2, label: '文章1-1', type: 'article' },
			{ id: 3, label: '文章1-2', type: 'article' },
		],
	},
	{
		id: 4,
		label: '文件夹2',
		type: 'folder',
		children: [
			{ id: 5, label: '文章2-1', type: 'article' },
			{ id: 6, label: '文章2-2', type: 'article' },
			{
				id: 7,
				label: '子文件夹2-1',
				type: 'folder',
				children: [
					{ id: 8, label: '文章2-1-1', type: 'article' },
					{ id: 9, label: '文章2-1-2', type: 'article' },
				],
			},
		],
	},
	{
		id: 10,
		label: '文件夹3',
		type: 'folder',
		children: [
			{ id: 11, label: '文章3-1', type: 'article' },
			{ id: 12, label: '文章3-2', type: 'article' },
			{
				id: 13,
				label: '子文件夹3-1',
				type: 'folder',
				children: [
					{ id: 14, label: '文章3-1-1', type: 'article' },
				],
			},
			{
				id: 15,
				label: '子文件夹3-2',
				type: 'folder',
				children: [],
			},
		],
	},
	{
		id: 16,
		label: '文件夹4',
		type: 'folder',
		children: []
	},
	// ...更多其他数据
];

const editingId = ref(null);
const curInputValue = ref('');

const renameLabel = (node, id, value) => {
	if (node.id === id) {
		node.label = value;
		return;
	}
	if (!node.children)
		return;
	for (let child of node.children) {
		renameLabel(child, id, value);
	}
};

const cancelEditNode = () => {
	if (editingId.value === null)
		return;
	for (let node of data)
		renameLabel(node, editingId.value, curInputValue.value);
	editingId.value = null;
	curInputValue.value = '';
};

const handleNodeDoubleClick = (data) => {
	editingId.value = data.id;
	curInputValue.value = data.label;
};

const addNode = (parentData) => {
	// 添加节点的逻辑
	// console.log("Add node", parentData);
};

const deleteNode = (data) => {
	// 删除节点的逻辑
	// console.log("Delete node", data);
};

const renameNode = (data) => {
	// 重命名节点的逻辑
	cancelEditNode();
	curInputValue.value = data.label;
	editingId.value = data.id;
};

const editArticle = (data) => {
	// 编辑文章的逻辑
	// console.log("Edit article", data);
};

</script>

<template>
	<BasePage title="管理后台" :show-header="false" :show-sidebar="true">
		<ElTabs>
			<ElTabPane label="数据统计">
				显示网站的统计信息
			</ElTabPane>
			<ElTabPane label="文章管理">
				<h3>文章分类/目录</h3>
				<ElTree :data="data" node-key="id" draggable style="padding: 15px; margin: 25px; border-radius: 5px; border-style: solid; border-width: 1px; border-color: #79bbff;" default-expand-all>
					<template #default="{ node, data }">
						<span @dblclick.stop="handleNodeDoubleClick(data)">
							<ElTooltip content="添加文章">
								<ElButton type="text" :icon="Plus" @click.stop="addNode(data)" v-if="data.type === 'folder'"></ElButton>
							</ElTooltip>
							<ElTooltip :content="data.type === 'folder' ? '删除文件夹' : '删除文章'">
								<ElButton type="text" :icon="Delete" @click.stop="deleteNode(data)"></ElButton>
							</ElTooltip>
							<ElTooltip content="重命名">
								<ElButton type="text" :icon="Edit" @click.stop="renameNode(data)"></ElButton>
							</ElTooltip>
							<ElTooltip v-if="data.type === 'article'" content="编辑文章">
								<ElButton type="text" :icon="EditPen" @click.stop="editArticle(data)"></ElButton>
							</ElTooltip>
							<ElInput v-model="curInputValue" v-if="editingId === data.id" @keyup.enter="cancelEditNode()"></ElInput>
							<span style="margin-left: 10px;" v-else>{{ node.label }}</span>
						</span>
					</template>
				</ElTree>
			</ElTabPane>
			<ElTabPane label="权限信息">

			</ElTabPane>
		</ElTabs>
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
