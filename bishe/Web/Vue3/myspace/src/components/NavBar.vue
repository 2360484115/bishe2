<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary bgc">
  <div class="container">
    <router-link class="navbar-brand" :to="{name:'home'}" active-class="active-link" v-if="$store.state.user.is_login">Myspace</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link active"  :to="{name:'home'}" active-class="active-link" v-if="$store.state.user.is_login">首页</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'highorder'}" active-class="active-link" v-if="$store.state.user.is_login">高阶数据与建议</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'statistical'}" active-class="active-link" v-if="$store.state.user.is_login">运动周报</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'sportsdata'}" active-class="active-link" v-if="$store.state.user.is_login">实时运动数据</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'charts'}" active-class="active-link" v-if="$store.state.user.is_login">实时数据图表</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'history'}" active-class="active-link" v-if="$store.state.user.is_login">历史数据图表</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'map'}" active-class="active-link" v-if="$store.state.user.is_login">地图</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'userlist'}" active-class="active-link" v-if="$store.state.user.is_login">好友列表</router-link>
        </li>
        <li class="nav-item" v-if="$store.state.user.is_login">
          <router-link class="nav-link" :to="{name:'userprofile',params:{userId:$store.state.user.id}}" active-class="active-link">用户动态</router-link>
        </li>
      </ul>
      <ul class="navbar-nav " v-if="!$store.state.user.is_login">
        <li class="nav-item">
          <router-link class="nav-link active" :to="{name:'login'}" active-class="active-link">登录</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'register'}" active-class="active-link">注册</router-link>
        </li>
      </ul>
      <ul class="navbar-nav " v-else>
        <li class="nav-item">
          <router-link class="nav-link active" :to="{name:'userprofile',params:{userId: $store.state.user.id}}" active-class="active-link">
            {{ $store.state.user.username }}
           <img  class="img-fluid" src="https://cdn.acwing.com/media/user/profile/photo/373951_lg_7d087f6872.jpg" alt="">
          </router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'login'}" active-class="active-link"><span @click="logout">退出</span></router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
import { useStore } from 'vuex';
   export default{
    name:"NavBar",
     
    setup(){
      const store=useStore();
      const logout=()=>{
           store.commit("logout");
    }
    return{
      logout,
    }
  },
    
   }
</script>



<style scoped>
.active-link {
  font-weight: bold;
}
.navbar {
  /* background-color: #4b5320; 保留橄榄绿背景色 */
  box-shadow: 0 2px 4px rgba(0,0,0,.1); /* 保留轻微的阴影 */
}


.navbar-brand, .nav-link {
  color: #000 !important; /* 字体颜色改为黑色 */
}

.nav-link:hover {
  color: blue !important; /* 悬停时改为白色字体，以增加对比度 */
}

.navbar-toggler {
  border-color: #000; /* 切换按钮边框颜色，与黑色文字颜色一致 */
}

.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'><path stroke='rgba(0, 0, 0, 1)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/></svg>"); /* 维持切换图标为黑色 */
}
.img-fluid {
  max-height: 40px; /* 或任何适合你需求的值 */
  max-width: 100%; /* 确保图片宽度不超过其容器宽度 */
  height: auto; /* 保持图片的原始宽高比 */
  border-radius: 50%;
}
.navbar-nav {
  display: flex;
  align-items: center; /* 添加这行 */
}

</style>

