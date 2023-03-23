<template>
    <div>
      <h1>Verifying user email...</h1>
    </div>
  </template>
  
  <script>
  export default {
    async asyncData({ route, redirect }) {
      const { uid, token } = route.query
  
      try {
        await $fetch('/api/v1/verify/', { method: "POST", body: { uid, token } })
        alert('Email verified successfully')
        redirect('/login')
      } catch (error) {
        alert(error.response)
        redirect('/')
      }
    },
  }
  </script>