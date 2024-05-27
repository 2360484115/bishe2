<template>

<div class="digital-twin-intro py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6">
          <h2>数字孪生技术介绍</h2>
          <p>数字孪生技术通过创建一个完整的数字镜像来模拟真实世界的运动员和训练环境，使教练和运动员能够以前所未有的方式分析和优化训练效果。</p>
          <ul class="custom-list">
            <li>实时数据分析</li>
            <li>训练效果预测</li>
            <li>伤病预防</li>
          </ul>
         <a href="https://zhuanlan.zhihu.com/p/99249900" class="btn btn-primary" target="_blank" rel="noopener noreferrer">了解更多</a>
          
        </div>
        <div class="col-md-6 ">
            <img src="../images/digitaltwins.jpg" alt="Digital Twin Technology" class="img-fluid">
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
    name:"DigitalTwins",
    
}
</script>

<style scoped>
.digital-twin-intro {
  background-color: #f0f2f5;
  color: #333;
}
img{
    width: 560px;
}
ul {
  list-style: none ;/* 移除默认的列表样式 */
  padding-left: 0; /* 移除默认的左填充 */ 
  
}


ul li {
  background-color: lightblue; /* 为每个列表项添加浅绿色背景，增加视觉吸引力 */
  margin-bottom: 10px; /* 列表项之间的间距 */
  padding: 10px 15px; /* 内边距 */
  border-radius: 5px; /* 圆角边框 */
  position: relative; /* 为伪元素定位 */
  transition: all 0.3s ease; /* 平滑过渡效果 */ 
 
}



ul li:hover {
  background-color: #d7ebc6; /* 悬停时改变背景色 */
}
</style>