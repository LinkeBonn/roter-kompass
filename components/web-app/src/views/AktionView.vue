<template>
  <Navbar/>
  <div class="action-container" v-if="renderComponent">
    <div v-if="action" class="meta-container">
      <h2>{{action.name}}</h2>
      <h3>{{action.group_actor}}</h3>
      <h4>{{action.description}}</h4>
    </div>
    <h2>Sagen Sie uns Ihre Meinung!</h2>
    <div class="action-create">
      <SDPostIt
        color-scheme="red"
        :is-editable="true"
        text-label="Ihre Meinung"
        author-label="Name"
        button-label="Posten"
        @on-submit="onOpinionSubmit"
      />
    </div>
    <h2 v-if="action?.opinions.length > 0">Gesammelte Meinungen</h2>
    <div v-if="action?.opinions.length > 0" class="action-board primary-red--inverted">
      <SDPostIt
        v-for="opinion in action.opinions"
        color-scheme="red"
        :is-editable="false"
        text-label="Ihre Meinung"
        author-label="Name"
        button-label="Posten"
        :text="opinion.text"
        :author="opinion.author"
        :key="opinion.id"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import Navbar from "@/components/Navbar.vue";
import {SDPostIt} from "@linkebonn/solid-ui";
import {createOpinion, getOpinionsByAction} from "@/api/api.ts";
import {ref, watch} from "vue";
import {useRoute} from "vue-router";
import type {ActionResponse, Opinion} from "../../env";
import {notify} from "@kyvg/vue3-notification";

const route = useRoute()
const action = ref<ActionResponse | null>(null)
const renderComponent = ref(true)

const fetchData = async () => {
  try{
    action.value = await getOpinionsByAction(route.params.aktionId ? route.params.aktionId.toString() : '');
  }catch (e){
    notify({
      title: "Fehler",
      text: `Es gab ein Problem bei dem Laden von Meinungen`,
      type: "error",
    })
  }
}

watch(() => route.params.actionId, fetchData, { immediate: true })

const onOpinionSubmit = async (opinionToCreate: Opinion) => {
  try{
    if(action.value){
      await createOpinion(
        {
          text: opinionToCreate.text,
          author: opinionToCreate.author,
          action_id: String(action?.value.id),
        }
      );
      notify({
        title: "Erfolgreich",
        text: `Ihre Meinung wurde gespeichert.`,
        type: "success",
      })
      renderComponent.value = false
      setTimeout(() => {
        renderComponent.value = true
      }, 1)
    }else{
      notify({
        title: "Fehler",
        text: `Es gab ein Problem bei der Erstellung deiner Meinungen`,
        type: "error",
      })
    }
  }catch (e){
    notify({
      title: "Fehler",
      text: `Es gab ein Problem bei der Erstellung deiner Meinungen`,
      type: "error",
    })
  }
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
  padding: .2em;
  @media screen and (min-width: 600px) {
    padding: 1em;
  }
}

.action-board {
  border: 0.2em solid;
  display: grid;
  width: 90%;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1em;
  padding: .2em;
  @media screen and (min-width: 600px) {
    padding: 1em;
  }
}

.action-create {
  padding: .2em;
  @media screen and (min-width: 600px) {
    padding: 1em;
  }
}

.meta-container {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  width: 100%;
  gap: .5em;
  padding: .2em;
  @media screen and (min-width: 600px) {
    padding: 1em;
  }
}
</style>
