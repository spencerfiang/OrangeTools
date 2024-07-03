<!-- src/components/HomePage.vue -->
<template>
<div id="home">
  <div class="home-page">
      <h1>OrangeTools</h1>
    <h1>欢迎使用桔子图像处理网站</h1>
<!--      <h3>———满足你对图像风格迁移的所有想象</h3>-->
    <el-button type="primary" @click="goToFunctionPage">开始使用</el-button>
  </div>
    </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    goToFunctionPage() {
      this.$router.push('/upload/50'); s
    }
  },
    created() {
        document.title = "Orange_TOOLS";
    }
};
</script>

<style scoped>
#home{
    background: url("../../public/img/home2.jpg");
    width:100%;
    height:100%;
    position:fixed;
    background-size:100% 100%;
  }

.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;

}

.home-page h1 {
  color: #ff6600; /* 橙色字体 */
  font-size: 38px;
  margin-bottom: 20px;
}

.home-page h3 {
    color: #ff6347; /* 橙色字体 */
    margin-bottom: 20px;
}

.el-button {
    margin-top: 20px;
  font-size: 18px;
}
</style>
