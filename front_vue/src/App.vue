<template>
  <component :is="currentView" :token="token"></component>
</template>

<script>
import { useCookies } from "vue3-cookies";
import AuthView from './components/AuthView.vue'
import ChooseChatView from "./components/ChooseChatView.vue";
import ChatView from "./components/ChatView.vue";

export default {
  name: 'App',
  setup() {
    const { cookies } = useCookies();
    return { cookies };
  },
  data() {
    return {
      currentView: null,
      token: this.cookies.get("token")
    }
  },
  created (){
    this.emitter.on('auth', (data) => {
      this.auth(data.login, data.pass)
    })

    this.emitter.on('changeView', (data) => {
      this.changeView(data.view)
    })

    if (this.token) {
      this.auth(null, null, this.token);
    } else {
      this.currentView = AuthView
    }
  },
  methods: {
    changeView: function (data) {
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
    },

    auth: async function (login, pass, token) {
      try {
        let head = {'Content-Type': 'application/json'}
        if (token) {
          head.token = token;
        }
        let req = await fetch('http://' + this.backendIp + ':8000/auth/', {
          method: 'POST',
          headers: head,
          body: JSON.stringify({login: login, pass: pass})
        })

        if (req.status === 200) {
          // // Записать куки в браузер
          let body = JSON.parse(await req.json()),
              token = body[0],
              date = new Date(Date.parse(body[1]))

          this.cookies.set("token", token, date);
          this.token = token;
          this.changeView({view: 'ChooseChatView'})
        }

      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style>
  #app {
    height: 100%;
    width: 100%;
    margin: 0;

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
</style>
