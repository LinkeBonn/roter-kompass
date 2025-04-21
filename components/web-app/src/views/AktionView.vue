<template>
  <Navbar/>
  <div class="action-container" v-if="renderComponent && !defaultView">
    <div v-if="action" class="meta-container">
      <h2>{{ action.name }}</h2>
      <h3>{{ action.group_actor }}</h3>
      <h4>{{ action.description }}</h4>
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
    <h2 v-if="action && action.opinions && action.opinions.length > 0">Gesammelte Meinungen</h2>
    <div v-if="action && action.opinions && action.opinions.length > 0" class="action-board primary-red--inverted">
      <SDPostIt
        class="opinion"
        v-for="opinion in action.opinions"
        color-scheme="red"
        :is-editable="false"
        text-label="Meinung"
        author-label="Name"
        button-label="Posten"
        :text="opinion.text"
        :author="opinion.author"
        :key="opinion.id"
      />
    </div>
  </div>
  <div class="action-container" v-if="defaultView">
    <SDTextInput mode="primary" color-scheme="red" label="Aktions ID"
                 @on-change="onActionIdChange"/>
    <SDButton mode="primary" color-scheme="red" label="Aktion finden" @on-click="onFindAction"/>
  </div>
</template>

<script setup lang="ts">
import Navbar from "@/components/Navbar.vue";
import {SDButton, SDPostIt, SDTextInput} from "@linkebonn/solid-ui";
import {createOpinion, getOpinionsByAction} from "@/api/api.ts";
import {ref, watch} from "vue";
import {useRoute, useRouter} from "vue-router";
import type {ActionResponse, Opinion} from "../../env";
import {notify} from "@kyvg/vue3-notification";

const route = useRoute()
const router = useRouter()
const action = ref<ActionResponse | null>(null)
const renderComponent = ref(true)
const defaultView = ref(false)
const actionId = ref("")

const fetchData = async () => {
  try {
    action.value = await getOpinionsByAction(route.params.aktionId ? route.params.aktionId.toString() : '');
  } catch (e) {
    notify({
      title: "Fehler",
      text: `Es gab ein Problem bei dem Laden von Meinungen`,
      type: "error",
    })
  }
}

watch(
  () => route.params.aktionId,
  () => {
    defaultView.value = route.params.aktionId === 'default';
    if (!defaultView.value) {
      fetchData();
    }
  },
  {immediate: true}
)

const onOpinionSubmit = async (opinionToCreate: Opinion) => {
  try {
    if (action.value) {
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
        fetchData();
      }, 1)
    } else {
      notify({
        title: "Fehler",
        text: `Es gab ein Problem bei der Erstellung deiner Meinungen`,
        type: "error",
      })
    }
  } catch (e) {
    notify({
      title: "Fehler",
      text: `Es gab ein Problem bei der Erstellung deiner Meinungen`,
      type: "error",
    })
  }
}

const onActionIdChange = (actionIdToFind: string) => {
  actionId.value = actionIdToFind;
}

const onFindAction = () => {
  router.push(`/aktion/${actionId.value}`)
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
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 90%;
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

.opinion {
  min-width: 300px;
  max-width: 400px;
}

</style>
