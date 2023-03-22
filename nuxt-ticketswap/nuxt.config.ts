// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    ssr:false,
    nitro: {
        devProxy: {
            '/api/':{
                target: 'localhost:8000/api/'
            }
        }
    }
})
