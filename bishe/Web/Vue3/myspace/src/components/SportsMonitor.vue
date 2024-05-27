<template>
    <link href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" rel="stylesheet">
   <div class="container mt-3">
    <div class="row">
      <!-- 3D 模型部分 -->
      <div class="col-md-5 mb-3">
        <div class="button-container">
          <button @click="startMonitor"  type="button" class="btn btn-success">开始监测</button>
          <button @click="EndMonitor"  type="button" class="btn btn-danger">停止监测</button>
        </div>
        <div class="model-container">
          <iframe title="3D Model" class="model-iframe" frameborder="0"
                  allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true"
                  allow="autoplay; fullscreen; xr-spatial-tracking"
                  xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share
                  src="https://sketchfab.com/models/4b9496a7757949d7a6e7a97116789cb4/embed">
          </iframe>
        </div>
      </div>

      <!-- 数据展示部分 -->

      

      <div class="col-md-5">

        <!-- <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">当前时间</h5>
            <canvas id="canvas" width="150" height="150"></canvas>
          </div>
        </div> -->

        <!-- 心率卡片 -->
        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">心率</h5>
            <p class="card-text"><i class="fas fa-heartbeat"></i>{{ heartRate }}</p>
          </div>
        </div>
        
        <!-- 大臂与地面夹角卡片 -->
        <!-- <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">大臂与地面夹角</h5>
            <p class="card-text"><i class="fas fa-ruler-combined"></i>{{ upperArmAngle }}</p>
          </div>
        </div> -->
        
        <!-- 小臂与地面夹角卡片 -->
        <!-- <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">小臂与地面夹角</h5>
            <p class="card-text"><i class="fas fa-ruler"></i>{{ lowerArmAngle }}</p>
          </div>
        </div> -->
        
        <!-- 当前环境温度卡片 -->
        <div class="card card-custom mb-3">
          <div class="card-body">
            <h5 class="card-title">环境温度</h5>
            <p class="card-text"><i class="fas fa-thermometer-half"></i>{{ temperature }}</p>
          </div>
        </div>

            <!-- 当前加速度卡片 -->

        <div class="card card-custom mb-3">
            <div class="card-body">
                <h5 class="card-title">加速度</h5>
                <p class="card-text">
                  <i class="fas fa-tachometer-alt"></i>
                  <span class="acceleration-data">AccX: <strong>{{ Acc.Accx }}</strong></span>
                  <span class="acceleration-data">AccY: <strong>{{ Acc.Accy }}</strong></span>
                  <span class="acceleration-data">AccZ: <strong>{{ Acc.Accz }}</strong></span>
                </p>
            </div>
        </div>
        
           <!-- 当前角速度卡片 -->
        <div class="card card-custom">
          <div class="card-body">
           <h5 class="card-title">角速度</h5>
           <p class="card-text">
            <i class="fas fa-drafting-compass"></i>
            <span class="acceleration-data">AsX: <strong>{{ As.Asx }}</strong></span>
           <span class="acceleration-data">AsY: <strong>{{ As.Asy }}</strong></span>
           <span class="acceleration-data">AsZ: <strong>{{ As.Asz }}</strong></span>
          </p>
         </div>
        </div>

         <!-- 当前角度卡片 -->
        <div class="card card-custom">
          <div class="card-body">
           <h5 class="card-title">三个方向角度</h5>
           <p class="card-text">
            <i class="fas fa-compass"></i>
            <span class="acceleration-data">AngX: <strong>{{ Ang.Angx }}</strong></span>
           <span class="acceleration-data">AngY: <strong>{{ Ang.Angy}}</strong></span>
           <span class="acceleration-data">AngZ: <strong>{{ Ang.Angz}}</strong></span>
          </p>
         </div>
        </div>


      </div>
      <div class="col-md-1 ">
        <canvas id="canvas" width="150" height="150"></canvas>
      </div>
    </div>
  
  </div>
  
</template>

<script>
import { ref , onMounted ,onUnmounted} from 'vue';
import 'font-awesome/css/font-awesome.min.css';
import $ from 'jquery';  

export default {
   name:"SportsMonitor",
   setup() {
   
    const heartRate = ref('75 bpm');
    const upperArmAngle = ref('45°');
    const lowerArmAngle = ref('30°');
    const temperature = ref('');
    // 加速度
    const Acc = ref({
       Accx: '',
        Accy: '',
        Accz: '',
      });
      //角速度
      const As = ref({
      Asx: '',
      Asy: '',
      Asz: ''
    });
    //角度
    const Ang = ref({
      Angx: '',
      Angy: '',
      Angz: ''
    });
    const Frameid=ref(null);

    function startMonitor(){
          $.ajax({
            url:'http://127.0.0.1:5000/database/connect',
            type:'POST',
            success:function(){
              console.log("已连接数据库")
            },
            error: function(error) {
          console.error('Error:', error);
            }
          })
    }

    function EndMonitor(){
          $.ajax({
            url:'http://127.0.0.1:5000/database/disconnect',
            type:'POST',
            success:function(){
              console.log("已断开数据库")
            },
            error: function(error) {
          console.error('Error:', error);
            }
          })
    }


    function loadData() {
      $.ajax({
        url: 'http://localhost:3000/data',  // 后端服务的URL
        type: 'GET',
        success: function(data) {
          //console.log(data[data.length-1]);
          console.log(data[0]);
          if (data.length > 0) {
            upperArmAngle.value = data[0].angle+'°';  // 更新角度
            lowerArmAngle.value=data[0].angle+'°';
            Acc.value.Accx = data[0].accx+'g';
            Acc.value.Accy = data[0].accy+'g';
            Acc.value.Accz = data[0].accz+'g';
            As.value.Asx = data[0].asx + '°/s';  
            As.value.Asy = data[0].asy + '°/s';
            As.value.Asz = data[0].asz + '°/s';
            Ang.value.Angx = data[0].angx + '°';  
            Ang.value.Angy = data[0].angy + '°';
            Ang.value.Angz = data[0].angz + '°';
            temperature.value=data[0].temp+'°C';
          }
          //console.log(1);
        },
        error: function(error) {
          console.error('Error:', error);
        }
      });
    }

    function clock() {
  const now = new Date();
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.save();
  ctx.clearRect(0, 0, 150, 150);
  ctx.translate(75, 75);
  ctx.scale(0.4, 0.4);
  ctx.rotate(-Math.PI / 2);
  ctx.strokeStyle = "black";
  ctx.fillStyle = "white";
  ctx.lineWidth = 8;
  ctx.lineCap = "round";

  // 小时刻度
  ctx.save();
  for (let i = 0; i < 12; i++) {
    ctx.beginPath();
    ctx.rotate(Math.PI / 6);
    ctx.moveTo(100, 0);
    ctx.lineTo(120, 0);
    ctx.stroke();
  }
  ctx.restore();

  // 分钟刻度
  ctx.save();
  ctx.lineWidth = 5;
  for (let i = 0; i < 60; i++) {
    if (i % 5 !== 0) {
      ctx.beginPath();
      ctx.moveTo(117, 0);
      ctx.lineTo(120, 0);
      ctx.stroke();
    }
    ctx.rotate(Math.PI / 30);
  }
  ctx.restore();

  const sec = now.getSeconds();
  // 要显示扫秒式的时钟，请使用：
  // const sec = now.getSeconds() + now.getMilliseconds() / 1000;
  const min = now.getMinutes();
  const hr = now.getHours() % 12;

  ctx.fillStyle = "black";

  // 显示图像描述
  canvas.innerText = `当前时间：${hr}:${min}`;

  // 时针
  ctx.save();
  ctx.rotate(
    (Math.PI / 6) * hr + (Math.PI / 360) * min + (Math.PI / 21600) * sec,
  );
  ctx.lineWidth = 14;
  ctx.beginPath();
  ctx.moveTo(-20, 0);
  ctx.lineTo(80, 0);
  ctx.stroke();
  ctx.restore();

  // 分针
  ctx.save();
  ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
  ctx.lineWidth = 10;
  ctx.beginPath();
  ctx.moveTo(-28, 0);
  ctx.lineTo(112, 0);
  ctx.stroke();
  ctx.restore();

  // 秒针
  ctx.save();
  ctx.rotate((sec * Math.PI) / 30);
  ctx.strokeStyle = "#D40000";
  ctx.fillStyle = "#D40000";
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(-30, 0);
  ctx.lineTo(83, 0);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(95, 0, 10, 0, Math.PI * 2, true);
  ctx.stroke();
  ctx.fillStyle = "rgb(0 0 0 / 0%)";
  ctx.arc(0, 0, 3, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.restore();

  ctx.beginPath();
  ctx.lineWidth = 14;
  ctx.strokeStyle = "#325FA2";
  ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
  ctx.stroke();

  ctx.restore();

  Frameid.value=window.requestAnimationFrame(clock);

}

   
    // 在组件挂载时设置定时器
    onMounted(() => {
      clock();
      loadData();  // 首次加载数据
      const intervalId = setInterval(loadData, 1000);  // 每1秒刷新一次数据
      
      // 在组件卸载时清除定时器
      onUnmounted(() => {
        clearInterval(intervalId);
        if(Frameid.value)
        {
          cancelAnimationFrame(Frameid.value);
        }
      });
    });
    return { heartRate, upperArmAngle, lowerArmAngle, temperature ,Acc,As ,Ang,startMonitor,EndMonitor};
  }
   
}
</script>

<style scoped>
   

.model-container {
  flex: 1;
  padding: 10px;
}

.model-iframe {
  width: 100%;
  height: 600px; /* 根据需要调整 */
  border: 1px solid #e1e1e1; /* 给 iframe 添加轻微的边框 */
  border-radius: 8px; /* 轻微的边框圆角 */
}

.card-custom {
  margin-top: 40px;
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
  font-size: 1.5rem; /* 增大字体大小 */
  font-weight: bold; /* 字体加粗 */
  display: flex;
  align-items: center;
}

/* 图标样式 */
.card-custom .card-text i {
  font-size: 2rem; /* 图标大小 */
  margin-right: 10px; /* 图标与文字间的距离 */
}
.acceleration-data {
  margin-left: 5px;
  margin-right: 25px; /* 加速度数据之间的间距 */
  display: inline-block; /* 使每个加速度数据独占一行 */
}
#canvas{
  position: fixed;
}

.button-container {
  display: flex;
  justify-content:flex-start;
  margin-bottom: 20px;
  margin-left: 10px;
}
.btn-success{
  margin-right: 30px;
}

</style>




