<template>

    <div>
        <el-container>
            <el-table :data="user" border style="width: 100%">
                <el-table-column prop="id" label="ID" width="80"></el-table-column>
                <el-table-column prop="username" label="姓名" width="120"></el-table-column>
                <el-table-column prop="password" label="密码" width="100"></el-table-column>
                <el-table-column prop="birth" label="生日" width="100"></el-table-column>
                <el-table-column prop="address" label="地址"></el-table-column>
                <el-table-column label="操作" width="380">
                    <el-button @click="$router.go(-1)" size="small" type="primary" icon="el-icon-back">返回上一页</el-button>
                </el-table-column>
            </el-table>
        </el-container>

    </div>

</template>

<script>
export default {
    name: "Detail",
    data() {
        return {
            user: [],
        }
    },
    methods: {},
    created() {
        let user_id = this.$route.params.id
        this.$axios({
            url: 'http://127.0.0.1:8000/user/the_users/'+user_id+'/',
            method: 'get',
            params: {
                // id: user_id,
            }
        }).then(res => {
            console.log(res.data.res);
            this.user = [res.data.res];
        }).catch(error => {
            console.log(error, 'get')
        })
    }
}
</script>

<style scoped>

</style>
