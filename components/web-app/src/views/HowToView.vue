<template>
  <Navbar/>
  <div class="howto-container">
    <details>
      <summary>
        <h2>Aktion erstellen
          <font-awesome-icon icon="chevron-down"/>
        </h2>
      </summary>
      <h3>Fülle auf der Flyer Seite alle Aktions Felder aus und drücke anschliessend auf Aktion
        erstellen</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_1.png">
      </div>
      <h3>Kopiere dir die Aktions ID für Später. Jetzt kannst du nach Wunsch den Flyer
        bearbeiten.</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_3.png">
      </div>
      <h3>Mit Klick auf Drucken kannst du dir die PDF speichern um später den Flyer zu drucken.</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_4.png">
      </div>
    </details>
    <details>
      <summary>
        <h2>Aktion finden
          <font-awesome-icon icon="chevron-down"/>
        </h2>
      </summary>
      <h3>Gebe deine Aktions ID auf der Aktion Seite ein oder scanne den QR-Code auf dem Flyer</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_5.png">
      </div>
    </details>
    <details>
      <summary>
        <h2>Meinung abgeben
          <font-awesome-icon icon="chevron-down"/>
        </h2>
      </summary>
      <h3>Gebe auf einer Aktionsseite deinen Input zur Aktion ein und sende ihn mit drücken auf Posten ab.</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_7.png">
      </div>
      <h3>Bereits gesendete Meinungen können unten auf der Aktionsseite ingesehen werden.</h3>
      <div class="image-wrapper">
        <img class="howto-image" src="../assets/howto/step_8.png">
      </div>
    </details>
  </div>
</template>

<script setup lang="ts">
import Navbar from "@/components/Navbar.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

</script>

<style scoped>
.howto-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: start;
  flex-direction: column;
  gap: 1em;
  padding: .2em;
  @media screen and (min-width: 600px) {
    padding: 4em;
  }
}

.howto-image {
  width: 90%;
  @media screen and (min-width: 600px) {
    width: 50%;
  }
}

details {
  display: flex;
  flex-direction: column;
  gap: 1em;
}

summary {
  font-weight: 500;
  color: var(--primary-red-text);
  list-style: none;
  margin-bottom: 2em;
  cursor: pointer;
}

summary:hover {
  color: var(--primary-red-active);
}

.image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border: .2em solid var(--primary-red-text);
  margin-bottom: 1em;
}

h3 {
  margin-bottom: 1em;
}
</style>
