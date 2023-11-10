<script setup>
import { apiBase } from '../../config.js';
import { ref, onBeforeMount, getCurrentInstance, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { ElTabPane, ElTabs, ElLink, ElTree, ElTooltip, ElInput, ElMessage, ElMessageBox, ElForm, ElFormItem, ElButton } from 'element-plus';
import { Plus, Delete, Edit, EditPen, FolderOpened } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

let data;
let currentInstance;
const router = useRouter();

onBeforeMount(() => {
	fetch(apiBase + '/api/article/list')
		.then(response => response.json())
		.then(data => data.data)
		.then(list => {
			console.log('Data fetched', list);
			data = list;
		});
});

onMounted(() => {
	currentInstance = getCurrentInstance();
});

const editingId = ref(null);
const curInputValue = ref('');

const renameLabel = (node, id, value) => {
	if (node.id === id) {
		node.label = value;
		return;
	}
	if (!node.children)
		return;
	for (let child of node.children)
		renameLabel(child, id, value);
};

const cancelEditNode = () => {
	if (editingId.value === null)
		return;
	for (let node of data)
		renameLabel(node, editingId.value, curInputValue.value);
	console.log(editingId.value, curInputValue.value);
	fetch(apiBase + '/api/article/rename', {
		method: 'POST',
		body: JSON.stringify({
			id: editingId.value,
			title: curInputValue.value
		}),
		headers: {
			'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
			'Content-Type': 'application/json'
		}
	})
	editingId.value = null;
	curInputValue.value = '';
};

const handleNodeDoubleClick = (data) => {
	editingId.value = data.id;
	curInputValue.value = data.label;
};

const addArticle = (parentData) => {
	fetch(apiBase + '/api/article/createArticle', {
		method: 'POST',
		body: JSON.stringify({
			title: '新文章',
			parent: parentData.id
		}),
		headers: {
			'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
			'Content-Type': 'application/json'
		}
	})
		.then(response => response.json())
		.then(responseData => {
			if (responseData.code !== 200)
				ElMessage({
					message: '添加失败',
					type: 'error'
				})
			else {
				ElMessage({
					message: '添加成功',
					type: 'success'
				})
				if (parentData && parentData.children) {
					parentData.children.push({
						id: responseData.data.id,
						label: '新文章',
						type: 'article'
					});
				} else {
					data.push({
						id: responseData.data.id,
						label: '新文章',
						type: 'article'
					});
				}
			}
		})
		.catch(() => { ElMessage.error('添加失败'); });
};

const addFolder = (parentData) => {
	fetch(apiBase + '/api/article/createFolder', {
		method: 'POST',
		body: JSON.stringify({
			title: '新文件夹',
			parent: parentData.id
		}),
		headers: {
			'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
			'Content-Type': 'application/json'
		}
	})
		.then(response => response.json())
		.then(responseData => {
			if (responseData.code !== 200)
				ElMessage({
					message: '添加失败',
					type: 'error'
				})
			else {
				ElMessage({
					message: '添加成功，请刷新页面后查看',
					type: 'success'
				})
				if (parentData && parentData.children) {
					parentData.children.push({
						id: responseData.data.id,
						label: '新文件夹',
						type: 'folder',
						children: []
					});
				} else {
					data.push({
						id: responseData.data.id,
						label: '新文件夹',
						type: 'folder',
						children: []
					});
				}
			}
		})
		.catch(() => { ElMessage.error('添加失败'); });
};

const deleteNode = (node) => {
	ElMessageBox.confirm(
		'此操作是不可逆的，是否继续？',
		'警告', {
			confirmButtonText: '确认删除',
			cancelButtonText: '取消',
			type: 'warning'
		}
	)
		.then(() => {
			fetch(apiBase + '/api/article/delete', {
				method: 'POST',
				body: JSON.stringify({
					id: node.id
				}),
				headers: {
					'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
					'Content-Type': 'application/json'
				}
			})
				.then(response => response.json())
				.then(responseData => {
					if (responseData.code === 200) {
						currentInstance.ctx.$refs.dataTree.remove(node);
						ElMessage({
							message: '删除成功',
							type: 'success'
						})
					} else
						ElMessage({
							message: '删除失败',
							type: 'error'
						})
				})
				.catch(() => {
					ElMessage({
						message: '删除失败',
						type: 'error'
					})
				});
		})
};

const renameNode = (data) => {
	cancelEditNode();
	curInputValue.value = data.label;
	editingId.value = data.id;
};

const editArticle = (data) => {
	// 跳转到 /edit/:id
	router.push(`/edit/${data.id}`);
};

const updateStructure = () => {
	fetch(apiBase + '/api/article/updateSturcture', {
		method: 'POST',
		body: JSON.stringify({
			data: data
		}),
		headers: {
			'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
			'Content-Type': 'application/json'
		}
	});
};

const logout = () => {
	ElMessageBox.confirm(
		'是否退出登录？',
		'警告', {
			confirmButtonText: '确认退出',
			cancelButtonText: '取消',
			type: 'warning'
		}
	)
		.then(() => {
			window.localStorage.removeItem('token');
			router.push('/login');
		})
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
				<ElButton @click="addFolder({ id: null })">在根节点下新建文件夹</ElButton>
				<ElTree :data="data" node-key="id" :draggable="false"
					style="padding: 15px; margin: 25px; border-radius: 5px; border-style: solid; border-width: 1px; border-color: #79bbff; font-size: 16px;"
					default-expand-all ref="dataTree" @node-drop="updateStructure">
					<template #default="{ node, data }">
						<div class="article-container" @dblclick.stop="handleNodeDoubleClick(data)">
							<ElInput v-model="curInputValue" v-if="editingId === data.id" @keyup.enter="cancelEditNode()">
							</ElInput>
							<div style="margin-left: 10px;" v-else>{{ node.label }}</div>
							<div>
								<ElTooltip content="添加文章" v-if="data.type === 'folder'">
									<ElLink :underline="false" :icon="Plus" @click.stop="addArticle(data)">&nbsp;</ElLink>
								</ElTooltip>
								<ElTooltip content="添加文件夹" v-if="data.type === 'folder'">
									<ElLink :underline="false" :icon="FolderOpened" @click.stop="addFolder(data)">&nbsp;
									</ElLink>
								</ElTooltip>
								<ElTooltip :content="data.type === 'folder' ? '删除文件夹' : '删除文章'">
									<ElLink :underline="false" :icon="Delete" @click.stop="deleteNode(data)">&nbsp;</ElLink>
								</ElTooltip>
								<ElTooltip content="重命名">
									<ElLink :underline="false" :icon="Edit" @click.stop="renameNode(data)">&nbsp;</ElLink>
								</ElTooltip>
								<ElTooltip v-if="data.type === 'article'" content="编辑文章">
									<ElLink :underline="false" :icon="EditPen" @click.stop="editArticle(data)">&nbsp;
									</ElLink>
								</ElTooltip>
							</div>
						</div>
					</template>
				</ElTree>
			</ElTabPane>
			<ElTabPane label="权限信息">
				<h3>修改管理员信息</h3>
				<ElForm label-width="120px" style="max-width: 400px; margin: 25px;">
					<ElFormItem label="用户名">
						<ElInput></ElInput>
					</ElFormItem>
					<ElFormItem label="旧密码">
						<ElInput></ElInput>
					</ElFormItem>
					<ElFormItem label="新密码">
						<ElInput></ElInput>
					</ElFormItem>
					<ElFormItem label="确认密码">
						<ElInput></ElInput>
					</ElFormItem>
					<ElFormItem>
						<ElButton type="primary">提交</ElButton>
					</ElFormItem>
				</ElForm>
				<h3>退出登录</h3>
				<ElButton type="danger" @click="logout">退出登录</ElButton>
			</ElTabPane>
		</ElTabs>
	</BasePage>
</template>

<style scoped>
.article-container {
	display: flex;
	align-items: center;
	justify-content: space-between;
	flex-direction: row;
	width: 100%;
	height: 50px;
	overflow-y: visible;
}

::v-deep .el-tree-node__content {
	height: 30px;
}

a {
	text-decoration: none;
	color: #409eff;
}
</style>
