// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    ssr:false,
    nitro: {
        devProxy: {
            '/api/':{
                target: 'http://127.0.0.1:8000/api/'
            }
        }
    },
    css: [
        // Load a Node.js module directly (here it's a Sass file).
        'bulma',
        // CSS file in the project
        // SCSS file in the project
      ]
})
