<template>
    <div class="demo-image__placeholder">
        <el-divider />
        <el-card>
             <div slot="header" class="clearfix">
            <span>效果呈现</span></div>
        <el-image :src="src0" style="width: 550px;margin-right: 10px"></el-image>
        <el-image :src="src" style="width: 550px"></el-image>
        </el-card>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "prepic",
    props: ['id'],

    data() {
        return {
            src0: require('../../public/img/default.jpg'),
            src: require('../../public/img/'+this.$route.params.id+'.jpg')
        };
    },
    created: function () {
    },

    methods: {
  },
  mounted() {},
};
</script>

<style>
.el-card {
    background-color: #ffdab9;
    border-radius: 8px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.el-card__header {
    background-color: #FF7F50; /* 浅蓝绿色 */
    color: white;
    border-bottom: 1px solid #FF4500; /* 蓝绿色 */
}
</style>

