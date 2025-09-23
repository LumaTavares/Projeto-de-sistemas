<template>
  <div class="app">
    <h1>{{ titulo }}</h1>

    <input v-model="nome" placeholder="Digite seu nome" />
    <p>Olá, {{ nome || "visitante" }}!</p>

    <button @click="mudarTitulo">Mudar título</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const titulo = ref("Minha primeira tela com Vue")
const nome = ref("")

function mudarTitulo() {
  titulo.value = "Título alterado!"
}
</script>

<style scoped>
.app {
  padding: 2rem;
  font-family: Arial, sans-serif;
}
h1 {
  color: teal;
}
</style>