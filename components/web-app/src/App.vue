<script setup lang="ts">
import { RouterView } from 'vue-router'
import {Notifications} from "@kyvg/vue3-notification";
</script>

<template>
  <RouterView />
  <notifications classes="linke-notification" position="top center"/>
</template>

<style scoped>

</style>
