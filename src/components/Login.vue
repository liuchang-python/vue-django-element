<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <div class="grid-content bg-purple">&nbsp;</div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">
                    <el-form ref="form" :model="user" label-width="80px">
                        <el-form-item label="姓名">
                            <el-input v-model="user.name"><i slot="prefix" class="el-icon-user"></i></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input v-model="user.password"><i slot="prefix" class="el-icon-lock"></i></el-input>
                        </el-form-item>
                    </el-form>
                </div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">&nbsp;</div>
            </el-col>
        </el-row>
        <el-button type="primary" @click="login_in">登录</el-button>


    </div>
</template>

<script>
export default {
    name: "Login",
    data(){
        return {
            user:{},
        }
    },
    methods:{
        login_in(){
            if (this.user.name && this.user.password) {
                let params = new URLSearchParams();
                params.append('name', this.user.name);
                params.append('password', this.user.password);
                this.$axios({
                    url: 'http://127.0.0.1:8000/user/login/',
                    method: 'post',
                    data: params,
                }).then(res=>{
                    console.log('成功');
                    this.$router.push('/users')
                }).catch(error=>{
                    console.log(error,'add')
                })
            } else {
                console.log('error')
            }
        }
    }
}
</script>

<style scoped>

</style>
