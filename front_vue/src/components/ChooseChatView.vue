<template>
  <button class="exitBut"></button>
  <div class="authForm">
    <div class="header">
      <div>Выберите / создайте чат</div>
    </div>
    <div class="frame">
      <div class="row">
        <div>
          <p>Первая комната</p>
          <button></button>
        </div>
      </div>

      <div class="row createChat">
        <input placeholder="Введите название чата">
        <button>Создать</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChooseChatView',
  props: {
    msg: String
  }
}
</script>

<style>
  #app {
    height: 100%;
    width: 100%;
    margin: 0;
    background: #F4F4F4;

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
</style>

<style scoped>
  @font-face {
    font-family: 'Open Sans';
    src: url(../assets/OpenSans/OpenSans-Light.ttf);
  }
  input:focus{
    outline: none;
  }

  .authForm {
    width: 546px;

    position:relative;
    top:0;
    bottom:0;
    left:0;
    right:0;
    margin:auto;

    display: flex;
    flex-direction: column;

    background: #FFFFFF;
    box-shadow: inset 0px 0px 0px 1px #E5E5EA;
    border-radius: 10px;
  }
  .header {
    flex: 0 0 68px;

    border-top-left-radius: 10px;
    border-top-right-radius: 10px;

    box-shadow: inset 0px -1px 0px #E5E5EA;

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
  }
  .frame {
    background: #FFFFFF;

    flex: 1 1 1px;
    margin: 20px;

    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    gap: 10px;
  }

  .row {
    width: 100%;
    height: 48px;
  }

  .row div {
    /* Iris/80 */
    background: #7879F1;
    border-radius: 5px;

    /* Inside auto layout */

    flex: none;
    order: 0;
    align-self: stretch;
    flex-grow: 0;

    color: #969696;

    color: #F4F4F4;

    align-items: center;
    /*padding: 15px;*/

    display: flex;
  }
  .row div div {
    margin: 0;
    padding: 0;
    flex: 1 1 1px
  }

  .row p {
    margin: 0;
    padding: 15px;
    flex: 1 1 1px;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 18px;
    /* identical to box height, or 129% */
  }

  .row div button {
    margin-right: 15px;
    margin-top: 12px;
    margin-bottom: 12px;

    background: url(../assets/arrow.svg);

    width: 24px;
    height: 24px;

    border: none;

    cursor: pointer;
  }
  .row div button:hover {
    filter: invert(34%) sepia(77%) saturate(642%) hue-rotate(203deg) brightness(96%) contrast(92%);
  }
  .row div button:active {
    filter: invert(34%) sepia(77%) saturate(142%) hue-rotate(253deg) brightness(96%) contrast(92%);
  }

  .createChat {
    box-sizing: border-box;

    /* Auto layout */

    display: flex;
    flex-direction: row;

    gap: 10px;

    width: 100%;
    height: 48px;

    border: 1px solid #E5E5E5;
    border-radius: 5px;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;
    align-items: center;

    padding: 15px 0 15px 15px;
  }

  .row.createChat input {
    border: none;
    flex: 1 1 1px;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 18px;
    /* identical to box height, or 129% */
    color: #000000;

    width: 100%;
    height: 46px;
    padding: 0;
    margin: 0;
  }
  .row.createChat button {
    margin: 5px 5.5px 5px 0;

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

    flex: 0 0 115px;

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
  .row.createChat button:hover{
    background: #4b4cc0;
    border-color: #4b4cc0;
  }
  .row.createChat button:active{
    background: #3638c0;
    border-color: #3638c0;
  }

  .exitBut {
    top: 0;
    right: 0;
    padding: 0;

    margin: 24px 182px 0 0;

    background: url(../assets/exit.svg);
    width: 24px;
    height: 24px;
    border: none;
    cursor: pointer;

    position: absolute;
  }
  .exitBut:hover {
    filter: invert(61%) sepia(4%) saturate(23%) hue-rotate(324deg) brightness(79%) contrast(82%);
  }
  .exitBut:active {
    filter: invert(66%) sepia(11%) saturate(4%) hue-rotate(45deg) brightness(106%) contrast(92%);
  }
</style>
