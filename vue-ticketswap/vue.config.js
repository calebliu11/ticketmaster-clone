const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: 'http://localhost:8080',
  outputDir: '../static/dist',
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
