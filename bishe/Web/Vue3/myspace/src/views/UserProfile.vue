<template>

   <NavBar/>
    <ContentBase>
  <div class="row">
    <div class="col-3">
      <UserProfileInfo @follow1="follow" @unfollow1="unfollow" :user="user">
      </UserProfileInfo>
      <UserProfileWrite v-if="is_me" @post_post="post_post" @clear="clear" >
         
      </UserProfileWrite>

    </div>
    <div class="col-9">
       <UserProfilePosts :user="user" :posts="posts" @delete_post="delete_post">
           
       </UserProfilePosts>
    </div>
  </div>

    </ContentBase>
  </template>
  
  <script>
  // @ is an alias to /src
  
  import ContentBase from "../components/ContentBase";
  import UserProfileInfo from "../components/UserProfileInfo";
  import UserProfilePosts from "../components/UserProfilePosts";
  import UserProfileWrite from "../components/UserProfileWrite";
  import NavBar from "../components/NavBar.vue";
  import { reactive } from "vue";
  import{useRoute} from 'vue-router';
  import $ from 'jquery';
  import { useStore } from 'vuex';
  import { computed } from "vue";
  export default {
    name: 'UserProfile',
    components: {
      ContentBase,
      UserProfileInfo,
      UserProfilePosts,
      UserProfileWrite,
      NavBar,
    },
      setup(){
        const store=useStore();
        const route = useRoute();
        const userId = parseInt(route.params.userId);
        
         const user=reactive({
         })
         const posts=reactive({
         })

         $.ajax({
          url:"https://app165.acapp.acwing.com.cn/myspace/getinfo/",
          type:"get",
          data:{
            user_id:userId,
          },
          headers: {
        'Authorization': "Bearer " + store.state.user.access,
         },
         success(resp){
          user.id = resp.id;
          user.username = resp.username;
          user.photo = resp.photo;
         user.followerCount = resp.followerCount;
           if(user.id===store.state.user.id)
           {
            user.is_followed=false;
           }
           else
          user.is_followed = resp.is_followed;
         },
        

        })

        $.ajax({
          url:"https://app165.acapp.acwing.com.cn/myspace/post/",
          type:"get",
          data:{
            user_id:userId,
          },
          headers: {
        'Authorization': "Bearer " + store.state.user.access,
         },
         success(resp){
          posts.count=resp.length;
            posts.posts=resp;
         }
        })

         

        const follow=()=>{
            if(user.isfollow===true)
            {
                 return;
            }
            if(user.id!==store.state.user.id)
           {
            user.followerCount++;
            user.is_followed=true;
           } 

         }

         const unfollow=()=>{
                if(user.is_followed===false)
                return;
              user.followerCount--;
              user.is_followed=false;
         }

         const post_post=(content)=>{
                 posts.count++;
                 posts.posts.unshift({
                  id:posts.count,
                  userId:1,
                  content:content,
                 })
         }

         const delete_post=(post_id)=>{

             posts.posts=posts.posts.filter(post=> post.id!==post_id);
             posts.count=posts.posts.length;
         }

         const clear=()=>{
            posts.count=0;
            posts.posts=[];
         }

         const is_me=computed(()=>userId===store.state.user.id);

         return {
          user,
          follow,
          unfollow,
          posts,
          post_post,
          clear,
          is_me,
          delete_post,
         }
      }
    
  }
  </script>
  
  
  <style scoped>
  .container{
    margin-top: 20px;
  }
  </style>
  