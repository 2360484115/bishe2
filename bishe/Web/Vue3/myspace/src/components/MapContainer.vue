<template>
    <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
   
       <div id="container"></div>
       <div id="my-panel"></div>
       <div id="panel"></div>
        <div class="info">
            <h4 id="status"></h4><hr>
            <p id="result"></p><hr>
        </div>
      
       <div class="input-group mb-3 text1">
            <input type="text" class="form-control " placeholder="请输入要查询的地点" v-model="searchKeyword">
            <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="performSearch">搜索</button>
            <button class="btn btn-outline-secondary" type="button"  @click="clearplace">清空</button>
       </div>
       <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="请输入路径起点" v-model="start">
            <input type="text" class="form-control" placeholder="请输入路径终点" v-model="end">
            <button class="btn btn-outline-secondary" type="button"  @click="modesearch">步行路径规划</button>
            <button class="btn btn-outline-secondary" type="button"  @click="clearroute">清空</button>
       </div>
       
</template>


<script>
 
 import AMapLoader from '@amap/amap-jsapi-loader';
 import { onMounted, onUnmounted ,ref} from "vue";

//  import {ref} from "vue";
 export default{
   name:"MapContainer",
   components: {
     
   },

   setup(){
    let map = null;
    const searchKeyword = ref("");
    const placeSearch = ref(null);
     const mode=ref(null);
     const start=ref("");
     const end=ref("");
        onMounted(() => {
            window._AMapSecurityConfig = {
                securityJsCode: "7e9e76848e5724a5e35622080de665c4",
            };
            AMapLoader.load({
                key: "e0026013891fbb3dc0c912760ca21253", // 申请好的Web端开发者Key，首次调用 load 时必填
                version: "2.0", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
                plugins: ["AMap.Scale"], //需要使用的的插件列表，如比例尺'AMap.Scale'，支持添加多个如：['...','...']
            })
            .then((AMap) => {
                map = new AMap.Map("container", {
                    // 设置地图容器id
                    viewMode: "2D", // 是否为3D地图模式
                    zoom: 11, // 初始化地图级别
                    center: [116.397428, 39.90923], // 初始化地图中心点位置
                    resizeEnable: true,
                });
                const marker = new AMap.Marker({
                    position: new AMap.LngLat(116.397428, 39.90923), //经纬度对象，也可以是经纬度构成的一维数组[116.39, 39.9]
                    title: "北京",
                });
                map.add(marker);
                var clickHandler = function(e) {
                    console.log('您在[ '+e.lnglat.getLng()+','+e.lnglat.getLat()+' ]的位置点击了地图！');
                    // const marker = new AMap.Marker({
                    // position: new AMap.LngLat(e.lnglat.getLng(), e.lnglat.getLat()), //经纬度对象，也可以是经纬度构成的一维数组[116.39, 39.9]
                    // title: "北京",
                    // });
                    // map.add(marker);
                };
                map.on('click', clickHandler);

                const content = [
                    "<div><b>高德软件有限公司</b>",
                    "电话 : 010-84107000   邮编 : 100102",
                    "地址 : 北京市望京阜通东大街方恒国际中心A座16层</div>",
                ];
                var infoWindow = new AMap.InfoWindow({
                    content: content.join("<br>"), //传入字符串拼接的 DOM 元素
                    anchor: "top-left",
                });
                marker.on("click", function () {
                    //alert("你点击了Marker");
                    infoWindow.open(map, map.getCenter());
                });
                AMap.plugin("AMap.Walking", function () {
              mode.value = new AMap.Walking({
                    map: map,
                    panel: "my-panel",
                    // policy: 0, //驾车路线规划策略，0是速度优先的策略
                });
            });


                //配置折线路径
                const path = [
                    new AMap.LngLat(121.215553,31.287681),
                    new AMap.LngLat(121.215489,31.287712),
                    new AMap.LngLat(121.215389,31.287951),
                    new AMap.LngLat(121.215404,31.288052),
                    new AMap.LngLat(121.215397,31.287872),
                    new AMap.LngLat(121.215421,31.288036),
                    new AMap.LngLat(121.21546,31.288127),
                    new AMap.LngLat(121.215531,31.288209),
                    new AMap.LngLat(121.215574,31.288246),
                    new AMap.LngLat(121.215702,31.288422),
                    new AMap.LngLat(121.215943,31.288743),
                    new AMap.LngLat(121.216025,31.288822),
                    new AMap.LngLat(121.216103,31.288847),
                    new AMap.LngLat(121.21622,31.28888),
                    new AMap.LngLat(121.216331,31.288865),
                    new AMap.LngLat(121.216423,31.28885),
                    new AMap.LngLat(121.216522,31.288774),
                    new AMap.LngLat(121.216618,31.28857),
                    new AMap.LngLat(121.216611,31.288479),
                    new AMap.LngLat(121.216512,31.288328),
                    new AMap.LngLat(121.216316,31.288085),
                    new AMap.LngLat(121.216128,31.287818),
                    new AMap.LngLat(121.216036,31.28769),
                    new AMap.LngLat( 121.21599,31.287639),
                    new AMap.LngLat(121.215869,31.287621),
                    new AMap.LngLat(121.215741,31.287611),
                    new AMap.LngLat(121.215563,31.287663),
                    new AMap.LngLat(121.215447,31.287783),
                    new AMap.LngLat(121.215403,31.288031),
                    new AMap.LngLat(121.215531,31.28819),
                    new AMap.LngLat(121.215483,31.288468),
                    new AMap.LngLat(121.215252,31.288171),
                    new AMap.LngLat(121.215036,31.287912),
                    new AMap.LngLat(121.215109,31.287767),
                    
                   
                ];
                                //创建 Polyline 实例
                const polyline = new AMap.Polyline({
                    path: path,
                    strokeWeight: 4, //线条宽度
                    strokeColor: "green", //线条颜色
                    lineJoin: "round", //折线拐点连接处样式
                    // isOutline:true,
                });
                map.add(polyline);

                AMap.plugin("AMap.PlaceSearch", function() {
                    placeSearch.value = new AMap.PlaceSearch({
                        pageSize: 5,
                        pageIndex: 1,
                        city: "010",
                        citylimit: false,
                        map: map,
                        panel: "panel",
                        autoFitView: true
                  });
             });
                AMap.plugin('AMap.Geolocation', function() {
                    const geolocation = new AMap.Geolocation({
                        enableHighAccuracy: true,//是否使用高精度定位，默认:true
                        timeout: 10000,          //超过10秒后停止定位，默认：5s
                        position:'RB',    //定位按钮的停靠位置
                        offset: [10, 20], //定位按钮与设置的停靠位置的偏移量，默认：[10, 20]
                        zoomToAccuracy: true,   //定位成功后是否自动调整地图视野到定位点

                    });
                    map.addControl(geolocation);
                    geolocation.getCurrentPosition(function(status,result){
                        if(status=='complete'){
                            onComplete(result)
                        }else{
                            onError(result)
                        }
                    });
             });

                function onComplete(data) {
                            document.getElementById('status').innerHTML='定位成功'
                            var str = [];
                            str.push('定位结果：' + data.position);
                            str.push('定位类别：' + data.location_type);
                            if(data.accuracy){
                                str.push('精度：' + data.accuracy + ' 米');
                            }//如为IP精确定位结果则没有精度信息
                            str.push('是否经过偏移：' + (data.isConverted ? '是' : '否'));
                            document.getElementById('result').innerHTML = str.join('<br>');
                 }
                    //解析定位错误信息
                function onError(data) {
                            document.getElementById('status').innerHTML='定位失败'
                            document.getElementById('result').innerHTML = '失败原因排查信息:'+data.message+'</br>浏览器返回信息：'+data.originMessage;
                    }


             

         })
            .catch((e) => {
                 console.log(e);
            });
        });

        onUnmounted(() => {
        map?.destroy();
        });

        

        const performSearch = () => {
            console.log(1);
            const keyword = searchKeyword.value;
           
            if (keyword.trim() !== "" && placeSearch.value) { // 确保 placeSearchRef 已初始化
                // 通过 placeSearchRef 引用执行搜索操作
                placeSearch.value.search(keyword);
            }
         };

         const modesearch = () => {
            const points = [
                        { keyword: start.value},
                        { keyword: end.value},
                    ];
                    mode.value.search(points, function (status, result) {
                        //status：complete 表示查询成功，no_data 为查询无结果，error 代表查询错误
                        //查询成功时，result 即为对应的驾车导航信息
                        if(status === "complete") {
                            console.log(result);
                        } else if (status === "no_data") {
                            console.log("未查询到结果");
                        } else {
                            console.log("路径规划出错：" + result);
                        }
                    });
         };

         function clearplace(){
            const panel=document.getElementById('panel');
              if(panel)
              {
                panel.innerHTML='';
              }
         }
         function clearroute(){
            const my_panel=document.getElementById('my-panel');
              if(my_panel)
              {
                my_panel.innerHTML='';
              }
         }


        return{
            performSearch,
            searchKeyword,
            modesearch,
            start,
            end,
            clearplace,
            clearroute,
        }



        



   }



}
       
</script>



<style  scoped>
   #container{
       padding:0px;
       margin: 0px;
       width: 100%;
       height: 550px;
   }
   #my-panel {
      position: fixed;
      background-color: white;
      max-height: 90%;
      overflow-y: auto;
      top: 10px;
      left: 10px;
      width: 280px;
    }

    .text1{
        margin-top: 10px;
    }
    .info{
            width:26rem;
        }

    

/* 按钮样式 */


</style>