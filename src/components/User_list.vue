<template>

    <div>

        <el-container>
            <el-table :data="user_list" border style="width: 100%">
                <el-table-column prop="id" label="ID" width="80"></el-table-column>
                <el-table-column prop="name" label="姓名" width="120"></el-table-column>
                <el-table-column prop="password" label="密码" width="100"></el-table-column>
                <el-table-column prop="gender" label="性别" width="100"></el-table-column>
                <el-table-column prop="phone" label="电话"></el-table-column>


                <el-table-column label="操作" width="380">
                    <template slot-scope="scope">
                        <el-row>
                            <el-button type="success" size="small" icon="el-icon-plus" @click="$router.push('/add')"> 添加</el-button>

                            <el-popconfirm @confirm="del_user(scope.row.id)"
                                           confirm-button-text='确定'
                                           cancel-button-text='不用了'
                                           icon="el-icon-info"
                                           icon-color="red"
                                           title="确定删除此用户吗？"

                            >
                                <el-button type="danger" size="small" icon="el-icon-delete-solid" slot="reference"> 删除
                                </el-button>
                            </el-popconfirm>

                            <el-button type="warning" size="small" icon="el-icon-edit"
                                       @click="alter_user(scope.row.id)"> 修改
                            </el-button>
                            <el-button @click="handleClick(scope.row.id)" type="primary" size="small"
                                       icon="el-icon-view"> 查看
                            </el-button>

                        </el-row>
                    </template>
                </el-table-column>
            </el-table>
        </el-container>
    </div>

</template>

<script>
export default {
    name: "User_list",

    data() {
        return {
            user_list: [],
            pic:'',
        }
    },
    methods: {
        alter_user(id) {
            this.$router.push("/alter/" + id)
        },
        handleClick(id) {
            this.$router.push("/detail/" + id)
        },
        del_user(id) {
            this.$axios({
                // url: 'http://127.0.0.1:8000/user/del_user/',
                // url: 'http://127.0.0.1:8000/app/stu/'+id+'/',
                url: 'http://127.0.0.1:8000/user/users/'+id+'/',
                // method: 'get',
                method: 'delete',
                params: {
                    // id: id,
                },
            }).then(res => {
                console.log(res);
                this.$router.go(0);
            }).catch(error => {
                console.log(error, 'user')
            })

        },
    },
    created() {
        this.$axios({
            // url: 'http://127.0.0.1:8000/user/the_users/',
            // url: 'http://127.0.0.1:8000/app/stu/',
            url: 'http://127.0.0.1:8000/user/users/',
            method: 'get',
        }).then(res => {
            console.log(res.data);
            this.user_list = res.data;
        }).catch(error => {
            console.log(error, '11');
        })
    }
}
</script>

<style scoped>
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
