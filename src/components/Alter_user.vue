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
        }
    },
    created() {
        let user_id = this.$route.params.id;
        this.$axios({
            url: 'http://127.0.0.1:8000/user/get_user/',
            method: 'get',
            params: {
                id: user_id,
            }
        }).then(res => {
            console.log(1, res.data);
            this.user = {
                username: res.data.username,
                age: res.data.age,
                address: res.data.address,
                password: res.data.password,
                birth: res.data.birth,
            };
            console.log(2, this.user)
        }).catch(error => {
            console.log(error, 'get')
        })
    }
}
</script>

<style scoped>

</style>
