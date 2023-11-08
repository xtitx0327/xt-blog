<script setup>
import { ElIcon, ElText, ElDivider, ElRow, ElCard, ElSpace } from 'element-plus';
import { EditPen, Iphone } from '@element-plus/icons-vue';
import XTBigLogo from '../common/XTBigLogo.vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage :title="title" :show-header="false" :show-sidebar="true">
		<div class="container">
			<XTBigLogo />
			<ElText
				style="font-family: Georgia, 'Times New Roman', Times, serif; font-size: 36px; margin-top: 25px; text-shadow: 1px 1px darkgray; font-weight: 600;">
				Welcome to XT's homepage
			</ElText>
		</div>
		<ElRow justify="center">
			<ElSpace size="large">
				<ElCard class="card">
					<ElText size="large">
						<ElIcon color="green">
							<EditPen />
						</ElIcon>&nbsp;关于我&nbsp;&nbsp;&nbsp;<ElText size="small">Introdction</ElText>
					</ElText>
					<ElDivider style="margin: 12px 0;" />
					<ElText>
						关于我的基本介绍。<br />
						<ElText size="small">See my basic introduction here.</ElText>
					</ElText>
				</ElCard>
				<ElCard class="card">
					<ElText size="large">
						<ElIcon color="green">
							<Iphone />
						</ElIcon>&nbsp;联系我&nbsp;&nbsp;&nbsp;<ElText size="small">Contact</ElText>
					</ElText>
					<ElDivider style="margin: 12px 0;" />
					<ElText>
						通过电话或邮件等方式与我沟通。<br />
						<ElText size="small">Contact me through phone, email, etc.</ElText>
					</ElText>
				</ElCard>
				<ElCard class="card">
					<ElText size="large">
						<ElIcon color="green">
							<EditPen />
						</ElIcon>&nbsp;了解我&nbsp;&nbsp;&nbsp;<ElText size="small">Reading</ElText>
					</ElText>
					<ElDivider style="margin: 12px 0;" />
					<ElText>
						来看看我写的文章吧。<br />
						<ElText size="small">Intrested in my articles?</ElText>
					</ElText>
				</ElCard>
			</ElSpace>
		</ElRow>
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
