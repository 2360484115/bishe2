<template>
     <div class="hero-section text-center bg-light p-5">
    <h1 class="display-4">引领运动科技的未来</h1>
    <p class="lead">使用数字孪生技术优化你的训练和表现</p>
    
    <a href="https://baike.baidu.com/item/%E6%95%B0%E5%AD%97%E5%AD%AA%E7%94%9F/22197545" class="btn btn-primary btn-lg" target="_blank" >查看简介</a>
    <router-link to="/sportsdata" class="btn btn-primary btn-lg position">查看实时运动数据</router-link>

  </div>
</template>

<script>
export default {
    name:"HomeGuide",

}
</script>

<style scoped>
.hero-section {
    height: 320px; /* 根据需要设置高度 */
  width: 100%; /* 根据需要设置宽度 */
  background-image: url('http://inews.gtimg.com/newsapp_bt/0/14505431984/641'); /* 替换为你的背景图片路径 */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: #ccc; /* 根据你的背景图片调整文字颜色 */
}
.lead{
    font-weight: bold;
}
a{
    margin-left: -10px;
}
.position{
    margin-left: 10px;
}

</style>