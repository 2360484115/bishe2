<template>
<div class="card content">
    <div class="card-body">
        <div class="mb-3">
          <label for="writepost" class="form-label">编辑</label>
         <textarea  v-model="content" class="form-control" id="writepost" rows="3"></textarea>
         <button @click="post_post" type="button" class="btn btn-primary btn-sm">发帖</button>
         <button @click="clear" type="button" class="btn btn-primary btn-sm">清空</button>
        </div>
    </div>
</div>

</template>


<script>
import {ref} from "vue";
import $ from'jquery';
import { useStore } from 'vuex';
export default{
    name:"UserProfileWrite",
    
    setup(props,context){
        const content=ref('');
    const store=useStore();
        const post_post=()=>{

            $.ajax({
                url:"https://app165.acapp.acwing.com.cn/myspace/post/",
                type:"post",
                headers: {
                'Authorization': "Bearer " + store.state.user.access,
                },
                data:{
                    content:content.value,
                },
                success(resp){
                    if(resp.result==="success")
                    {
                        context.emit("post_post",content.value);
                        content.value="";
                    }

                }
            })
           
        }

        const clear=()=>{
            context.emit("clear");
        }
        return {
            post_post,
            content,
            clear,
        }
    }
}

</script>


<style scoped>
   .content{
    margin-top: 20px;
   }

   button{
    margin-top: 10px;
    margin-right: 10px;
   }

</style>