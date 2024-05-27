<template>
  <NavBar>
    
  </NavBar>
    <ContentBase>
       <HomeGuide></HomeGuide>
       <div class="gap"></div>
       <DigitalTwins></DigitalTwins>
    </ContentBase>
</template>

<script>
// @ is an alias to /src
import ContentBase from"../components/ContentBase";
import NavBar from "../components/NavBar.vue";
import HomeGuide from "../components/HomeGuide.vue";
import DigitalTwins from "../components/DIgitalTwins.vue";
export default {
  name: 'HomeView',
  components: {
    ContentBase,
    NavBar,
    HomeGuide,
    DigitalTwins
  }
}
</script>

<style scoped>
   .gap{
        width: 100%;
        height: 20px;
   }
</style>



