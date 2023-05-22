<template>
  <h1>Formulario para crear city</h1>
  <img v-if="isError" src="../assets/image/error.png" alt="error">
    <form @submit.prevent>
        <div>
            <label for="id_city"> ID: </label>
            <input type="text" id="id_city" v-model="dataID">
        </div>
        <div>
            <label for="name_city">NAME: </label>
            <input type="text" id="name_city" v-model="dataName">
        </div>
        <div>
            <label for="temperature_city">TEMPERATURE: </label>
            <input type="text" id="temperature_city" v-model="dataTemperature">
        </div>
        <div>
            <label for="rain_city">PROBABILIY RAIN:</label>
            <input type="text" id="rain_city" v-model="dataRain">
        </div>        
    </form>
    <button @click="createCity">Crear</button>
</template>

<script setup>
import {ref} from "vue"
import axios from "axios"

let isError = ref(false)

let dataID= ref("")
let dataName = ref("")
let dataTemperature = ref("")
let dataRain = ref("")

const url = 'http://localhost:5000/cities';

async function createCity(){
    try{
      await axios.post(url, {
            id: dataID.value,
            name: dataName.value,
            temperature: dataTemperature.value,
            rain_probability: dataRain.value
        })
         location.reload()
    }catch(error){
        console.log(error)
        isError = true
    }
}




</script>



<style>

</style>