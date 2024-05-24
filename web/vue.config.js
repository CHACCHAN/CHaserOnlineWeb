const MonocoEditorPlugin = require('monaco-editor-webpack-plugin');
const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: 'static',
  plugin: [
    new MonocoEditorPlugin({
      languages: ['css']
    })
  ]
})
