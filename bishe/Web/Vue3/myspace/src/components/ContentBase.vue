<template>
  <div class="home">
    <div class="container">
      <div class="card">
      <!-- <img src="..." class="card-img-top" alt="..."> -->
        <div class="card-body">
           <slot></slot>
        </div>
    </div>
  </div>
    
  </div>
</template>

<script>
   export default{
    name:"ContentBase",
   }
</script>

<style scoped>
.container{
  margin-top: 20px;
}

</style>