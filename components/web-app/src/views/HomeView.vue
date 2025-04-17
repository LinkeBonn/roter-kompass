<template>
  <main>
    <div class="container">
      <div class="center-col">
        <div class="center-row">
          <h1>Roter</h1>
          <img src="../assets/logo.svg" alt="logo" class="compass-logo"/>
          <h1>Kompass</h1>
        </div>
    <SDPoster color-scheme="red" first-headline="Empathische Politik" second-headline=" statt Lobbyismus!" sub-headline="Zeig uns deine Meinung."/>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import {SDPoster} from "@linkebonn/solid-ui"
</script>

<style scoped>
.center-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 15px;
}

.center-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 15px;
  flex-wrap: wrap;
}

.compass-logo{
  width: 100px;
}
</style>
