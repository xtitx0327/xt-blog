<script setup>
import { ElCarousel, ElCarouselItem, ElDescriptions, ElDescriptionsItem, ElText, ElIcon, ElImage } from 'element-plus';
import { OfficeBuilding, Iphone, Message, ChatRound } from '@element-plus/icons-vue';
import BasePage from './BasePage.vue';

defineProps(['title']);
</script>

<template>
	<BasePage title="联系我" :show-header="true" :show-sidebar="true">
		<ElCarousel type="card">
			<ElCarouselItem v-for="item in 6" :key="item">
				<ElImage :src="'./public/' + item.toString() + '.jpg'"></ElImage>
			</ElCarouselItem>
		</ElCarousel>

		<ElDescriptions :column="1" size="large" :border="true" style="margin-top: 25px; ">
			<ElDescriptionsItem>
				<template #label>
					<div class="label-container">
						<ElIcon>
							<Iphone />
						</ElIcon>
						&nbsp;&nbsp;电话/微信&nbsp;&nbsp;&nbsp;<ElText size="small">Telephone/WeChat</ElText>
					</div>
				</template>
				13532803974
			</ElDescriptionsItem>
			<ElDescriptionsItem>
				<template #label>
					<div class="label-container">
						<ElIcon>
							<ChatRound />
						</ElIcon>
						&nbsp;&nbsp;QQ 号&nbsp;&nbsp;&nbsp;<ElText size="small">QQ Number</ElText>
					</div>
				</template>
				1012361559
			</ElDescriptionsItem>
			<ElDescriptionsItem label="邮箱&nbsp;&nbsp;&nbsp;Email">
				<template #label>
					<div class="label-container">
						<ElIcon>
							<Message />
						</ElIcon>
						&nbsp;&nbsp;电子邮箱&nbsp;&nbsp;&nbsp;<ElText size="small">Email</ElText>
					</div>
				</template>
				<a href="mailto:xtitx327@gmail.com">xtitx327@gmail.com</a>
				<br />
				<a href="mailto:qingbo114@foxmail.com">qingbo114@foxmail.com</a>
			</ElDescriptionsItem>
			<ElDescriptionsItem label="地址&nbsp;&nbsp;&nbsp;Address">
				<template #label>
					<div class="label-container">
						<ElIcon>
							<OfficeBuilding />
						</ElIcon>
						&nbsp;&nbsp;地址&nbsp;&nbsp;&nbsp;<ElText size="small">Address</ElText>
					</div>
				</template>
				浙江省杭州市西湖区余杭塘路 866 号浙江大学紫金港校区
				<br />
				<ElText size="small">
					Zhejiang University Zijingang Campus, No. 866 Yuhangtang Road, Xihu District, Hangzhou City, Zhejiang Province
				</ElText>
			</ElDescriptionsItem>
		</ElDescriptions>
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
