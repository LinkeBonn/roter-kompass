<template>
  <main>
    <div class="center-col" :style="`background-color: var(--primary-${colorScheme}-full)`">
      <div class="logo-box" :style="`background-color: var(--secondary-${colorScheme}-full)`">
        <img src="../assets/kreisverband_bonn.png" alt="logo" class="logo"/>
      </div>
      <SDPoster :color-scheme="colorScheme" first-headline="Menschennahe Politik"
                second-headline=" statt Lobbyismus!" sub-headline="Zeig uns deine Meinung."/>
      <h2>Roter Kompass</h2>
      <qrcode-vue :value="link" foreground="#460000" :size="200" :image-settings="imageSettings" level="H"/>
    </div>
  </main>
</template>

<script setup lang="ts">
import {SDPoster} from "@linkebonn/solid-ui"
import QrcodeVue from "qrcode.vue";
import type {ImageSettings} from 'qrcode.vue'
import {ref} from "vue";
import {useRoute} from "vue-router";

const route = useRoute()
console.log(route.query)
const colorScheme = ref(route.query.colorScheme ? route.query.colorScheme : "red");
const link = ref(route.query.link ? route.query.link : "#");

const imageSettings = ref<ImageSettings>({
  src: 'https://raw.githubusercontent.com/LinkeBonn/roter-kompass/refs/heads/main/components/web-app/src/assets/logo.svg',
  width: 50,
  height: 50,
  excavate: false,
})

</script>

<style scoped>
.center-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  padding: 15px;
  gap: 30px;
  aspect-ratio: 148 / 210;
}

@media print {
  .center-col {
    aspect-ratio: 148 / 210;
    print-color-adjust: exact;
  }
}

@page {
  margin: 0;
  width: 148mm;
  height: 210mm;
  size: A5;
}

.logo-box{
  padding: 15px;
  width: 100%;
}

.logo {
  width: 150px;
}

h2 {
  color: white;
}
</style>
