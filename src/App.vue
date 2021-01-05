<template>
    <div id="app">

        <el-container>
            <el-header>
                <span>管理系统</span>
                <router-link to="/users">角色列表</router-link>
                <router-link to="/add">添加角色</router-link>
            </el-header>
            <el-container>
                <el-main>
                    <router-view  v-if="isRouterAlive" :isShow="isShow"></router-view>
                </el-main>
            </el-container>
            <el-footer>Footer</el-footer>
        </el-container>

    </div>
</template>

<script>
export default {
    name: 'App',
    provide () {
        return {
            reload: this.reload
        }
    },
    data() {
        return {
            isRouterAlive: true,
            isShow: true
        }

    },
    methods: {
        reload: function () {
            this.isRouterAlive = false;
            this.$nextTick(function () {
                this.isRouterAlive = true;
                this.isShow = false;
            })
        },
    }

}
</script>

<style>
.el-header, .el-footer {
    background: linear-gradient(to right, #FF9900, #FFFFCC, #FF9900);
    color: #333;
    text-align: center;
    line-height: 60px;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
}

.el-main {
    background: linear-gradient(to left, #FFFFFF, #CCFFFF, #CCCCFF);
    color: #333;
    text-align: center;
    line-height: 60px;
}

body > .el-container {
    margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}
</style>
