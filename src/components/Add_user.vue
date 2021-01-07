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
                        <el-form-item label="二次密码">
                            <el-input v-model="user.re_pwd"><i slot="prefix" class="el-icon-sunny"></i></el-input>
                        </el-form-item>
                        <el-form-item label="电话">
                            <el-input v-model="user.phone"><i slot="prefix" class="el-icon-map-location"></i></el-input>
                        </el-form-item>
                    </el-form>

                </div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">&nbsp;</div>
            </el-col>

        </el-row>

        <el-button type="primary" @click="added">添加</el-button>


    </div>

</template>

<script>
export default {
    name: "Add_user",
    data() {
        return {
            user: {
                name: '',
                password: '',
                // age: '',
                // address: '',
                // birth:'',
                re_pwd:'',
                phone:'',
            }
        }
    },
    methods: {

        added() {
            // if (this.user.name && this.user.password && this.user.age && this.user.address) {
            if (this.user.name && this.user.password === this.user.re_pwd && this.user.phone) {
                let params = new URLSearchParams();
                params.append('name', this.user.name);
                params.append('password', this.user.password);
                // params.append('age', this.user.age);
                // params.append('address', this.user.address);
                params.append('re_pwd', this.user.re_pwd);
                params.append('phone', this.user.phone);
                this.$axios({
                    // url: 'http://127.0.0.1:8000/user/the_users/',
                    url: 'http://127.0.0.1:8000/app/stu/',
                    method: 'post',
                    data: params,
                    // JSON.stringify({
                    //     username: this.user.username,
                    //     password: this.user.password,
                    //     age: this.user.age,
                    //     // age:1,
                    //     address: this.user.address,
                    // })
                }).then(res=>{
                    console.log('成功')
                }).catch(error=>{
                    console.log(error,'add')
                })
            } else {
                console.log('error')
            }
        },

    }
}
</script>

<style scoped>

</style>
