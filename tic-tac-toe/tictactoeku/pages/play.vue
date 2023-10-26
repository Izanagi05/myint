<template>
  <div class="htmlku">
    <v-dialog v-model="dialogpauseku">
      <v-card class="pa-4 rounded-xl">
        <div class="d-flex justify-end mb-4">
          <v-icon
            class="grey--text text--darken-4"
            @click="dialogpauseku = false"
          >
            mdi-close
          </v-icon>
        </div>
        <div
          class="font-weight-medium text-center text-h5 grey--text text--darken-4"
        >
          Yakin Ingin Keluar?
        </div>
        <v-row class="ma-0 mt-6">
          <v-col cols="12">
            <div class="d-flex justify-center">
              <button class="mulai2 py-2 px-4" @click="dialogpauseku = false">
                Lanjut Main
              </button>
            </div>
          </v-col>
          <v-col cols="12" class="my-4">
            <div class="d-flex justify-center">
              <button class="mulai2 py-2 px-4" @click="$router.push('/')">
                Keluar Game
              </button>
            </div>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogku" persistent>
      <v-card class="pa-4 rounded-xl" style="background-color: rgba(255, 255, 255, 0.629) !important;">
        <div>
          <div
            v-if="keterangan !== 'Seri'|| keterangan==='berlangsung'"
            class="font-weight-medium text-center text-h5 grey--text text--darken-4"
          >
            <v-img :src="require('~/assets/menang.gif')"> </v-img>
            Selamat
            <v-icon v-if="keterangan === 'X'" color="#378bd3" class="text-h4"
              >mdi-close</v-icon
            >
            <v-icon
              v-else-if="keterangan === 'Y'"
              color="#49b7d2"
              class="text-h4"
              >mdi-circle-outline</v-icon
            >
            Atas Kemenangannya
          </div>
          <div
            v-else
            class="font-weight-medium text-center text-h5 grey--text text--darken-4"
          >
            Seri
          </div>
          <div class="d-flex justify-center my-4">
            <button class="mulai2 py-2 px-4" @click="restartgame">
              Kembali
            </button>
          </div>
        </div>
      </v-card>
    </v-dialog>
    <div class="">
      <div class="d-flex justify-center align-center my-4">
        <div class="text-h5 grey--text text--darken-4 font-weight-medium">
          Giliran player:
        </div>
        <v-icon v-if="isianpemain === 'X'" class="text-h3" color="#378bd3"
          >mdi-close</v-icon
        >
        <v-icon v-else-if="isianpemain === 'Y'" class="text-h3" color="#49b7d2"
          >mdi-circle-outline</v-icon
        >
        <v-icon v-else-if="isianpemain === 'Seri'">seri</v-icon>
      </div>
    </div>

    <v-container class="pa-4">
      <div class="d-flex justify-center align-items-center">
        <v-card max-width="auto" flat style="background-color: #9fe7f5">
          <v-row>
            <v-col cols="4" v-for="(cell, i) in board" :key="i" class="pa-1">
              <div class="d-flex justify-center align-center">
                <button
                  type="button"
                  style="height: 122px; width: 122px"
                  class="grey lighten-3"
                  @click="makeMove(i, cell)"
                  :disabled="cell.disbl"
                >
                  <v-icon
                    v-if="cell.dt === 'X'"
                    :style="{ animation: cell.disbl ? 'none' : 'fadeIn 1s' }"
                    text
                    class="text-h2"
                    color="#378bd3"
                    >mdi-close</v-icon
                  >
                  <v-icon
                    v-else-if="cell.dt === 'Y'"
                    class="text-h2"
                    color="#49b7d2"
                    >mdi-circle-outline</v-icon
                  >
                </button>
              </div>
              <!-- <v-btn @click="tes()">{{ i }}</v-btn> -->
            </v-col>
          </v-row>
        </v-card>
      </div>
      <div
        class="d-flex justify-space-between"
        style="margin-top: 100px; margin-bottom: 100px"
      >
        <button type="button" class="mulai pa-4" @click="restartgame">
          <v-icon class="text-h4" color="#212121">mdi-restart</v-icon>
        </button>
        <button type="button" class="mulai pa-4" @click="pausemodal">
          <v-icon class="text-h4" color="#212121">mdi-cog-outline</v-icon>
        </button>
      </div>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      board: [
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
      ],
      disablenya: false,
      dialogku: false,
      dialogpauseku: false,
      keterangan: "berlangsung",
      // // ... data lainnya ...
      // player1: { p1name: null, p1value: 'X', p1move: null },
      // player2: { p2name: null, p2value: 'Y', p2move: null },
      isianpemain: "X",
    };
  },
  methods: {
    // initializeBoard() {
    //   this.board = [{dt:''},{dt:''},{dt:''},{dt:''},{dt:''},{dt:''},{dt:''},{dt:''},{dt:''}]
    // },
    makeMove(i, cell) {
      this.board[i].dt = this.isianpemain;
      this.isianpemain = this.isianpemain === "X" ? "Y" : "X";
      this.yangjalan();
      cell.disbl = true;
    },
    yangjalan() {
      const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8], // Horizontal
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8], // Vertical
        [0, 4, 8],
        [2, 4, 6], // Diagonal
      ];

      for (const condition of winningConditions) {
        const [a, b, c] = condition;
        console.log(`Checking condition: ${a}-${b}-${c}`);
        console.log("-------------------------------");
        console.log(
          `Board values: ${this.board[a].dt}-${this.board[b].dt}-${this.board[c].dt}`
        );

        if (
          this.board[a].dt !== null &&
          this.board[a].dt === this.board[b].dt &&
          this.board[a].dt === this.board[c].dt
        ) {
          this.keterangan = this.board[a].dt;
          this.disablenya = true;
          this.dialogku = true;
          return; // Hentikan loop jika ada yang menang
        }
      }

      // Cek apakah semua sel terisi, dalam hal ini seri
      if (this.board.every((cell) => cell.dt !== null)) {
        this.keterangan = "Seri";
        this.isianpemain = "Seri";
        this.disablenya = true;
        this.dialogku = true;
      }
    },
    tes() {
      console.log(this.board);
      console.log(this.allpem);
      console.log("5" + 2 + 3);
    },
    pausemodal() {
      this.dialogpauseku = true;
    },
    restartgame() {
      (this.board = [
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
        { dt: null, disbl: false },
      ]),
        this.keterangan = "berlangsung",
        this.disablenya = false,
        this.dialogku = false,
        this.dialogpauseku = false
      this.isianpemain= 'X'
    },
  },
  mounted() {
    // this.initializeBoard()
  },
};
</script>

<style >
html .htmlku {
  background: #9fe7f5;
}
:root {
  --bg: #fff;
  --text: #212121;
  --light-wrnaku: #fff8e1;
  --wrnaku: #ffecb3;
  --dark-wrnaku: #ffca28;
  --wrnaku-border: #ffb300;
  --wrnaku-shadow: #ffe08274;
}
.v-btn.v-btn--disabled {
  color: green;
  background-color: transparent;
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

button.mulai2 {
  font-weight: 600;
  color: var(--text);
  background: var(--light-wrnaku);
  border: 2px solid var(--wrnaku-border);
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    background 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.mulai2::before {
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

button.mulai2:hover {
  background: var(--wrnaku);
  transform: translate(0, 0.25em);
}

button.mulai2:hover::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.5em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.5em, -1em);
}

button.mulai2:active {
  background: var(--wrnaku);
  transform: translate(0em, 0.65em);
}

button.mulai2:active::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0, -1em);
}
</style>
