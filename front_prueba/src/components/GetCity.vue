<template>
  <h1>Consigue una city</h1>
  <img v-if="isError" src="../assets/image/error.png" alt="error">
  <form @submit.prevent>
    <div>
        <label for="id_city"> ID: </label>
        <input type="text" id="id_city" v-model="dataID_get">
    </div>
    <button @click="getCity">City</button>
  </form>
  <div v-show="hidden ">
    <p>Name: {{  data.name }}</p> 
    <p>Temperature: {{ data.temperature}}</p> 
    <p>Rain_Probility: {{ data.rain_probability }}</p>
  </div>
</template>

<script setup>
import {ref} from "vue"
import axios from "axios"

let dataID_get= ref("")
let isError = false
let data = ref("")
let hidden = ref(false)


async function getCity(){

    try{
      let response = await axios.get(`http://localhost:5000/cities/${dataID_get.value}`)
      data.value = await response.data
      console.log("esto es data", data.value)
      hidden.value = true
     
    }catch(error){
      console.log(error)
      isError = true
    }
}

</script>

<style>

</style>