<template>
  <div>
    <h1>Permainan Suit 3 Ronde</h1>
    <div>
      <p>Komputer memilih: {{ computerChoice }}</p>
      <p>Kamu memilih: {{ playerChoice }}</p>
      <p>Ronde: {{ currentRound }}</p>
      <p>Skor Anda: {{ playerScore }}</p>
      <p>Skor Komputer: {{ computerScore }}</p>
      {{ tunggu }}
    </div>
    <v-btn @click="choose('rock')">batu</v-btn>
    <v-btn @click="choose('paper')">kertas</v-btn>
    <v-btn @click="choose('scissors')">gunting</v-btn>
    <v-btn @click="reset()">reset</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentRound: 1,
      playerScore: 0,
      computerScore: 0,
      playerChoice: "",
      computerChoice: "",
      tunggu: false,
    };
  },
  methods: {
    choose(playerChoice) {
      const choices = ["rock", "paper", "scissors"];
      const computerChoice =
        choices[Math.floor(Math.random() * choices.length)];

      setTimeout(() => {
        this.$nextTick(() => {
          this.tunggu = true;
          // this.tunggu=false
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
          if (this.currentRound < 3) {
            this.currentRound++;
          } else {
            if (this.playerScore > this.computerScore) {
              alert("Anda menang!");
              this.reset()
            } else if (this.computerScore > this.playerScore) {
              alert("Komputer menang!");
              this.reset()
            } else {
              alert("Seri!");
              this.reset()
            }
          }
        });
      }, 2000);
    },
    reset(){
      this.currentRound= 1,
      this.playerScore= 0,
      this.computerScore= 0,
      this.playerChoice= "",
      this.computerChoice= "",
      this.tunggu= false
    }
  },
};
</script>
