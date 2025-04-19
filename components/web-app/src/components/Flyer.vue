<template>
  <main>
    <div class="center-col" :style="`background-color: var(--primary-${colorScheme}-full)`">
      <div class="logo-box" :style="`background-color: var(--secondary-${colorScheme}-full)`">
        <img src="../assets/kreisverband_bonn.png" alt="logo" class="logo"/>
      </div>
      <SDPoster :color-scheme="colorScheme" :first-headline="firstHeadline"
                :second-headline="secondHeadline" :sub-headline="subHeadline"/>
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
const colorScheme = ref(route.query.colorScheme ? route.query.colorScheme.toString() : "red");
const link = ref(route.query.link ? route.query.link.toString() : "#");
const firstHeadline = ref(route.query.firstHeadline ? route.query.firstHeadline.toString() : "");
const secondHeadline = ref(route.query.secondHeadline ? route.query.secondHeadline.toString() : "");
const subHeadline = ref(route.query.subHeadline ? route.query.subHeadline.toString() : "");

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
