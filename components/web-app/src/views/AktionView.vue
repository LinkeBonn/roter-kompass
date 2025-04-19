<template>
  <Navbar/>
  <div class="action-container">
    <div v-if="action" class="meta-container">
      <h2>{{action.name}}</h2>
      <h3>{{action.group_actor}}</h3>
      <h4>{{action.description}}</h4>
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
import {getOpinionsByAction} from "@/api/api.ts";
import {ref, watch} from "vue";
import {useRoute} from "vue-router";
import type {ActionResponse} from "../../env";

const route = useRoute()
const action = ref<ActionResponse | null>(null)

const fetchData = async () => {
  try{
    action.value = await getOpinionsByAction(route.params.aktionId ? route.params.aktionId.toString() : '');
  }catch (e){
    console.error('Error creating action:', e);
  }
}

watch(() => route.params.actionId, fetchData, { immediate: true })

const onOpinionSubmit = () => {

}

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
  padding: 1em;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  width: 100%;
  gap: .5em;
}
</style>
