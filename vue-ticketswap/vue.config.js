const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: 'https://ticketswap.vercel.app/',
  outputDir: 'dist',
  indexPath: '../../templates/_base_vue.html',
  transpileDependencies: true,

  configureWebpack: {
    devServer: {
      historyApiFallback: true,
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
})
