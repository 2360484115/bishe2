<template>
     <link href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" rel="stylesheet">
    <NavBar>
        
    </NavBar>
    <ContentBase>
       
    </ContentBase>

    <div class="charts" style="width: 50%; margin: auto; padding: 20px 0;">
      <h3 class="chart-title"><i class="fas fa-tachometer-alt"></i> Acc(m/s^2)三个方向的15个实时数据帧</h3>
      <div ref="AccxChart" style="height:270px;"></div>
      <h3 class="chart-title"><i class="fas fa-tachometer-alt"></i> Acc(m/s^2)模值的15个实时数据帧</h3>
      <div ref="AccChart" style="height:270px;"></div>
      <h3 class="chart-title"><i class="fas fa-drafting-compass"></i> As(°/s)三个方向的15个实时数据帧</h3>
      <div ref="AsChart" style="height:270px;"></div>
      <h3 class="chart-title"><i class="fas fa-compass"></i> Ang(°)三个方向的15个实时数据帧</h3>
      <div ref="AngChart" style="height:270px;"></div>
    </div>
</template>






<script>
import NavBar from "../components/NavBar.vue";
import ContentBase from "../components/ContentBase";
import { ref , onMounted ,onUnmounted} from 'vue';
import 'echarts/lib/chart/bar';
import 'echarts/lib/chart/line';
import 'echarts/lib/chart/pie';
import * as echarts from 'echarts';
import $ from 'jquery'; 
export default {
    name:"SportsCharts",
    components: {
      ContentBase,
      NavBar,
    },

    setup(){
        const AsChart = ref(null);
        const AccChart = ref(null);
        const AccxChart = ref(null);
        const AngChart = ref(null);
        const chartInstance1 = ref(null);
        const chartInstance2 = ref(null);
        const chartInstance3 = ref(null);
        const chartInstance4 = ref(null);
        function initChartAccx() {
        chartInstance1.value = echarts.init(AccxChart.value);
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
            series: [
            { name: 'AccX', type: 'line', data: [], color: '#ff0000' },
            { name: 'AccY', type: 'line', data: [], color: '#00ff00' },
            { name: 'AccZ', type: 'line', data: [], color: '#0000ff' }
        ]
        });
        }

        function initChartAcc() {
        chartInstance2.value = echarts.init(AccChart.value);
        chartInstance2.value.setOption({
            tooltip: { trigger: 'axis',axisPointer: {
                type: 'cross',
                label: {
                backgroundColor: '#6a7985'
                }
            } },
            xAxis: { type: 'category', data: [] ,axisLabel: {
                interval: 0,  // 显示所有标签
                rotate: 45,   // 标签旋转45度
            }},
            yAxis: { type: 'value',
             scale: true,  // 开启刻度自动缩放
            splitNumber: 10,  // 增加刻度数量，使得间隔更小
           
        },
            series: [
            { type: 'line', data: [], color: '#ff0000' },
           
        ]
        });
        }

        function initChartAs() {
        chartInstance3.value = echarts.init(AsChart.value);
        chartInstance3.value.setOption({
            tooltip: {trigger: 'item',},
            legend: {
            data: ['AsX', 'AsY', 'AsZ']
        },
            xAxis: { type: 'category', data: [] ,axisLabel: {
                interval: 0,  // 显示所有标签
                rotate: 45,   // 标签旋转45度
            }},
            yAxis: { type: 'value' },
            series: [
            { name: 'AsX', type: 'line', data: [], color: '#ff0000' },
            { name: 'AsY', type: 'line', data: [], color: '#00ff00' },
            { name: 'AsZ', type: 'line', data: [], color: '#0000ff' }
        ]
        });
        }

        function initChartAng() {
        chartInstance4.value = echarts.init(AngChart.value);
        chartInstance4.value.setOption({
            tooltip: { trigger: 'axis',axisPointer: {
                type: 'cross',
                label: {
                backgroundColor: '#6a7985'
                }
            } },
            legend: {
            data: ['AngX', 'AngY', 'AngZ']
        },
            xAxis: { type: 'category', data: [] ,axisLabel: {
                interval: 0,  // 显示所有标签
                rotate: 45,   // 标签旋转45度
            }},
            yAxis: { type: 'value' },
            series: [
            { name: 'AngX', type: 'line', data: [], color: '#ff0000' },
            { name: 'AngY', type: 'line', data: [], color: '#00ff00' },
            { name: 'AngZ', type: 'line', data: [], color: '#0000ff' }
        ]
        });
        }

        
        
        const temperature = ref('36.5°C');
        // 加速度
        
        function loadData() {
        $.ajax({
            url: 'http://localhost:3000/data',  // 后端服务的URL
            type: 'GET',
            success: function(data) {
            //console.log(data[data.length-1]);
            console.log(data[2]);
            if (data.length > 0) {
                const xAxisData = data.map((_, index) => `Time${index}`).reverse();
                const seriesDataX = data.map(item => item.accx*9.8).reverse();
                const seriesDataY = data.map(item => item.accy *9.8).reverse();
                const seriesDataZ = data.map(item => item.accz *9.8).reverse();
                const seriesDataMagnitude = data.map(item => 
                    Math.sqrt(
                        Math.pow(item.accx * 9.8, 2) + 
                        Math.pow(item.accy * 9.8, 2) + 
                        Math.pow(item.accz * 9.8, 2)
                    )
                ).reverse();
                const seriesDataASX = data.map(item => item.asx).reverse();
                const seriesDataASY = data.map(item => item.asy ).reverse();
                const seriesDataASZ = data.map(item => item.asz ).reverse();
                const seriesDataAngX = data.map(item => item.angx).reverse();
                const seriesDataAngY = data.map(item => item.angy ).reverse();
                const seriesDataAngZ = data.map(item => item.angz ).reverse();
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
                        { type: 'line', data: seriesDataMagnitude },
                    ]
                });
                chartInstance3.value.setOption({
                    xAxis: [{ data: xAxisData }],
                    series: [
                        { name: 'AsX', type: 'line', data: seriesDataASX },
                        { name: 'AsY', type: 'line', data: seriesDataASY },
                        { name: 'AsZ', type: 'line', data: seriesDataASZ }
                    ]
                });
                chartInstance4.value.setOption({
                    xAxis: [{ data: xAxisData }],
                    series: [
                        { name: 'AngX', type: 'line', data: seriesDataAngX },
                        { name: 'AngY', type: 'line', data: seriesDataAngY },
                        { name: 'AngZ', type: 'line', data: seriesDataAngZ }
                    ]
                });
           
            


            }
            
            //console.log(1);
            },
            error: function(error) {
            console.error('Error:', error);
            }
        });
        }

       

//
        



        onMounted(() => {
        loadData();  // 首次加载数据
        initChartAccx();
        initChartAcc();
        initChartAs();
        initChartAng();
        const intervalId = setInterval(loadData, 1300);  // 每1秒刷新一次数据
        
        // 在组件卸载时清除定时器
        onUnmounted(() => {
            clearInterval(intervalId);
            if (chartInstance1.value != null) {
            chartInstance1.value.dispose();
        }
        if (chartInstance2.value != null) {
            chartInstance2.value.dispose();
        }
        if (chartInstance3.value != null) {
            chartInstance3.value.dispose();
        }
        if (chartInstance4.value != null) {
            chartInstance4.value.dispose();
        }
            
        });
        });
            
        return{AccxChart,temperature,AccChart,AsChart,AngChart};
    },



}

</script>



<style scoped>
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
div{
    margin-bottom: 50px;
}

/* 可以添加媒体查询来进一步优化响应式布局 */
@media (max-width: 768px) {
    .charts {
        width: 100%; /* 在小屏幕设备上全宽 */
    }
}
</style>
