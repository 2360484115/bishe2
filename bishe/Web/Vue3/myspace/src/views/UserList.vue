<template>
      <NavBar></NavBar>
      <ContentBase>
        <div class="card" v-for="user in users" :key="user.id" @click="openprofile(user.id)">
          <div class="card-body">
            <div class="row">
              <div class="col-1">
                <img class="img-fluid" :src="user.photo" alt="">
              </div>
              <div class="col-11">
                <div class="username">{{ user.username }}</div>
                <div class="fans-count">{{ user.followerCount }}</div>
              </div>
            </div>
          </div>
        </div>
      </ContentBase>
</template>



<script>
  import ContentBase from "../components/ContentBase";
  import NavBar from "../components/NavBar.vue";
  import $ from 'jquery';
  import {ref} from 'vue';
  import { useRouter } from 'vue-router';
  import { useStore } from 'vuex';
      export default{
        name:"UserList",
        components: {
        ContentBase,
        NavBar,
    },

    setup(){
           const router = useRouter();
           const store= useStore();
           let users=ref([]);
           $.ajax({
            url:'https://app165.acapp.acwing.com.cn/myspace/userlist/',
            type:"get",
             success(resp){
                users.value=resp;
             }
           })

           const openprofile=(userId)=>{
                    if(store.state.user.is_login){
                      router.push({ name: 'userprofile',params:{userId:userId } });
                    }
                    else{
                      router.push({name: 'login'});
                    }
           }
       


           return{
                users,
                openprofile,
           };
        
    }

    




}
    

</script>




<style scoped>

 img{
  border-radius: 50%;
 }

 .username{
  height: 50%;
  font-weight: bold;
 }

 .fans-count{
  height: 50%;
  font-size: 12px;
  color: gray;
 }

 .card{
  margin-bottom: 20px;
  cursor: pointer;
 }

 .card:hover{
  box-shadow: 2px 2px 10px lightgrey;
  transition: 300ms;
 }


</style>