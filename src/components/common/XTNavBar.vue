<script setup>
import 'element-plus/theme-chalk/dark/css-vars.css';
import 'element-plus/theme-chalk/dark/css-vars.css';
import { useDark, useToggle } from '@vueuse/core';
import { ElMenu, ElMenuItem, ElButton, ElSwitch } from 'element-plus';
import { Search, Sunny, Moon } from '@element-plus/icons-vue';
import XTLogo from './XTLogo.vue';

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>

<template>
    <ElMenu mode="horizontal" :ellipsis="false" :router="true">
        <ElMenuItem index="/" class="ml-3">
            <XTLogo></XTLogo>
        </ElMenuItem>
        <div class="flex-grow"></div>
        <div class="menu-container">
            <ElButton round :icon="Search">&nbsp;&nbsp;&nbsp;搜索…&nbsp;&nbsp;&nbsp;</ElButton>
            &nbsp;&nbsp;&nbsp;
        </div>
        <ElMenuItem index="/admin" class="ml-5">&nbsp;管理后台&nbsp;</ElMenuItem>
        <ElMenuItem index="/contact" class="ml-5">&nbsp;联系作者&nbsp;</ElMenuItem>
        <div class="menu-container">
            &nbsp;&nbsp;&nbsp;
            <ElSwitch class="mr-5" :model-value="isDark" @click="toggleDark()" :active-icon="Moon" :inactive-icon="Sunny"
                inline-prompt></ElSwitch>
            &nbsp;&nbsp;&nbsp;
        </div>
    </ElMenu>
</template>

<style scoped>
.flex-grow {
    flex-grow: 1;
}

.menu-container {
    display: flex;
    align-items: center;
    margin-bottom: 0;
}
</style>
