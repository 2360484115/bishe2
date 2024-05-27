<template>
  <NavBar></NavBar>
  <!-- <ContentBase></ContentBase> -->
 <div class="total">
  <div class="container container1  d-flex align-items-center justify-content-center">
    <div class="card" style="width: 22rem;">
      <div class="card-body content">
        <!-- 头像部分 -->
        <div class="text-center mb-4">
          <img src="https://cdn.acwing.com/media/user/profile/photo/373951_lg_7d087f6872.jpg" class="rounded-circle" alt="Avatar" style="width: 100px; height: 100px; border: 3px solid #dee2e6; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        </div>
        <h3 class="card-title text-center mb-4">运动员管理平台</h3>
        <form @submit.prevent="register">
          <!-- 表单内容 -->
          <div class="form-group">
            <input  type="text" class="form-control" id="username" placeholder="账号" required v-model="loginForm.username">
          </div>
          <div class="form-group">
            <input type="password" class="form-control" id="password" placeholder="密码" required v-model="loginForm.password">
          </div>
          <div class="form-group">
            <input type="password_confirm" class="form-control" id="password_confirm" placeholder="确认密码" required v-model="password_confirm">
          </div>
          <div class="error_message">{{ error_message }}</div>
          <div class="form-group">
            <button @click="register"  type="submit" class="btn btn-primary btn-block">注册</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</template>



  
  <script>
  // @ is an alias to /src
 //import ContentBase from "../components/ContentBase";
  import NavBar from "../components/NavBar.vue";
  import { useRouter } from 'vue-router';
  import {ref} from "vue";
  import { useStore } from 'vuex';
    import $ from 'jquery';
 
  export default {
    name: 'RegisterView',
    components: {
      NavBar,
    },
    setup() {
      const store=useStore();
      console.log(store);
    
      let error_message=ref('');
      let password_confirm=ref('');
      const router = useRouter();
     console.log(router) ;
      const loginForm = ref({
        username: '',
        password: '',
      });

    const register = () => {
         $.ajax({
            url:"https://app165.acapp.acwing.com.cn/myspace/user/",
            type:"POST",
            data:{
            username: loginForm.value.username,
            password:loginForm.value.password,
            password_confirm:password_confirm.value,
            },
            success(resp){
              if(resp.result==="success")
              {
                store.dispatch("login",{
                    username:loginForm.value.username,
                    password:loginForm.value.password,
                    success(){
                    
                      router.push({ name: 'home' });
                    },
                    error(){
                      error_message.value="系统异常，请稍后重试";
                    },
                });
              }
              else{
                error_message.value=resp.result;
              }
                   
            }
         })
    };

    return {
      loginForm,
      error_message,
      password_confirm,
      register,
    };
    },
  }
  
  </script>
  
  
  <style scoped>
 
  .container1{
    /* margin-top: 20px; */
    height: 700px;
    width: 100%;
    /* background-image: url(https://ts1.cn.mm.bing.net/th/id/R-C.2e3b7963246988626f612c68da967ef3?rik=r0kA9RSUlZy5lg&riu=http%3a%2f%2fpic.bizhi360.com%2fbbpic%2f7%2f5107.jpg&ehk=pSGpjEh26hXBnGYeC8JfVYwClUg2ZpuJ0vFGLxw5L94%3d&risl=&pid=ImgRaw&r=0);
    background-repeat: no-repeat;
    background-size: cover; */
  }
  .total{
    height: 700px;
    width: 100%;
    background-image: url(https://ts1.cn.mm.bing.net/th/id/R-C.2e3b7963246988626f612c68da967ef3?rik=r0kA9RSUlZy5lg&riu=http%3a%2f%2fpic.bizhi360.com%2fbbpic%2f7%2f5107.jpg&ehk=pSGpjEh26hXBnGYeC8JfVYwClUg2ZpuJ0vFGLxw5L94%3d&risl=&pid=ImgRaw&r=0);
    background-repeat: no-repeat;
    background-size: cover;
  }

  .form-group{
    margin-bottom: 5px;
  }
  button{
    margin-top: 5px;
  }
  .error_message{
    color:red;
  }

  </style>
  