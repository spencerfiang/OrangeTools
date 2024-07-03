<template>
    <div>
    <div class="content">
            <el-dialog title="上传中" :visible.sync="dialogTableVisible"
                       :show-close="false"
                       :close-on-press-escape="false"
                       :append-to-body="true"
                       :close-on-click-modal="false"
                       :center="true">
                <el-progress :percentage="percentage"></el-progress>
            <span slot="footer">请耐心等待</span>
            </el-dialog>

        <!-- 原始图像上传 -->
        <el-card class="box-card">
         <div class="image-container">
            <div class="demo-image__preview">

                <div v-loading="loadingOriginal"
                     element-loading-text="上传图片中"
                     element-loading-spinner="el-icon-loading">
                    <el-image
                        :src="url_1" class="image_1"
                        :preview-src-list="srcList"
                        style="border-radius: 3px 3px 0 0">
                        <div slot="error">
                            <div slot="placeholder" class="error">
                                <el-button v-show="showbuttonOriginal"
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

            <!-- 自定义风格图片上传 -->
            <div class="demo-image__preview">
                <div v-loading="loadingStyle"
                     element-loading-text="上传自定义风格图片中"
                     element-loading-spinner="el-icon-loading">
                    <el-image
                        :src="url_3" class="image_1"
                        :preview-src-list="srcList2"
                        style="border-radius: 3px 3px 0 0">
                        <div slot="error">
                            <div slot="placeholder" class="error">
                                <el-button v-show="showbuttonStyle"
                                           type="primary" plain
                                           icon="el-icon-upload"
                                           class="download_bt orange-button"
                                           v-on:click="true_upload2">
                                    上传图像<input ref="upload2" style="display: none"
                                                   name="style_file" type="file" @change="updateStyle"/>
                                </el-button>
                            </div>
                        </div>
                    </el-image>
                </div>
                <div class="img_info_1" style="border-radius: 0 0 5px 5px">
                    <span style="color: white; letter-spacing: 4px">自定义风格图片</span>
                </div>
            </div>

            <div class="demo-image__preview">
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
            </div>

            <div class="training-controls">

            <el-button type="primary" icon="el-icon-upload"
                       plain
                       class="download-button orange-button" @click="resetData">
                重新选择图像
            </el-button>

                <!-- 输入文本框 -->
                <el-input v-model.number="trainingCount" placeholder="请输入训练次数" class="training-input"></el-input>
                <el-input v-model="learningRate" placeholder="请输入学习度" class="training-input" type="text" @input="validateDecimal($event)" step="0.01"></el-input>

            <!--开始训练-->
            <el-button type="primary" icon="el-icon-upload"
                       plain
                       class="download-button orange-button" @click="startTraining">
                开始训练
            </el-button>

            </div>
        </el-card>
    </div>

    <div class="demo-image__placeholder">
        <el-divider></el-divider>
        <el-card>
            <div slot="header" class="clearfix">
                <span>效果呈现</span>
            </div>
                <div class="image-container">
                    <img src="./01.jpg" alt="Image 1" class="image-item">
                    <img src="./02.jpg" alt="Image 2" class="image-item">
                    <img src="./03.jpg" alt="Image 3" class="image-item">
                 </div>
        </el-card>
    </div>

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
            url_1: "", url_2: "",url_3: "",
            srcList: [], srcList1: [],srcList2: [],
            url: "",
            visible: false,
            wait_return: "等待上传", wait_upload: "等待上传",
            loading: false,
            loadingOriginal: false,
            loadingStyle: false,
            showbuttonOriginal: true,
            showbuttonStyle: true,
            percentage: 0,
            fullscreenLoading: false,
            dialogTableVisible: false,
            param: new FormData(),
            trainingCount: null, // 新增
            learningRate: null // 新增
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

        update(e) {
            this.percentage = 0;
            this.dialogTableVisible = true;
            this.url_1 = "";
            this.srcList = [];
            this.wait_return = "";
            this.wait_upload = "";
            this.fullscreenLoading = true;
            this.loadingOriginal = true;
            this.showbuttonOriginal = false;

            let file = e.target.files[0];
            this.url_1 = this.$options.methods.getObjectURL(file);

            this.param.append("content_file", file, file.name); // 修改此行

            var timer = setInterval(() => {
                this.myFunc();
            }, 30);

            setTimeout(() => {
                this.percentage = 100;
                clearInterval(timer);

                this.srcList.push(this.url_1);

                this.fullscreenLoading = false;
                this.loadingOriginal = false;  // 修改
                this.dialogTableVisible = false;
                this.percentage = 0;

            }, 1000);
        },

        updateStyle(e) {
            this.percentage = 0;
            this.dialogTableVisible = true;
            this.url_3 = "";
            this.srcList2 = [];
            this.wait_return = "";
            this.wait_upload = "";
            this.fullscreenLoading = true;
            this.loadingStyle = true;  // 修改
            this.showbuttonStyle = false;

            let file = e.target.files[0];
            this.url_3 = this.$options.methods.getObjectURL(file);

            this.param.append("style_file", file, file.name); // 修改此行

            var timer = setInterval(() => {
                this.myFunc();
            }, 30);

            setTimeout(() => {
                this.percentage = 100;
                clearInterval(timer);

                this.srcList2.push(this.url_3);

                this.fullscreenLoading = false;
                this.loadingStyle = false;  // 修改
                this.dialogTableVisible = false;
                this.percentage = 0;
                //this.notice1();
            }, 1000);
        },

        myFunc() {
            if (this.percentage + 33 < 99) {
                this.percentage = this.percentage + 33;
            } else {
                this.percentage = 99;
            }
        },

        //开始训练方法
        startTraining() {
            this.percentage = 0;
            this.dialogTableVisible = true;
            this.url_2 = "";
            this.srcList1 = [];
            this.wait_return = "";
            this.wait_upload = "";
            this.fullscreenLoading = true;
            this.loading = true;

            var timer = setInterval(() => {
                this.myFunc();
            }, 30);

            console.log( this.trainingCount,this.learningRate)
            // 将训练次数和学习率添加到 FormData 对象
            this.param.append("training_count",this.trainingCount);
            this.param.append("learning_rate",this.learningRate);
            // 打印FormData对象的内容
            for (let pair of this.param.entries()) {
                console.log(pair[0] + ': ' + pair[1]);
            }

            let config = {
                headers: { "Content-Type": "multipart/form-data" },
            };

            axios.post(this.server_url + `/upload/50`, this.param, config)
                .then((response) => {
                    this.percentage = 100;
                    clearInterval(timer);

                    this.url_2 = response.data.draw_url;
                    console.log(this.url_2)
                    this.srcList1.push(this.url_2);

                    this.fullscreenLoading = false;
                    this.loading = false;
                    this.dialogTableVisible = false;
                    this.percentage = 0;
                    this.notice1();
                });
    },

        validateDecimal(event) {
            const value = event.target.value;
            const regex = /^\d*\.?\d*$/;
            if (!regex.test(value)) {
                event.target.value = value.slice(0, -1);
            } else {
                this.learningRate = value;
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
        //检查
      console.log('mounted - $refs:', this.$refs);
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

.image-container {
  display: flex;
  justify-content: space-between;
}

.demo-image__preview {
width: 250px;
  height: 290px;
  margin: 20px 60px;

  display: flex;
  flex-direction: column;
  align-items: center;
    background-color: #ffe4c4;
}

.error {
  margin: 100px auto;
  width: 50%;
  padding: 10px;
  text-align: center;
}

.el-button.orange-button {
    margin-left: 10px;
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

.image-container {
  display: flex;
  justify-content: flex-start;
}

.image-item {
  width: 350px;
  height: 400px; /* 如果需要高度相同 */
  object-fit: cover; /* 确保图像适应容器 */
  margin-right: 10px; /* 设置图片之间的间距 */
}

.image-item:last-child {
  margin-right: 0; /* 去掉最后一个图片的右边距 */
}

.training-controls {
    display: flex;
    align-items: center;
    margin-top: 20px;
    padding: 10px;
}

.training-input {
    width: 200px;
    margin-left: 10px;
    background-color: #FFE4C4; /* 淡橙色 */
    border-radius: 5px;
}

</style>

