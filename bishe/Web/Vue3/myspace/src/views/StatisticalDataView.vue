<template>
<NavBar/>
<ContentBase>
    <StatData>
        
    </StatData>
</ContentBase>
  
</template>

<script>
import NavBar from "../components/NavBar.vue";
import ContentBase from "../components/ContentBase";
import StatData  from "../components/StatData";
export default {
    name: 'StatisticalDataView',
    components: {
      ContentBase,
      NavBar,
      StatData,
    },

}
</script>

<style scoped>

</style>