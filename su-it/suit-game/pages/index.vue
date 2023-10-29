<template>
  <div class="bgku">
    <v-dialog v-model="dialogku" persistent max-widht="600px" >
      <v-card class="rounded-xl pa-4">
        <h1 class="my-4 text-center " style="color:#df6051;">{{ keterangan }}</h1>

        <div class="d-flex justify-center my--">
          <v-btn block  depressed text class="rounded-xl btnku teksku " @click="dialogku=false">Kembali</v-btn>
        </div>
      </v-card>
    </v-dialog>
    <h2>Ronde: {{ currentRound }}</h2>
    <div class="d-flex mt-2 justify-space-between">
      <h3>Skor Kamu: {{ playerScore }}</h3>
      <h3>Skor Komputer: {{ computerScore }}</h3>
    </div>
    <div v-if="tunggu == true">
      <v-row class="align-center justify-space-between">
        <v-col cols="6" style="position: relative" class="d-flex justify-start">
          <v-img
            :src="require('~/assets/batu2.png')"
            max-width="100px"
            class="batupng2"
          ></v-img>
        </v-col>
        <v-col cols="6" style="position: relative" class="d-flex justify-end">
          <v-img
            :src="require('~/assets/batu.png')"
            max-width="100px"
            class="batupng"
          ></v-img>
        </v-col>
      </v-row>
    </div>
    <div v-else-if="tunggu == null">
      <v-row class="align-center justify-space-between">
        <v-col cols="6" style="position: relative" class="d-flex justify-start">
          <v-img
            :src="require('~/assets/batu2.png')"
            style="opacity: 0"
            max-width="100px"
            class="batupng2"
          ></v-img>
        </v-col>
        <v-col cols="6" style="position: relative" class="d-flex justify-end">
          <v-img
            :src="require('~/assets/batu.png')"
            style="opacity: 0"
            max-width="100px"
            class="batupng"
          ></v-img>
        </v-col>
      </v-row>
    </div>
    <div v-if="tunggu == false">
      <v-row class="align-center justify-space-between">
        <v-col cols="6" style="position: relative" class="d-flex justify-start">
          <v-img :src="imageplayer" max-width="100px" class="playerChoice" />
        </v-col>
        <v-col cols="6" style="position: relative" class="d-flex justify-end">
          <v-img :src="imagecomp" max-width="100px" class="compChoice" />
        </v-col>
      </v-row>
    </div>
    <v-row>
      <v-col cols="4"
      class="d-flex justify-center">
      <v-btn :disabled="disblkond" block  depressed text class="rounded-xl btnku teksku text-h5 text-capitalize" @click="choose('scissors')">✌</v-btn>
    </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <v-btn :disabled="disblkond" block  depressed text class="rounded-xl btnku teksku text-h5 text-capitalize" @click="choose('paper')">✋</v-btn>
      </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <v-btn :disabled="disblkond" block  depressed text class="rounded-xl btnku teksku text-h5 text-capitalize" @click="choose('rock')">✊</v-btn>
      </v-col>
      <v-col cols="12" class="d-flex justify-center">
        <v-btn :disabled="disblkondres"  block  depressed text class="rounded-xl btnku teksku text-h6 text-capitalize" @click="reset()">reset</v-btn>
      </v-col>
    </v-row>



  </div>
</template>

<script>
export default {
  data() {
    return {
      imageplayer: "gunting.png",
      imagecomp: null,
      currentRound: 1,
      playerScore: 0,
      computerScore: 0,
      playerChoice: "",
      computerChoice: "",
      disblkond: false,
      disblkondres: false,
      keterangan: null,
      tunggu: null,
      dialogku:false,
    };
  },
  methods: {
    async choose(playerChoice) {
      this.disblkond = true;
      this.disblkondres = true;
      this.tunggu = true;
      const choices = ["rock", "paper", "scissors"];
      const computerChoice =
        choices[Math.floor(Math.random() * choices.length)];
      this.imageChoice(playerChoice, computerChoice);
      // await new Promise(resolve => {
      setTimeout(() => {
        this.$nextTick(() => {
          this.tunggu = false;
          this.playerChoice = playerChoice;
          this.computerChoice = computerChoice;

          if (playerChoice === computerChoice) {
          } else if (
            (playerChoice === "rock" && computerChoice === "scissors") ||
            (playerChoice === "scissors" && computerChoice === "paper") ||
            (playerChoice === "paper" && computerChoice === "rock")
          ) {
            this.playerScore++;
          } else {
            this.computerScore++;
          }
          // if (this.currentRound === 3) {
            // }

            // resolve();
          this.menang();
          this.disblkond = false;
          this.disblkondres = false;
          });
      }, 2000);
      // })
    },
    async imageChoice(playerimg, compChoice) {
      // if(img==='scissors'){
      this.imageplayer = playerimg + "1.png";
      this.imagecomp = compChoice + ".png";
      // }else if()
    },
    async reset() {
      (this.currentRound = 1),
        (this.playerScore = 0),
        (this.computerScore = 0),
        (this.playerChoice = ""),
        (this.computerChoice = ""),
        (this.tunggu = false);
    },
    async menang() {
      if (this.currentRound < 3) {
        this.currentRound++;
      } else {
        if (this.playerScore > this.computerScore) {
          // alert("Anda menang!");
          this.disblkond = true;
          this.keterangan = 'Kamu menang!';
          this.dialogku = true;
          // this.reset();
        } else if (this.computerScore > this.playerScore) {
          // alert("Komputer menang!");
          this.disblkond = true;
          this.keterangan = 'Kamu Kalah!';
          this.dialogku = true;
          // this.reset();
        } else {
          // alert("Seri!");
          // this.reset();
          this.disblkond = true;
          this.keterangan = 'Seri!';
          this.dialogku = true;
        }
      }
    },
  },
};
</script>
</script>
<style>
.teksku {
  color: #ffe1c7 !important;
}
.btnku {
  background: #df6051 !important;
}
.bgku {
  height:100vh;
  background: #6ba0a6;
}
.batupng {
  left: 0px;
  animation: batupnganimasi 2s infinite ease-in-out;
}
.playerChoice {
  left: 20px;
  transform: rotate(90deg);
}
.compChoice {
  right: 20px;
  transform: rotate(-90deg);
}
@keyframes batupnganimasi {
  0% {
    transform: rotate(-80deg);
  }
  50% {
    transform: rotate(-100deg);
  }
  100% {
    transform: rotate(-80deg);
  }
}
.batupng2 {
  right: 0px;

  animation: batupnganimasi2 2s infinite ease-in-out;
}
@keyframes batupnganimasi2 {
  0% {
    transform: rotate(80deg);
  }
  50% {
    transform: rotate(100deg);
  }
  100% {
    transform: rotate(80deg);
  }
}
</style>
