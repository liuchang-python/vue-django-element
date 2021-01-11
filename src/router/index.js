import Vue from 'vue'
import Router from 'vue-router'
import User_list from "../components/User_list";
import Detail from "../components/Detail";
import Alter_user from "../components/Alter_user";
import Add_user from "../components/Add_user";
import Login from "../components/Login";

Vue.use(Router)

export default new Router({
  routes: [
      {path:'/users',component:User_list},
      {path:'/detail/:id',component:Detail},
      {path:'/alter/:id',component:Alter_user},
      {path:'/add',component:Add_user},
      {path:'/login',component:Login},

      {path:'/',redirect:'/users'},
      {path:'/*',redirect:'/users'},

  ]
})
