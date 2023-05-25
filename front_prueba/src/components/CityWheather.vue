<!-- Este componente es para visualizar todos los datos de las ciudades, eliminar y modificar-->
<template>
<h1>City Weather</h1>
<img v-if="isError" src="../assets/image/error.png" alt="error">
<img v-if="isLoading" src="../assets/image/error.png" alt="loading">
<div v-for="dta in data" :key="dta.id">
     <p>Name:  {{ dta.name}}</p>
     <p>Temperature:  {{ dta.temperature}}</p>
     <p>Rain probability:  {{ dta.rain_probability}}</p>
    <button @click="deleteCity(dta.id)">Eliminar</button>
    <button @click="editCity(dta.id)">Editar</button>
</div>
<div v-show="showEdit">
    <form @submit.prevent>
        <div>
            <label for="name_city">NAME: </label>
            <input type="text" id="name_city" v-model="editName">
        </div>
        <div>
            <label for="temperature_city">TEMPERATURE: </label>
            <input type="text" id="temperature_city" v-model="editTemperature">
        </div>
        <div>
            <label for="rain_city">PROBABILIY RAIN:</label>
            <input type="text" id="rain_city" v-model="editRain">
        </div>        
    </form>
    <button @click="enviarCity">Enviar</button>
</div>

</template>

<script setup>
import {ref, onMounted} from "vue"
import axios from "axios"

// let city = ref("")
// let image = ref("")
// let temperature = ref("")
// let rainProbability = ref("")
let isError = ref(false)
let isLoading = ref(false)
let data = ref("")
let showEdit = ref(false)

let editName = ref("")
let editTemperature = ref("")
let editRain = ref("")


// onMounted es la función que renderiza la paǵina cuando se llama.

onMounted(() => {
    getCities()
})

// Conseguir los datos de todas las ciudades

async function getCities(){
    const url = 'http://localhost:5000/cities';
    isLoading.value = true 
    try{
        let response = await axios.get(url)
        data.value = await response.data
        console.log("***** data", data.value)
        console.log("***** response", response)
        
    }catch(error){
        isError.value = true
        console.log(error)
    }
    isLoading.value = false
}

// Modificar
let getId = ref("")

function editCity(id){
    getId.value = id 
    console.log("getID", getId.value)
    showEdit.value = true
}

async function enviarCity(){
    try{
        await axios.put(`http://localhost:5000/cities/${getId.value}`, {
            name: editName.value,
            temperature: editTemperature.value,
            rain_probability: editRain.value
        })
        
    }catch(error){
        console.log(error)
        isError = true
    }
}

// Eliminar

async function deleteCity(id){
try{
    await axios.delete(`http://localhost:5000/cities/${id}`)
    location.reload()
}catch(error){
    isError = true
    console.log(error)
}
}


</script>


<style scoped>

</style>
