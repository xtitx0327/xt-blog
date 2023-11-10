<script setup>
import { ElMenu, ElMenuItem, ElIcon } from 'element-plus';
import { Document, HomeFilled, Avatar, Picture, Link } from '@element-plus/icons-vue';
</script>

<template>
    <ElMenu mode="vertical" style="height: 100%;" :router="true">
        <ElMenuItem index="/">
            <template #title>
                <ElIcon>
                    <HomeFilled />
                </ElIcon>
                <span>主页</span>
            </template>
        </ElMenuItem>
        <ElMenuItem index="/contact">
            <template #title>
                <ElIcon>
                    <Avatar />
                </ElIcon>
                <span>联系我</span>
            </template>
        </ElMenuItem>
        <ElMenuItem index="/gallery">
            <template #title>
                <ElIcon>
                    <Picture></Picture>
                </ElIcon>
                <span>照片墙</span>
            </template>
        </ElMenuItem>
        <ElMenuItem index="/articles">
            <template #title>
                <ElIcon>
                    <Document />
                </ElIcon>
                <span>文章列表</span>
            </template>
        </ElMenuItem>
        <ElMenuItem index="/link">
            <template #title>
                <ElIcon>
                    <Link />
                </ElIcon>
                <span>友情链接</span>
            </template>
        </ElMenuItem>
    </ElMenu>
</template>

<style scoped></style>