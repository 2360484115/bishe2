<template>
    <link href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" rel="stylesheet">
     <NavBar />
 
     <ContentBase>
        <div class="test">
            <div class="header-text">
                <p>请输入日期范围以查询历史数据帧。</p>
             </div>
            <div class="input-container">
            <div class="input-section">
                <flat-pickr v-model="startDate" :config="dateConfig" placeholder="Start Date (yyyy-mm-dd HH:mm:ss)"></flat-pickr>
                <flat-pickr v-model="endDate" :config="dateConfig" placeholder="End Date (yyyy-mm-dd HH:mm:ss)"></flat-pickr>
                <button @click="fetchData">查询</button>
            </div>
            </div>
        
 
            <div class="charts" style="width: 50%; margin: auto; padding: 20px 0;">
                <h3 class="chart-title"><i class="fas fa-tachometer-alt"></i> Acc(m/s^2)三个方向的历史数据帧</h3>
                <div ref="AccChart" style="height:270px;"></div>
                <h3 class="chart-title"><i class="fas fa-drafting-compass"></i> As(°/s)三个方向的历史数据帧</h3>
                <div ref="AsChart" style="height:270px;"></div>
                <h3 class="chart-title"><i class="fas fa-compass"></i> Ang(°)三个方向的历史数据帧</h3>
                <div ref="AngChart" style="height:270px;"></div>
            </div>
        </div>
       
     </ContentBase>
 
 </template>
 
 <script>
 import { ref , onMounted ,onUnmounted} from 'vue';
 import $ from 'jquery';
 import NavBar from "../components/NavBar.vue";
 import ContentBase from "../components/ContentBase";
 import 'echarts/lib/chart/line';
 import * as echarts from 'echarts';
 import 'flatpickr/dist/flatpickr.css';
import FlatPickr from 'vue-flatpickr-component';
 
 export default {
   components: {
     NavBar,
     ContentBase,
     FlatPickr
   },
   setup() {
     const startDate = ref('');
     const endDate = ref('');
     const dateConfig = {
      enableTime: true,
      enableSeconds:true,
      dateFormat: "Y-m-d H:i:S",
      time_24hr: true,
      minuteIncrement:1,
    };
     const data = ref([]);
     const AccChart = ref(null);
     const AsChart=ref(null);
     const AngChart=ref(null);
     const chartInstance1 = ref(null);
     const chartInstance2 = ref(null);
     const chartInstance3 = ref(null);
     function initChartAcc() {
         chartInstance1.value = echarts.init(AccChart.value);
         chartInstance1.value.setOption({
             tooltip: {trigger: 'item',},
             legend: {
             data: ['AccX', 'AccY', 'AccZ']
         },
             
             xAxis: { type: 'category', data: [] ,axisLabel: {
                 interval: 0,  // 显示所有标签
                 rotate: 45,   // 标签旋转45度
             }},
             yAxis: { type: 'value' },
             dataZoom: [
           {   // 这个dataZoom组件，默认控制x轴。
               type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
               start: 10,      // 左边在 10% 的位置。
               end: 60         // 右边在 60% 的位置。
           }
         ],
             series: [
             { name: 'AccX', type: 'line', data: [], color: '#ff0000' },
             { name: 'AccY', type: 'line', data: [], color: '#00ff00' },
             { name: 'AccZ', type: 'line', data: [], color: '#0000ff' }
         ]
         });
      }
      function initChartAs() {
         chartInstance2.value = echarts.init(AsChart.value);
         chartInstance2.value.setOption({
             tooltip: {trigger: 'item',},
             legend: {
             data: ['AsX', 'AsY', 'AsZ']
         },
             xAxis: { type: 'category', data: [] ,axisLabel: {
                 interval: 0,  // 显示所有标签
                 rotate: 45,   // 标签旋转45度
             }},
             yAxis: { type: 'value' },
             dataZoom: [
           {   // 这个dataZoom组件，默认控制x轴。
               type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
               start: 10,      // 左边在 10% 的位置。
               end: 60         // 右边在 60% 的位置。
           }
         ],
             series: [
             { name: 'AsX', type: 'line', data: [], color: '#ff0000' },
             { name: 'AsY', type: 'line', data: [], color: '#00ff00' },
             { name: 'AsZ', type: 'line', data: [], color: '#0000ff' }
         ]
         });
         }
     function initChartAng() {
     chartInstance3.value = echarts.init(AngChart.value);
     chartInstance3.value.setOption({
         tooltip: {trigger: 'item',},
         legend: {
         data: ['AngX', 'AngY', 'AngZ']
     },
         xAxis: { type: 'category', data: [] ,axisLabel: {
             interval: 0,  // 显示所有标签
             rotate: 45,   // 标签旋转45度
         }},
         yAxis: { type: 'value' },
         dataZoom: [
           {   // 这个dataZoom组件，默认控制x轴。
               type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
               start: 10,      // 左边在 10% 的位置。
               end: 60         // 右边在 60% 的位置。
           }
         ],
         series: [
         { name: 'AngX', type: 'line', data: [], color: '#ff0000' },
         { name: 'AngY', type: 'line', data: [], color: '#00ff00' },
         { name: 'AngZ', type: 'line', data: [], color: '#0000ff' }
     ]
     });
     }
 
 
     function fetchData() {
       $.ajax({
         url: 'http://localhost:3000/history',
         type: 'GET',
         data: {
           start: startDate.value,
           end: endDate.value
         },
         success: function(response) {
           data.value = response;
           if(response.length>20)
           {
             const sampledData = response.filter((_, i) => i % 3 === 0);  // 每10个数据点取一个
             const xAxisData = sampledData.map((_, index) => `${index}`);
             const seriesDataX = sampledData.map(item => item.accx*9.8);
             const seriesDataY = sampledData.map(item => item.accy *9.8);
             const seriesDataZ = sampledData.map(item => item.accz *9.8);
             const seriesDataASX = sampledData.map(item => item.asx);
             const seriesDataASY = sampledData.map(item => item.asy );
             const seriesDataASZ = sampledData.map(item => item.asz );
             const seriesDataAngX = sampledData.map(item => item.angx);
             const seriesDataAngY = sampledData.map(item => item.angy );
             const seriesDataAngZ = sampledData.map(item => item.angz );
             console.log(seriesDataAngZ);
             chartInstance1.value.setOption({
                     xAxis: [{ data: xAxisData }],
                     series: [
                         { name: 'AccX', type: 'line', data: seriesDataX },
                         { name: 'AccY', type: 'line', data: seriesDataY },
                         { name: 'AccZ', type: 'line', data: seriesDataZ }
                     ]
                 });
             chartInstance2.value.setOption({
                 xAxis: [{ data: xAxisData }],
                 series: [
                     { name: 'AsX', type: 'line', data: seriesDataASX },
                     { name: 'AsY', type: 'line', data: seriesDataASY },
                     { name: 'AsZ', type: 'line', data: seriesDataASZ }
                 ]
             });
            chartInstance3.value.setOption({
                 xAxis: [{ data: xAxisData }],
                 series: [
                     { name: 'AngX', type: 'line', data: seriesDataAngX },
                     { name: 'AngY', type: 'line', data: seriesDataAngY },
                     { name: 'AngZ', type: 'line', data: seriesDataAngZ }
                 ]
             });
 
           }
         },
         error: function(error) {
           console.error('Error fetching data:', error);
         }
       });
     }
     onMounted(() => {
         
         initChartAcc();
         initChartAs();
         initChartAng();
         // 在组件卸载时清除定时器
         onUnmounted(() => {
            
             if (chartInstance1.value != null) {
             chartInstance1.value.dispose();
         }
             
             if (chartInstance2.value != null) {
                 chartInstance2.value.dispose();
             }
             if (chartInstance3.value != null) {
                 chartInstance3.value.dispose();
             }
         });
         });
 
     return {
        dateConfig,
       startDate,
       endDate,
       data,
       fetchData,
       AccChart,
       AsChart,
       AngChart,
     };
   }
 };
 </script>
 
 <style scoped>
 .header-text {
    text-align: center;
    margin-top: 20px;
    font-size: 30px;
    color: #555;
}
 
 .input-container{
   
    margin: 0 auto;
    display: flex;
  justify-content: center;  /* Center horizontally */
 }
 .input-section {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    
}

.input-section > button {
    padding: 10px 20px;
    background-color: #007bff;
    border: none;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

.input-section > button:hover {
    background-color: #0056b3;
}
.charts {
    /* 图表容器的额外样式 */
    padding: 20px;
    background-color: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    
}

.chart-title {
    text-align: center;
    font-size: 18px;
    color: #333;
    margin-bottom: 10px;
}
.charts div{
    margin-bottom: 100px;
}

/* 可以添加媒体查询来进一步优化响应式布局 */
@media (max-width: 768px) {
    .charts {
        width: 100%; /* 在小屏幕设备上全宽 */
    }
}


 </style>