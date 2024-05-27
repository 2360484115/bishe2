<template>
  <!-- <NavBar/> -->
  <router-view :key="$route.fullPath"/>
</template>

<script>

  //  import NavBar from "./components/NavBar.vue";
   
   export default{
    name:"APP",
    // components:{
    //   NavBar,
    // }

    
   }
</script>

<style>



</style>

