<template>
    <div class="content">
            <el-dialog title="生成中" :visible.sync="dialogTableVisible"
                       :show-close="false"
                       :close-on-press-escape="false"
                       :append-to-body="true"
                       :close-on-click-modal="false"
                       :center="true">
                <el-progress :percentage="percentage"></el-progress>
            <span slot="footer">请耐心等待</span>
            </el-dialog>

        <el-card class="box-card">
            <div class="demo-image__preview1">

                <div v-loading="loading"
                     element-loading-text="上传图片中"
                     element-loading-spinner="el-icon-loading">
                    <el-image
                        :src="url_1" class="image_1"
                        :preview-src-list="srcList"
                        style="border-radius: 3px 3px 0 0">
                        <div slot="error">
                            <div slot="placeholder" class="error">
                                <el-button v-show="showbutton"
                                           type="primary" plain
                                           icon="el-icon-upload"
                                           class="download_bt orange-button"
                                           v-on:click="true_upload">
                                    上传图像<input ref="upload" style="display: none"
                                                   name="content_file" type="file" @change="update"/>
                                </el-button>
                            </div>
                        </div>
                    </el-image>
                </div>
                <div class="img_info_1" style="border-radius: 0 0 5px 5px">
                    <span style="color: white; letter-spacing: 6px">原始图像</span>
                </div>
            </div>

            <div class="demo-image__preview2">
                <div v-loading="loading"
                     element-loading-text="处理中"
                     element-loading-spinner="el-icon-loading">
                    <el-image :src="url_2" class="image_1"
                              :preview-src-list="srcList1"
                              style="border-radius: 3px 3px 0 0">
                        <div slot="error">
                            <div slot="placeholder" class="error">{{ wait_return }}</div>
                        </div>
                    </el-image>
                </div>
                <div class="img_info_1" style="border-radius: 0 0 5px 5px">
                    <span style="color: white; letter-spacing: 4px">处理结果</span>
                </div>
            </div>
            <el-button type="primary" icon="el-icon-upload"
                       plain
                       class="download-button orange-button" @click="resetData">
                重新选择图像
            </el-button>
        </el-card>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Upload2Show",
    props: ['id'],

    data() {
        return {
            server_url: "http://127.0.0.1:5000",
            url_1: "", url_2: "",
            srcList: [], srcList1: [],
            url: "",
            visible: false,
            wait_return: "等待上传", wait_upload: "等待上传",
            loading: false,
            showbutton: true, percentage: 0,
            fullscreenLoading: false,
            dialogTableVisible: false,
        };
    },
    created: function () {

        this.$watch('$route.params.id',(newId, oldId) =>{
            this.resetData()
        })
        console.log(" :key=\"$route.params.id\"", this.$route.params.id)
        document.title = "Orange_TOOLS";

    },

    methods: {
        true_upload() {
            this.$refs.upload.click();
        },
        true_upload2() {
            this.$refs.upload2.click();
        },
        // 获得目标文件
        getObjectURL(file) {
            var url = null;
            if (window.createObjcectURL !== undefined) {
                url = window.createOjcectURL(file);
            } else if (window.URL !== undefined) {
                url = window.URL.createObjectURL(file);
            } else if (window.webkitURL !== undefined) {
                url = window.webkitURL.createObjectURL(file);
            }
            return url;
        },
        // 上传文件
        update(e) {
            this.percentage = 0;
            this.dialogTableVisible = true;
            this.url_1 = "";
            this.url_2 = "";
            this.srcList = [];
            this.srcList1 = [];
            this.wait_return = "";
            this.wait_upload = "";
            this.fullscreenLoading = true;
            this.loading = true;
            this.showbutton = false;
            let file = e.target.files[0];
            this.url_1 = this.$options.methods.getObjectURL(file);
            let param = new FormData(); //创建form对象
            param.append("content_file", file, file.name); //通过append向form对象添加数据
            var timer = setInterval(() => {
                this.myFunc();
            }, 30);
            let config = {
                headers: { "Content-Type": "multipart/form-data" },
            }; //添加请求头 DONE 这里获取this.id

            axios.post(this.server_url + `/upload/${this.$route.params.id}`, param, config)
                .then((response) => {
                    this.percentage = 100;
                    clearInterval(timer);
                    this.url_1 = response.data.image_url;
                    this.srcList.push(this.url_1);
                    this.url_2 = response.data.draw_url;//处理后的
                    this.srcList1.push(this.url_2);

                    this.fullscreenLoading = false;
                    this.loading = false;
                    this.dialogTableVisible = false;
                    this.percentage = 0;
                    this.notice1();
            });
        },
        myFunc() {
            if (this.percentage + 33 < 99) {
                this.percentage = this.percentage + 33;
            } else {
                this.percentage = 99;
            }
        },
        drawChart() {},
        notice1() {
            this.$notify({
                title: "处理成功",
                message: "点击图片可以查看大图",
                duration: 0,
                type: "success",
            });
        },
        resetData(){
            window.location.reload()
        },
  },
  mounted() {
    this.drawChart();
  },
};
</script>

<style>
.box-card {
  border-radius: 8px;
    background-color: #ffdab9;
}
.image_1 {
  width: 275px;
  height: 260px;
  background: #fff5ee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.img_info_1 {
  height: 30px;
  width: 275px;
  text-align: center;
  background-color: #FF7F50;
  line-height: 30px;
}
.demo-image__preview1 {
  width: 250px;
  height: 290px;
  margin: 20px 60px;
  float: left;
}

.demo-image__preview2 {
  width: 250px;
  height: 290px;

  margin: 20px 460px;
  /* background-color: green; */
}
.error {
  margin: 100px auto;
  width: 50%;
  padding: 10px;
  text-align: center;
}

.el-button.orange-button {
    background-color: #FF7F50 !important; /* 橙色 */
    border-color: #FF7F50 !important; /* 橙色边框 */
    color: white !important; /* 白色文字 */
}

.el-button.orange-button:hover {
    background-color: #FF4500 !important; /* 深橙色 */
    border-color: #FF4500 !important; /* 深橙色边框 */
}

.el-button.orange-button:focus,
.el-button.orange-button:active {
    background-color: #FFA07A !important; /* 淡橙色 */
    border-color: #FFA07A !important; /* 淡橙色边框 */
    color: #333333 !important; /* 深灰色文字 */
}


</style>

