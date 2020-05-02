<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
  >
    <el-menu-item index="1">首页</el-menu-item>
    <el-submenu index="2">
      <template slot="title">其他</template>
      <el-menu-item index="2-1">项目介绍</el-menu-item>
      <!-- <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
      <el-menu-item index="2-4-3">选项3</el-menu-item>-->
      <!-- </el-submenu> -->
    </el-submenu>
    <el-menu-item index="3" disabled>禁用</el-menu-item>
    <el-menu-item index="4">
      <a href="https://github.com/sunlanchang" target="_blank">关于作者</a>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: "navigator",
  data() {
    return {
      activeIndex: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<style>
</style>