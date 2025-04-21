<template>
  <Navbar/>
  <div class="form-container">
    <div class="input-container">
      <h2>Erstelle einen Flyer</h2>
      <h3>Schritt 1 Aktion Erstellen</h3>
      <SDTextInput mode="primary" color-scheme="red" label="Aktionsname" :disabled="isActionCreated" @on-change="onActionNameChange"/>
      <SDTextInput mode="primary" color-scheme="red" label="Aktionsgruppe" :disabled="isActionCreated" @on-change="onActionGroupChange"/>
      <SDTextArea style="width: 55%" mode="primary" color-scheme="red" label="Aktionsbeschreibung" :disabled="isActionCreated" @on-change="onActionDescriptionChange"/>
      <SDButton mode="primary" color-scheme="red" label="Aktion erstellen" @onClick="onCreateAction" :disabled="isActionCreated || (!actionName || !actionGroup)"/>
      <h3>Schritt 2 Flyer Drucken</h3>
      <h4 v-if="actionId" @click="onActionIdClick" class="action-id">Aktions ID: {{actionId}} <font-awesome-icon icon="save" /></h4>
      <SDSelect label="Flyer Farbe" mode="primary" color-scheme="red" :options="colorOptions" @on-select="onFlyerColorChange" :disabled="!isActionCreated"/>
      <SDTextInput mode="primary" color-scheme="red" label="Erste Überschrift" @on-change="onFlyerFirstHeadlineChange" :disabled="!isActionCreated"/>
      <SDTextInput mode="primary" color-scheme="red" label="Zweite Überschrift" @on-change="onFlyerSecondaryHeadlineChange" :disabled="!isActionCreated"/>
      <SDTextInput mode="primary" color-scheme="red" label="Aktionsspruch" @on-change="onFlyerSubHeadlineChange" :disabled="!isActionCreated"/>
      <SDButton mode="primary" color-scheme="red" label="Drucken" @on-click="onPrint" :disabled="!isActionCreated"/>
    </div>
    <iframe class="flyer-box" :src="previewLink" title="Preview" width="50%" >
    </iframe>
  </div>
</template>

<script setup lang="ts">
import {SDButton, SDSelect, SDTextArea, SDTextInput} from "@linkebonn/solid-ui";
import {ref} from "vue";
import Navbar from "@/components/Navbar.vue";
import {createAction} from "@/api/api.ts";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useNotification} from "@kyvg/vue3-notification";
const { notify }  = useNotification()

const colorOptions = [
  {
    value: "red",
    label: "Rot",
  },
  {
    value: "blue",
    label: "Blau",
  },
  {
    value: "green",
    label: "Grün",
  },
  {
    value: "violet",
    label: "Violett",
  },
]

const baseUrl = import.meta.env.VITE_BASE_URL
const previewLink = ref(`preview?firstHeadline=Menschennahe%20Politik&secondHeadline=%20statt%20Lobbyismus%21&subHeadline=Zeig%20uns%20deine%20Meinung.&colorScheme=red&link=${baseUrl}/aktion`)
const isActionCreated = ref(false)
const actionId = ref("")
const actionName = ref("")
const actionGroup = ref("")
const actionDescription = ref("")

const onPrint = () => {
  //@ts-ignore
  document.querySelector("iframe").contentWindow.print()
}

const onCreateAction = async () => {
  try{
    const createdAction = await createAction(
      {
        name: actionName.value,
        description: actionDescription.value,
        group_actor: actionGroup.value,
      }
    )
    isActionCreated.value = true
    onActionIdChange(createdAction.id)
  }catch (e){
    notify({
      title: "Fehler",
      text: `Es gab ein Problem bei der Erstellung der Aktion`,
      type: "error",
    })
  }
}

const onFlyerColorChange = (flyerColor: string) => {
  previewLink.value = previewLink.value.replace(/(colorScheme=)[^&]*/, `$1${flyerColor}`)
}

const onFlyerFirstHeadlineChange = (flyerFirstHeadline: string) => {
  previewLink.value = previewLink.value.replace(/(firstHeadline=)[^&]*/, `$1${flyerFirstHeadline}`)
}

const onFlyerSecondaryHeadlineChange = (flyerSecondHeadline: string) => {
  previewLink.value = previewLink.value.replace(/(secondHeadline=)[^&]*/, `$1${flyerSecondHeadline}`)
}

const onFlyerSubHeadlineChange = (flyerSubHeadline: string) => {
  previewLink.value = previewLink.value.replace(/(subHeadline=)[^&]*/, `$1${flyerSubHeadline}`)
}

const onActionIdChange = (flyerActionId: string) => {
  actionId.value = flyerActionId
  notify({
    title: "Erfolgreich",
    text: `Eine Aktion mit der ID ${flyerActionId} wurde erstellt`,
    type: "success",
  })
  previewLink.value = previewLink.value.replace(/(link=)[^&]*/, `$1${baseUrl}/aktion/${flyerActionId}`)
}

const onActionNameChange = (flyerActionName: string) => {
  actionName.value = flyerActionName
}

const onActionGroupChange = (flyerActionGroup: string) => {
  actionGroup.value = flyerActionGroup
}

const onActionDescriptionChange = (flyerActionDescription: string) => {
  actionDescription.value = flyerActionDescription
}

const onActionIdClick = () => {
  navigator.clipboard.writeText(actionId.value)
}

</script>

<style scoped>
.flyer-box {
  border: 0.2em solid;
  padding: 0.3em 0.5em;
  aspect-ratio: 148 / 210;
  min-width: calc(100vw - 2em);
  max-width: 210mm;
}

@media screen and (min-width: 600px){
  .flyer-box {
    min-width: unset;
  }
}

.form-container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: start;
  padding: 1em;
  flex-wrap: wrap;
  gap: 1em;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: space-between;
  gap: 15px;
}

.action-id {
  color: var(--primary-red-text);
  cursor: pointer;
}

.action-id:hover {
  color: var(--primary-red-active);
  cursor: pointer;
}
</style>
