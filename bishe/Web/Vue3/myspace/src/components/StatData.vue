<template>
  <link href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" rel="stylesheet">
   <div class="dashboard">
    <div class="sidebar">
      <div class="health-tips">
        <h2>周报分析</h2>
        <p>根据您过去七日的运动步数,我们建议您每天至少走10,000步</p>
        <p>根据您过去七日的平均心率,我们建议您适当加强心肺功能</p>
        <p>根据您过去七日的卡路里消耗,我们建议您选择游泳这项运动</p>
      </div>
      <div class="trend-analysis">
        <h2>趋势分析</h2>
        <p>您的平均心率在过去一周有所下降，这是一个好现象。</p>
        <p>您的步数在过去一周呈现总体上升趋势，请继续保持。</p>
        <p>从卡路里的消耗来看，您的运动种类多样，请继续保持</p>
      </div>
    </div>
    <div class="charts">
      <h3 class="chart-title"><i class="fas fa-walking"></i>运动步数</h3>
      <div ref="stepsChart" style="width: 100%;height:270px;"></div>
      <h3 class="chart-title"><i class="fas fa-heartbeat"></i>24h平均心率</h3>
      <div ref="heartRateChart" style="width: 100%;height:270px;margin-top:20px;"></div>
      <h3 class="chart-title"><i class="fas fa-fire"></i>卡路里消耗</h3>
      <div ref="caloriesChart" style="width: 100%;height:270px;margin-top:20px;"></div>
    </div>
  </div>


</template>

<script>


import 'echarts/lib/chart/bar';
import 'echarts/lib/chart/line';
import 'echarts/lib/chart/pie';

import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';
export default {
    name:"StatData",
    components: {
  },
  setup() {
    const stepsChart = ref(null);
    const heartRateChart = ref(null);
    const caloriesChart = ref(null);

    onMounted(() => {


      const stepsOption = {
       // title: { text: '运动步数' },
        tooltip: {
        trigger: 'item',
        // 自定义提示框内容
        formatter: function (params) {
        // params 是包含当前数据项信息的对象
        return `${params.name}<br/>步数: ${params.value}`;
        }
        },
        xAxis: {
            type: 'category',
            data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            name: '步数',
            type: 'bar',
            data: [4820, 2932, 7901, 11934, 13290, 8330, 9320],
            // 可以添加标签显示每个柱子的具体数值
            label: {
            show: true,
            position: 'top'
        }
            }]
    };


      const heartRateOption = {
       // title: { text: '整日平均心率' },
        tooltip: {trigger: 'item',},
        xAxis: { type: 'category', data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"] },
        yAxis: { type: 'value' },
        series: [{ type: 'line', data: [100, 112, 101, 84, 90, 75, 85] }]
      };

      const caloriesOption = {
       // title: { text: '卡路里消耗' },
        tooltip: {trigger: 'item',},
        series: [{ type: 'pie', radius: '55%', data: [{ value: 235, name: '跑步' }, { value: 274, name: '骑自行车' }, { value: 310, name: '游泳' }, { value: 335, name: '健身' }, { value: 400, name: '散步' }] }],
        label: {
        show: true,
        formatter: '{b}: {c} kcal ({d}%)',
      },
      };

      echarts.init(stepsChart.value).setOption(stepsOption);
      echarts.init(heartRateChart.value).setOption(heartRateOption);
      echarts.init(caloriesChart.value).setOption(caloriesOption);
    });

    return {
      stepsChart,
      heartRateChart,
      caloriesChart,
    };
  }

}
</script>

<style scoped>
.dashboard {
  display: flex;
  max-width: 1200px;
  margin: 20px auto;
  gap: 30px; /* 调整间隙以提供更多空间 */
}

.sidebar {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 30px; /* 增加卡片间的间隙 */
}

.charts {
  flex: 2;
  display: flex;
  flex-direction: column;
  gap: 20px; /* 调整图表间的间隙 */
}

/* 卡片样式 */
.health-tips, .trend-analysis {
  padding: 20px;
  background-color: #ffffff; /* 使用纯白背景色 */
  border: none; /* 去掉边框 */
  border-radius: 10px; /* 更大的圆角 */
  box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* 更柔和的阴影 */
  transition: all 0.3s ease; /* 添加过渡效果 */
}
.health-tips{
  margin-bottom: 100px;
}

.health-tips:hover, .trend-analysis:hover {
  transform: translateY(-5px); /* 鼠标悬停时轻微上移 */
  box-shadow: 0 6px 15px rgba(0,0,0,0.15); /* 阴影加深 */
}

.health-tips h2, .trend-analysis h2 {
  color: #0056b3; /* 更深的蓝色调 */
  margin-bottom: 20px; /* 增加标题下的间距 */
}

.health-tips p, .trend-analysis p {
  font-size: 1rem;
  line-height: 1.6; /* 增加行高 */
  color: #343a40; /* 深灰色文字 */
}

/* 图表容器样式 */
.charts > div {
  background-color: #f8f9fa; /* 轻微的背景色 */
  border-radius: 10px; /* 圆角 */
  overflow: hidden; /* 防止图表溢出容器 */
}
.chart-title {
  display: flex;
  align-items: center;
  font-weight: bold;
  margin-bottom: 5px;
}

.chart-title i {
  margin-right: 5px;
}
.chart-container {
  margin-top: -5px;
}

</style>
