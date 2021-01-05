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
                            <el-input v-model="user.username"><i slot="prefix" class="el-icon-user"></i></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input v-model="user.password"><i slot="prefix" class="el-icon-lock"></i></el-input>
                        </el-form-item>
                        <el-form-item label="年龄">
                            <el-input v-model="user.age"><i slot="prefix" class="el-icon-sunny"></i></el-input>
                        </el-form-item>
                        <el-form-item label="地址">
                            <el-input v-model="user.address"><i slot="prefix" class="el-icon-map-location"></i></el-input>
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
                username: '',
                password: '',
                age: '',
                address: '',
                // birth:'',
            }
        }
    },
    methods: {
        added() {
            if (this.user.username && this.user.password && this.user.age && this.user.address) {
                this.$axios({
                    url: 'http://127.0.0.1:8000/user/add_user/',
                    method: 'get',
                    params: {
                        username: this.user.username,
                        password: this.user.password,
                        age: this.user.age,
                        address: this.user.address,
                    }
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
