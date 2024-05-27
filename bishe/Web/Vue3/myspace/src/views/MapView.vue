<template>
     <NavBar></NavBar>
     <ContentBase>
       <MapContainer></MapContainer>
     </ContentBase>
</template>


<script>
  import ContentBase from "../components/ContentBase";
  import NavBar from "../components/NavBar.vue";
  import MapContainer from "../components/MapContainer.vue";
//   import { onMounted, onUnmounted } from "vue";
  export default{
    name:"MapView",
    components: {
        ContentBase,
        NavBar,
        MapContainer,
    },

    setup(){
       

        return{

        };
    }
}
       

</script>



<style  scoped>
  
</style>