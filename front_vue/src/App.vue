<template>
  <component :is="currentView"></component>
</template>

<script>
import AuthView from './components/AuthView.vue'
import ChooseChatView from "./components/ChooseChatView.vue";
import ChatView from "./components/ChatView.vue";

export default {
  name: 'App',
  data() {
    return {
      currentView: AuthView
    }
  },
  created (){
    this.emitter.on('changeView', (data) => {
      switch (data.view) {
        case "AuthView":
          this.currentView = AuthView;
          break;
        case "ChooseChatView":
          this.currentView = ChooseChatView;
          break;
        case "ChatView":
          this.currentView = ChatView;
          break;
        default:
          this.currentView = AuthView;
      }
    })
  },
  methods: {
  }
}
</script>

<style>

</style>
