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
                            <el-form-item label="电话">
                                <el-input v-model="user.phone"><i slot="prefix" class="el-icon-sunny"></i></el-input>
                            </el-form-item>
<!--                            <el-form-item label="">-->
<!--                                <el-input v-model="user.address"><i slot="prefix" class="el-icon-map-location"></i></el-input>-->
<!--                            </el-form-item>-->
                        </el-form>
                    </div>
                </el-col>
                <el-col :span="8">
                    <div class="grid-content bg-purple">&nbsp;</div>
                </el-col>

        </el-row>
<!--        <el-form ref="form" :model="user" label-width="80px">-->
<!--            <el-form-item label="姓名">-->
<!--                <el-input v-model="user.username"><i slot="prefix" class="el-icon-user"></i></el-input>-->
<!--            </el-form-item>-->
<!--            <el-form-item label="密码">-->
<!--                <el-input v-model="user.password"><i slot="prefix" class="el-icon-lock"></i></el-input>-->
<!--            </el-form-item>-->
<!--            <el-form-item label="年龄">-->
<!--                <el-input v-model="user.age"><i slot="prefix" class="el-icon-sunny"></i></el-input>-->
<!--            </el-form-item>-->
<!--            <el-form-item label="地址">-->
<!--                <el-input v-model="user.address"><i slot="prefix" class="el-icon-map-location"></i></el-input>-->
<!--            </el-form-item>-->
<!--        </el-form>-->
        <el-button type="primary" @click="altered">提交修改</el-button>

    </div>

</template>

<script>
export default {
    name: "Alter_user",
    data() {
        return {
            user: {},
        }
    },
    watch: {
        user() {
            console.log(this.user)
        }
    },
    methods: {
        altered() {
            console.log(this.user)
            // if (this.user.username && this.user.password && this.user.age && this.user.address) {
            if (this.user.name && this.user.password && this.user.phone) {
                let params = new URLSearchParams();
                params.append('name', this.user.name);
                params.append('password', this.user.password);
                params.append('id', this.$route.params.id);
                // params.append('address', this.user.address);
                params.append('phone', this.user.phone);
                this.$axios({
                    // url: 'http://127.0.0.1:8000/user/alter_user/',
                    url: 'http://127.0.0.1:8000/user/users/',
                    method: 'patch',
                    params: params,
                }).then(res=>{
                    console.log('成功')
                }).catch(error=>{
                    console.log(error,'add')
                })
            } else {
                console.log('error')
            }
        }
    },
    created() {
        let user_id = this.$route.params.id;
        this.$axios({
            // url: 'http://127.0.0.1:8000/user/get_user/',
            // url: 'http://127.0.0.1:8000/app/stu/'+user_id+'/',
            url: 'http://127.0.0.1:8000/user/users/'+user_id+'/',
            method: 'get',
            params: {
                // id: user_id,
            }
        }).then(res => {
            console.log(1, res.data);
            this.user = res.data;
            // this.user = {
            //     username: res.data.username,
            //     age: res.data.age,
            //     address: res.data.address,
            //     password: res.data.password,
            //     birth: res.data.birth,
            // };
            console.log(2, this.user)
        }).catch(error => {
            console.log(error, 'get')
        })
    }
}
</script>

<style scoped>

</style>
