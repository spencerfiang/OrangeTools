<template>
  <div class="layout">
      <el-container>
          <div class="sidebar-container"><!--Aside-->
                <el-menu mode="vertical"
                        :default-active="this.$route.path" router
                         :router="true"
                         active-text-colo="ffd04b"
                         class="sidebar">

                    <el-menu-item index="/">数字图像处理平台</el-menu-item>
                    <!-- index要绑定路由上的path   -->
                    <el-menu-item index="/upload/50">自定义风格迁移</el-menu-item>
                    <el-menu-item index="/upload/51">风格转换-Candy</el-menu-item>
                    <el-menu-item index="/upload/52">风格转换-The Starry Night</el-menu-item>
                    <el-menu-item index="/upload/53">风格转换-Composition VII</el-menu-item>
                    <el-menu-item index="/upload/54">风格转换-La Muse</el-menu-item>
                    <el-menu-item index="/upload/55">风格转换-Mosaic</el-menu-item>
                    <el-menu-item index="/upload/56">风格转换-かながわおきなみうら</el-menu-item>
                    <el-menu-item index="/upload/57">风格转换-Udnie</el-menu-item>
                    <el-menu-item index="/upload/58">风格转换-The Scream</el-menu-item>
                    <el-menu-item index="/upload/59">风格转换-Feathers</el-menu-item>
                    <el-menu-item index="/upload/0">添加椒盐噪声</el-menu-item>
                    <el-menu-item index="/upload/1">均值平滑</el-menu-item>
                    <el-menu-item index="/upload/2">中值平滑</el-menu-item>
                    <el-menu-item index="/upload/3">高斯平滑</el-menu-item>
                    <el-menu-item index="/upload/4">图像锐化-拉普拉斯算子</el-menu-item>
                    <el-menu-item index="/upload/5">图像锐化-Sobel算子水平方向</el-menu-item>
                    <el-menu-item index="/upload/6">图像锐化-Sobel算子垂直方向</el-menu-item>
                    <el-menu-item index="/upload/7">双线性插值法扩大图像</el-menu-item>
                    <el-menu-item index="/upload/8">左移30个像素，下移50个像素</el-menu-item>
                    <el-menu-item index="/upload/9">旋转45度，缩放因子为1</el-menu-item>
                    <el-menu-item index="/upload/10">转灰度图</el-menu-item>
                    <el-menu-item index="/upload/11">转灰度后二值化-全局阈值法</el-menu-item>
                    <el-menu-item index="/upload/12">直方图均衡化</el-menu-item>
                    <el-menu-item index="/upload/13">灰度直方图</el-menu-item>
                    <el-menu-item index="/upload/14">仿射变换</el-menu-item>
                    <el-menu-item index="/upload/15">透视变换</el-menu-item>
                    <el-menu-item index="/upload/16">图像翻转</el-menu-item>
                    <el-menu-item index="/upload/17">rgb转hsv</el-menu-item>
                    <el-menu-item index="/upload/18">hsv获取h</el-menu-item>
                    <el-menu-item index="/upload/19">hsv获取s</el-menu-item>
                    <el-menu-item index="/upload/20">hsv获取v</el-menu-item>
                    <el-menu-item index="/upload/21">rgb获取b</el-menu-item>
                    <el-menu-item index="/upload/22">rgb获取g</el-menu-item>
                    <el-menu-item index="/upload/23">rgb获取r</el-menu-item>
                    <el-menu-item index="/upload/24">水平翻转</el-menu-item>
                    <el-menu-item index="/upload/25">垂直翻转</el-menu-item>
                    <el-menu-item index="/upload/26">对角镜像</el-menu-item>
                    <el-menu-item index="/upload/27">图像开运算</el-menu-item>
                    <el-menu-item index="/upload/28">图像闭运算</el-menu-item>
                    <el-menu-item index="/upload/29">腐蚀</el-menu-item>
                    <el-menu-item index="/upload/30">膨胀</el-menu-item>
                    <el-menu-item index="/upload/31">顶帽运算</el-menu-item>
                    <el-menu-item index="/upload/32">底帽运算</el-menu-item>
                    <el-menu-item index="/upload/33">houghLinesP实现线条检测</el-menu-item>
                    <el-menu-item index="/upload/34">canny边缘检测</el-menu-item>
                    <el-menu-item index="/upload/35">图像增强</el-menu-item>
                    <el-menu-item index="/upload/36">Roberts算子提取图像边缘</el-menu-item>
                    <el-menu-item index="/upload/37">Prewitt 算子提取图像边缘</el-menu-item>
                    <el-menu-item index="/upload/38">Laplacian算子提取图像边缘</el-menu-item>
                    <el-menu-item index="/upload/39">LoG边缘提取</el-menu-item>

                </el-menu>
            </div><!-- 侧边栏 -->
          <el-container>
              <el-header class="header">
                  <app-header />
              </el-header>
              <el-main>
                  <div>
                      <router-view name="default" />
                      <router-view name="footer" />
                  </div>
              </el-main>
          </el-container>

        </el-container>

  </div>
</template>

<script>

import Header from "./Header.vue";

export default {
    name: 'Layout',
    components: {
        'app-header':Header,
    },
    data() {},
}
</script>

<style scoped>
.layout {
    display: flex;
}

.sidebar-container {
    width: 250px;
    background-color: #FFA07A; /* 主色调 蓝绿色 */
}

.sidebar {
    background-color: #FFA07A; /* 主色调 蓝绿色 */
    color: #ffffff; /* 白色文字 */
}

.sidebar .el-menu-item {
    background-color: #FFA07A; /* 主色调 蓝绿色 */
    color: #ffffff; /* 白色文字 */
}

.sidebar .el-menu-item:hover {
    /*background-color: #ff6f61; /* 辅助色调 浅蓝绿色 */
    background-color: #FF7F50; /* 辅助色调 浅蓝绿色 */
}

.sidebar .el-menu-item.is-active {
    background-color: #ff6347; /* 辅助色调 深蓝绿色 */
}

.header {
    background-color: #FFA07A; /* 主色调 蓝绿色 */
    color: #ff6347; /* 白色文字 */
    font-weight: bold; /* 文字加粗 */
}

.el-main {
    background-color: #faf0e6; /* 浅黄色背景 */
    padding: 20px;
}
</style>
