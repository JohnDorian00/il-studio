<template>
  <div class="authForm">
    <div class="header"><div>Авторизация</div></div>
    <div class="frame">
      <input autofocus class="inp1" placeholder="Логин" v-model="login">
      <input class="inp2" placeholder="Пароль" v-model="pass">
      <button @click="auth">Войти</button>
    </div>
  </div>
</template>

<script>
import { useCookies } from "vue3-cookies";

export default {
  name: 'AuthView',
  props: {
    token: String
  },
  setup() {
    const { cookies } = useCookies();
    return { cookies };
  },
  data() {
    return {
      login: "",
      pass: ""
    }
  },
  methods: {
    auth: function () {
      this.emitter.emit('auth', {login: this.login, pass: this.pass})
    },
    pressEnter: function (e) {
      if (e.key === "Enter" && (document.activeElement.tagName.toLowerCase() !== 'button')) {
        this.auth();
      }
    }
  },
  mounted: function () {
    document.addEventListener("keypress", this.pressEnter);
    document.getElementById("app").style.backgroundSize = "cover";
  },
  unmounted() {
    document.getElementById("app").style.backgroundSize = "0px 0px";
    document.removeEventListener("keypress", this.pressEnter);
  }
}
</script>

<style>
  #app {
    background-image: url("../assets/Blur.png");
    background-position:center center;
    background-size: 0 0;
  }
</style>

<style scoped>
  @font-face {
    font-family: 'Open Sans';
    src: url("../assets/OpenSans/OpenSans-Light.ttf");
  }
  input:focus {
    outline: none;
  }

  .authForm {
    height: 292px;
    width: 546px;

    position:absolute;
    top:0;
    bottom:0;
    left:0;
    right:0;
    margin:auto;

    display: flex;
    flex-direction: column;
    /* White/white */
    background: #FFFFFF;
    box-shadow: 0px 40px 30px 10px rgba(0, 0, 0, 0.25), inset 0px 0px 0px 1px #E5E5EA;
    border-radius: 10px;
  }
  .header {
    flex: 0 0 68px;

    border-top-left-radius: 10px;
    border-top-right-radius: 10px;

    background: #FFFFFF;
    box-shadow: inset 0 -1px 0 #E5E5EA;
    backdrop-filter: blur(2px);
    /* Note: backdrop-filter has minimal browser support */

    color: #2C2C2E;

    text-align: center;
    display: table;
  }
  .header div {
    display: table-cell;
    vertical-align: middle;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: bold;
    font-size: 26px;
    line-height: 18px;
    /* identical to box height, or 69% */
    /* Text/grayDark */

  }
  .frame {
    background: #FFFFFF;

    flex: 1 1 1px;
    margin: 20px 20px 30px 20px;

    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    gap: 10px;
  }

  .frame input {
    box-sizing: border-box;

    /* Auto layout */

    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 15px;
    gap: 10px;

    width: 100%;
    height: 48px;

    border: 1px solid #E5E5E5;
    border-radius: 5px;


    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 18px;
    /* identical to box height, or 129% */
    color: #000000;

    /* Inside auto layout */
    flex: none;
    flex-grow: 0;
  }
  .frame input.inp1 {
    order: 0;
  }
  .frame input.inp2 {
    order: 1;
  }
  .frame button {
    /* Frame 3 */
    /* Auto layout */

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;

    gap: 10px;

    width: 102px;
    height: 38px;

    /* Iris/100 */

    background: #5D5FEF;
    border-radius: 5px;
    border: solid 1px #5D5FEF;

    /* Inside auto layout */

    flex: none;
    order: 2;
    flex-grow: 0;

    /* Войти */
    font-family: 'Open Sans', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 18px;
    /* identical to box height, or 129% */

    color: #FFFFFF;

    cursor: pointer;
  }
  .frame button:hover{
    background: #4b4cc0;
    border-color: #4b4cc0;
  }
  .frame button:active{
    background: #3638c0;
    border-color: #3638c0;
  }
</style>
