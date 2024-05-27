<template>
    
    <NavBar>
        
    </NavBar>
    <ContentBase>
        <SportsMonitor>
            
        </SportsMonitor>
    </ContentBase>
</template>

<script>
import SportsMonitor from "../components/SportsMonitor";
import NavBar from "../components/NavBar.vue";
import ContentBase from "../components/ContentBase";

export default {
    name:"SportsData",
    components: {
      ContentBase,
      NavBar,
      SportsMonitor,
    },

    setup(){
            
        
            return{};
    },



}
</script>

<style scoped>

</style>