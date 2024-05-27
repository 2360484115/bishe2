<template>
    <NavBar>
      
    </NavBar>
    <ContentBase>
      <LastData></LastData>
    </ContentBase>
  </template>
  
  <script>
  // @ is an alias to /src
  
  import ContentBase from "../components/ContentBase";
  import NavBar from "../components/NavBar.vue";
  import LastData from "../components/LastData.vue";
  export default {
    name: 'HighorderData',
    components: {
      ContentBase,
      NavBar,
      LastData,
    }
  }
  </script>
  
  
  <style scoped>
  .container{
    margin-top: 20px;
  }
  </style>
  