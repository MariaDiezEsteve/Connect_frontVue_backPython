<template>
<h1>City Weather</h1>
<div v-for="(item, index) in data" :key="index">
        {{ item }}
    <button @click="deleteCity(item[0])">Eliminar</button>
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

onMounted(() => {
    getCities()
})

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
