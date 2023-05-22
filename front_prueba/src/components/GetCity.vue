<template>
  <h1>Consigue una city</h1>
  <form @submit.prevent>
    <div>
        <label for="id_city"> ID: </label>
        <input type="text" id="id_city" v-model="dataID_get">
    </div>
    <button @click="getCity(id)">City</button>
  </form>
</template>

<script setup>
import {ref} from "vue"

let dataID_get= ref("")

async function getCity(id){
    dataID_get.value = id
}

</script>

<style>

</style>