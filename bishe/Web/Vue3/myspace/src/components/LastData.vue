<template>
   <link href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" rel="stylesheet">
   <div class="container mt-3">
    <div class="row">
      <!-- 高阶数据部分 -->
      <div class="col-md-5 mb-3">
        <h2>过去三天高阶的数据</h2>
        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">走路的时长</h5>
            <p class="card-text"><i class="fas fa-walking"></i>{{ walktime  }}</p>
          </div>
        </div>
        
        
        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">跑步的时长</h5>
            <p class="card-text"><i class="fas fa-running"></i>{{ runtime }}</p>
          </div>
        </div>
        
       
        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">运球的时长</h5>
            <p class="card-text"><i class="fas fa-basketball-ball"></i>{{ Dribbletime }}</p>
          </div>
        </div>

        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">上篮的次数</h5>
            <p class="card-text"><i class="fas fa-arrow-right"></i>{{ Layuptheshot }}</p>
          </div>
        </div>
        
        <div class="card card-custom">
          <div class="card-body">
            <h5 class="card-title">投篮的次数</h5>
            <p class="card-text"><i class="fas fa-arrow-up"></i>{{ Fieldgoal }}</p>
          </div>
        </div>

      </div>

      <!-- 建议部分 -->
      <div class="col-md-7">
        <!-- 运动建议卡片 -->
        <div class="card card-custom mb-3 " style="margin-top: 50px;">
            <div class="position">
                <div class="card-body custom1">
                <h5 class="card-title">运动建议:</h5>
                <p class="card-text">{{ advice }}</p>
                </div>
            </div>
          
        </div>
        
        <!-- 教程推荐卡片 --> 
        <div class="card card-custom mb-3 " style="margin-top: 100px">
          <div class="card-body custom1">
            <h5 class="card-title">教程推荐</h5>
            <ul>
              <li v-for="tutorial in tutorials" :key="tutorial.id">
                <a :href="tutorial.url" target="_blank">{{ tutorial.title }}</a>
              </li>
            </ul>
          </div>
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import {ref} from "vue";
export default {
   name:"LastData",
   setup() {
    const walktime = ref('10h');
    const runtime = ref('5h');
    const Dribbletime = ref('1h');
    const Fieldgoal = ref(50);
    const Layuptheshot=ref(100);
    const advice = ref("基于您过去三天的运动数据，我们建议您增加跑步时间，以提升心肺功能。");
    const tutorials = ref([
      { id: 1, title: "如何提高跑步耐力", url: "https://www.bilibili.com/video/BV1SZ42187A3/?spm_id_from=333.337.search-card.all.click" },
      { id: 2, title: "篮球基础运球技巧", url: "https://www.bilibili.com/video/BV1Hr4y1r7VQ/?spm_id_from=333.337.search-card.all.click" },
      { id: 3, title: "提高篮球投篮准确性的练习", url: "https://www.bilibili.com/video/BV1GS4y1D7rM/?spm_id_from=333.337.search-card.all.click" }
    ]);

    return { walktime , runtime, Dribbletime,  Fieldgoal, Layuptheshot,advice,tutorials};
  }
}
</script>
   
<style scoped>
.card-custom {
  background: linear-gradient(135deg, #6e8efb, #a777e3);
  color: #fff;
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px; /* 为卡片之间添加一些间距 */
  border-radius: 10px; /* 更圆润的边角 */
}

/* 卡片标题样式 */
.card-custom .card-title {
  font-size: 1.2rem; /* 调整字体大小 */
}

/* 卡片文本样式 */
.card-custom .card-text {
  font-size: 1.2rem; /* 增大字体大小 */
  font-weight: bold; /* 字体加粗 */
  display: flex;
  align-items: center;
}

/* 图标样式 */
.card-custom .card-text i {
  font-size: 2rem; /* 图标大小 */
  margin-right: 10px; /* 图标与文字间的距离 */
}

.custom1{
    background: linear-gradient(135deg, #FFA07A, #E9967A);
    border-radius: 10px; 
}

</style>