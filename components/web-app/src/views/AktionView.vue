<template>
  <Navbar/>
  <div class="action-container">
    <div class="meta-container">
      <h2>Aktionsname</h2>
      <h3>Aktionsgruppe</h3>
      <h4>Aktions Beschreibung Aktions Beschreibung Aktions Beschreibung Aktions Beschreibung Aktions Beschreibung
        Aktions BeschreibungAktions BeschreibungAktions Beschreibung Aktions Beschreibung</h4>
    </div>
    <h2>Sagen Sie uns Ihre Meinung!</h2>
    <div class="action-create">
      <SDPostIt color-scheme="red" :is-editable="true" text-label="Ihre Meinung" author-label="Name" button-label="Posten"/>
    </div>
    <h2>Gesammelte Meinungen</h2>
    <div class="action-board primary-red--inverted">
      <SDPostIt color-scheme="red" :is-editable="false" text-label="Ihre Meinung" author-label="Name" button-label="Posten"/>
      <SDPostIt color-scheme="red" :is-editable="false" text-label="Ihre Meinung" author-label="Name" button-label="Posten"/>
      <SDPostIt color-scheme="red" :is-editable="false" text-label="Ihre Meinung" author-label="Name" button-label="Posten"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import Navbar from "@/components/Navbar.vue";
import {SDPostIt} from "@linkebonn/solid-ui";

</script>

<style scoped>
.action-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  gap: 1em;
  padding: 1em;
}

.action-board {
  border: 0.2em solid;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 1em;
  padding: 1em;
}

.action-create {
  padding: 1em;
}

.meta-container {
  gap: 1em;
  padding: 1em;
}
</style>
