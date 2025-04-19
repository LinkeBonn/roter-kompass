<template>
  <div class="navbar">
    <div class="logo-wrapper">
    <img class="logo" src="../assets/logo.svg" />
    </div>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.navbar{
  width: 100vw;
  height: 85px;
  display: flex;
  flex-direction: row;
  background-color: white;
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.3);
  margin-bottom: 15px;
}

.logo {
  width: 100px;
}

.logo-wrapper {
  margin: 10px;
}
</style>
