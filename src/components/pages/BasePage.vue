<script setup>
import { ElHeader, ElMain, ElAside, ElFooter, ElContainer, ElPageHeader } from 'element-plus';
import { ArrowLeft } from '@element-plus/icons-vue';
import XTNavBar from '../common/XTNavBar.vue';
import XTSideBar from '../common/XTSideBar.vue';
import XTFooter from '../common/XTFooter.vue';

const props = defineProps(['title', 'showHeader', 'showSidebar', 'mainNoPadding']);
</script>

<template>
	<ElContainer style="height: 100vh;">
		<ElHeader>
			<XTNavBar />
		</ElHeader>

		<ElContainer>
			<ElAside v-if="showSidebar">
				<XTSideBar/>
			</ElAside>

			<ElMain :style="{paddingTop: props.mainNoPadding ? '0' : 'auto', paddingBottom: props.mainNoPadding ? '0' : 'auto'}">
				<ElPageHeader :icon="ArrowLeft" title="返回上一页" v-if="showHeader" style="margin-bottom: 15px;" @click="$router.back">
					<template #content>
						<span> {{ title }} </span>
					</template>
				</ElPageHeader>
                <slot></slot>
			</ElMain>
		</ElContainer>

		<ElFooter>
			<XTFooter />
		</ElFooter>
	</ElContainer>
</template>

<style scoped>
</style>
