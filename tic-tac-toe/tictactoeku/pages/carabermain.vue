<template>
  <div>
    <v-container class="pt-2" style="padding-bottom: 100px;">
    <button type="button" class="mulai pa-2 mt-4 mb-4"  @click="$router.push('/')">
          <v-icon class="text-h4" color="#212121" >mdi-arrow-left</v-icon>
        </button>

      <button class="kartuku pa-4 mt-2">

      <div
      class="font-weight-medium text-center text-h5 grey--text text--darken-4 mb-4"
    >
      Cara bermainnya
    </div>
    <ul>
      <li v-for="(step, index) in steps" :key="index" left class="text-start">
        {{ step }}
      </li>
    </ul>
  </button>
</v-container>
  </div>
</template>
  <script>
export default {
  data() {
    return {
      steps: [
        "Pemain 'X' selalu bergerak pertama.",
        "Pemain 'X' memilih salah satu kotak yang masih kosong pada papan permainan.",
        "Pemain 'X' menempatkan tanda 'X' pada kotak yang dipilih.",
        "Pemain 'O' giliran berikutnya dan melakukan langkah yang sama.",
        "Permainan berlanjut dengan pemain bergantian hingga ada pemenang atau hasil seri.",
        "Pemenang adalah pemain yang berhasil menempatkan tiga tanda berurutan secara horizontal, vertikal, atau diagonal.",
        "Jika seluruh papan terisi tanpa ada pemenang, permainan berakhir dengan hasil seri.",
        "Anda dapat mengulangi permainan sebanyak yang Anda inginkan!",
      ],
    }
  },
};
</script>
  <style>
  :root {
  --bg: #fff;
  --text: #212121;
  --light-wrnaku: #fff8e1;
  --wrnaku: #ffecb3;
  --dark-wrnaku: #ffca28;
  --wrnaku-border: #ffb300;
  --wrnaku-shadow: #ffe08274;
}

button {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-size: inherit;
  font-family: inherit;
}

button.mulai {
  font-weight: 600;
  color: var(--text);
  background: var(--light-wrnaku);
  border: 2px solid var(--wrnaku-border);
  border-radius: 100%;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    background 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.mulai::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--dark-wrnaku);
  border-radius: 100%;
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.625em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.65em, -1em);
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    box-shadow 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.mulai:hover {
  background: var(--wrnaku);
  transform: translate(0, 0.25em);
}

button.mulai:hover::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.5em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.5em, -1em);
}

button.mulai:active {
  background: var(--wrnaku);
  transform: translate(0em, 0.65em);
}

button.mulai:active::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0, -1em);
}
button {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-size: inherit;
  font-family: inherit;
}

button.kartuku {
  font-weight: 600;
  color: var(--text);
  background: var(--light-wrnaku);
  border: 2px solid var(--wrnaku-border);
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    background 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.kartuku::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--dark-wrnaku);
  border-radius: inherit;
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.625em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.65em, -1em);
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    box-shadow 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.kartuku:hover {
  background: var(--wrnaku);
  transform: translate(0, 0.25em);
}

button.kartuku:hover::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.5em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.5em, -1em);
}

button.kartuku:active {
  background: var(--wrnaku);
  transform: translate(0em, 0.65em);
}

button.kartuku:active::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0, -1em);
}
</style>
