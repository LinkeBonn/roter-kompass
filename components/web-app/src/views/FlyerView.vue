<template>
  <Navbar/>
  <div class="form-container">
    <div class="input-container">
      <h2>Erstelle einen Flyer</h2>
      <h3>Schritt 1 Aktion Erstellen</h3>
      <SDTextInput mode="primary" color-scheme="red" label="Aktionsname"/>
      <SDTextInput mode="primary" color-scheme="red" label="Aktionsgruppe"/>
      <SDTextArea mode="primary" color-scheme="red" label="Aktionsbeschreibung"/>
      <SDButton mode="primary" color-scheme="red" label="Aktion erstellen"/>
      <h3>Schritt 2 Flyer Drucken</h3>
      <SDButton mode="primary" color-scheme="red" label="Drucken" @on-click="onPrint"/>
    </div>
    <iframe class="flyer-box" :src="previewLink" title="Preview" width="50%" >
    </iframe>
  </div>
</template>

<script setup lang="ts">
import {SDButton, SDTextArea, SDTextInput} from "@linkebonn/solid-ui";
import {ref} from "vue";
import Navbar from "@/components/Navbar.vue";

const previewLink = ref("preview?colorScheme=red&link=https://roter-kompass.linkebonn.de/aktion/test")

const onPrint = () => {
  //@ts-ignore
  document.querySelector("iframe").contentWindow.print()
}

</script>

<style scoped>
.flyer-box {
  border: 0.2em solid;
  padding: 0.3em 0.5em;
  aspect-ratio: 148 / 210;
}

.form-container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: start;
  padding: 2em;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: space-between;
  gap: 15px;
}
</style>
