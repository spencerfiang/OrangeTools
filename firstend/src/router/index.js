import Vue from 'vue'
import Router from 'vue-router'

import Layout from "../components/Layout.vue";
import HomePage from '@/components/HomePage.vue'; // 新增
import Upload2Show from "@/components/Upload2Show.vue";
import prepic from "@/components/prepic.vue";
Vue.use(Router)

const routess = [];

// 对应50个操作
for (let id = 0; id < 40; id++) {
      const route = {
          path: `/upload/:id`,
          components: {
              default: Upload2Show,
              footer: prepic,
          },
          props: true,
          meta: { id: id},
      };
      routess.push(route);
}

const routesss = [];

// 对应50个操作
for (let id = 51; id <= 59; id++) {
      const route = {
          path: `/upload/:id`,
          components: {
              default: Upload2Show,
              footer: prepic,
          },
          props: true,
          meta: { id: id},
      };
      routesss.push(route);
}

const routes = [
    {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },

    {
        path: '/',
        redirect:'/upload/50',
        component: Layout,
        hidden: true,
    },
    {
        path: '/upload',
        component: Layout,
        hidden: true,
        children: [
            {//TODO 还不知道为什么这个要放在上面
                path: '/upload/50',
                component: () => import("../views/styleTrain.vue"),
                name: 'styleTrain',
            },
            ...routess,
            ...routesss,
        ]
    },
];

const router = new Router({
    mode: 'history',//取消哈希模式
    routes
});

export default router;
