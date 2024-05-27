<template>
    <div class="card">
        <div class="card-body">
            <div class="row">
    <div class="col-3 img-filed">
      <img class="img-fluid" src="https://cdn.acwing.com/media/user/profile/photo/373951_lg_7d087f6872.jpg" alt="" v-if="user.id===9551">
      <img class="img-fluid" :src="user.photo" alt="" v-else>
    </div>
    <div class="col-9">
        <div class="name">{{user.username }}</div>
        <div class="fans">粉丝: {{ user.followerCount}}</div>
        <div>
            <button @click="follow"  v-if="user.is_followed===false">+关注</button>
            <button  @click="unfollow" v-if="user.is_followed">取消关注</button>
        </div>
    </div>
</div>
        </div>
    </div>

</template>

<script>
  import $ from 'jquery';
  import { useStore } from 'vuex';
  export default{
    name:"UserProfileInfo",
    props:{
        user:{
            type:Object,
            required:true,
        },
    },

    setup(props,context){

       const store=useStore();
        const follow=()=>{
          $.ajax({
            url:"https://app165.acapp.acwing.com.cn/myspace/follow/",
            type:"POST",
            headers: {
        'Authorization': "Bearer " + store.state.user.access,
         },
         data:{
          target_id:props.user.id,
         },
         success(resp){
          if(resp.result==="success")
              context.emit("follow1");
         }

          })
            
           
        }

        const unfollow=()=>{

          $.ajax({
            url:"https://app165.acapp.acwing.com.cn/myspace/follow/",
            type:"POST",
            headers: {
        'Authorization': "Bearer " + store.state.user.access,
         },
         data:{
          target_id:props.user.id,
         },
         success(resp){
          if(resp.result==="success")
              context.emit("unfollow1");
         }

          })
           
        }
        return{
            follow,
            unfollow,
           
        }

    }


  }

</script>


<style scoped>
  .name{
    font-weight: 700;
  }
  .fans{
    font-size: 12px;
    color:gray;
  }
  button{
    padding:2px 4px;
    font-size:12px;
  }

  img{
    border-radius: 50%;
  }
  .img-filed{
    display:flex;
    align-items: center;
  }
    
</style>