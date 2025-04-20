<template>
  <div class="navbar">
    <div class="logo-wrapper">
    <img class="logo" src="../assets/logo.svg" />
    </div>
    <div class="link-wrapper">
      <RouterLink to="/flyer"><h3 class="nav-link">Flyer</h3></RouterLink>
      <RouterLink to="/aktion/default"><h3 class="nav-link">Aktion</h3></RouterLink>
      <RouterLink to="/how-to"><h3 class="nav-link">How-To</h3></RouterLink>
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
  justify-content: start;
  padding: 0 2em;
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.3);
  margin-bottom: 35px;
}

.logo {
  width: 100px;
}

.logo-wrapper {
  margin: 10px 4em 10px 10px;
}

.link-wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 2em;
}

a {
  text-decoration: none;
}

.nav-link {
  font-weight: 500;
  color: var(--primary-red-text);
}

.nav-link:hover {
  color: var(--primary-red-active);
}
</style>
