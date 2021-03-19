import {createRouter, createWebHistory} from "vue-router";
import Login from "../views/Login.vue";
import store from "@/store"

const routes = [{path: "/", redirect: "/home"},
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            guestOnly: true
        }
    },
    {
        path: "/register",
        name: "Register",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "register" */ "../views/Register.vue"),
        meta: {
            guestOnly: true
        }
    }, {
        path: "/home",
        name: "Home",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "home" */ "../views/Home.vue"),
        meta: {
            requireAuth: true
        }
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),

    routes,
});
router.beforeEach((to, from, next) => {
    if (to.matched.some((record) => record.meta.requireAuth)) {
        if (store.getters.isAuthenticated) {
            next();
            return;
        }
        next("/login");
    } else if (to.matched.some((record) => record.meta.guestOnly)) {
        if (!store.getters.isAuthenticated) {
            next();
            return;
        }
        next("/home");
    } else {
        next();
    }
})
export default router;
