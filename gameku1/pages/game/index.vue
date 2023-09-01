<template>
  <div class="game">
    <img src="~/assets/gameaste/ok-okay.gif" alt="" :class="achvm1 ? 'achv1 achv1aktif' : 'achv1'" srcset="">
    <img src="~/assets/gameaste/anime-wow.gif" alt="" :class="achvm2 ? 'achv2 achv2aktif' : 'achv2'" height="300px"
      srcset="">
    <img src="~/assets/gameaste/ses.png" alt="" :class="achvm3 ? 'achv3 achv3aktif' : 'achv3'" height="600px" srcset="">
    <!-- <v-btn @click="achvm3 = !achvm3">p</v-btn> -->
    <v-dialog class="pauseee" v-model="dialogpause" style="background: #3c6bc09d;">
      <div class="" style="padding: 20px 200px;">
        <div class="kolomtblpaus ">
          <v-row class="ma-0  justify-center">
            <button @click="lanjutps" class="tombolpause mb-5">Lanjut</button>
          </v-row>
          <v-row class="ma-0  justify-center">
            <!-- <button class="tombolpause mb-5" >Ulang</button> -->
          </v-row>
          <v-row class="ma-0  justify-center">
            <button class="tombolpause" @click="keluargame">Keluar</button>
          </v-row>
        </div>
      </div>
    </v-dialog>
    <v-dialog v-model="itgmndg" persistent>
      {{ angkagmnd }}
    </v-dialog>
    <v-dialog v-model="dialogend" persistent width="auto" style="box-shadow: none !important;">
      <div class="">
        <v-row class="ma-0 ">
          <!-- <v-col cols="2" class="d-flex justify-content-flex-end"> -->
          <v-col class="my-auto">
            <p>Game Over</p>
            <div class=" skorak ">
              <p class="atsangskrak ma-0" style="  color:white;
  margin-top: 20px;
  font-weight: 400;
  font-size: 20px;">Hasil Skor:</p>
              <p class="angkaskorakhir ma-0" style=" color:yellow;line-height: 100px ;
  margin-top: 20px;
  font-size: 100px;">{{ totskor }}</p>
            </div>
          </v-col>
          <v-col class="">

            <!-- </v-col> -->

            <div class="imgkont justify-center ">
              <!-- <v-col cols="2"> -->
              <img src="~/assets/kuru-kuru-kururin.gif" height="10px" alt="">
              <img src="~/assets/2.png" style="object-fit: cover;" height="400px" alt="">
              <div class="klmpbtn ">
                <button class="tombolend mr-3" @click="stargamenya">Main Lagi</button>
                <button class="tombolend" @click="keluargame">Keluar</button>
              </div>
            </div>
          </v-col>

          <!-- </v-col> -->
        </v-row>
      </div>
    </v-dialog>
    <v-container>
      <div class="atas d-flex justify-space-between pt-5">
        <!-- style="position: absolute; z-index: 3 " -->

        <div class="hati" v-if="nyawa == 3">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
        </div>
        <div class="hati" v-if="nyawa == 2">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
        </div>
        <div class="hati" v-if="nyawa == 1">
          <img src="~/assets/ati.png" alt="" height="25px" srcset="">
        </div>
        <div class="hati" v-if="nyawa == 0">
        </div>
        <div class="waktu text-center">
          <p class="wktxt ma-0" style=" color: yellow;font-size: 50px;">{{ waktu }}</p>
          <div class="">
            <p class="ma-0" style="font-size: 10px; font-weight: 400;">pilihan bot</p>
            <p>{{ bot }}</p>
          </div>
        </div>
        <div class="i"><v-icon @click="pausee">mdi-keyboard-backspace</v-icon></div>
      </div>

      <div class="bawahan" style="">
        <div class="poinmu pt-2" style="position:relative;">
          <p style="position: absolute; z-index: 3;" class="skork">Skor:</p>
          <p class="botskr">{{ skor }} </p>
        </div>
      </div>




      <div class="row" style="padding-top: 100px;">
        <div class="col  text-center">
          <div style="position: absolute; z-index: 3; " :class="csklik[0] ? 'kotakpil ktkpilhvr' : 'kotakpil'">
            <p class="my-auto" style="  font-size: 34px; font-weight: 700;">1</p>
          </div>
        </div>
        <div class="col  text-center">
          <div style="position: absolute; z-index: 3; " :class="csklik[1] ? 'kotakpil ktkpilhvr' : 'kotakpil'">
            <p class="my-auto" style=" font-size: 34px; font-weight: 700;"> 2</p>
          </div>
        </div>
        <div class="col  text-center">
          <div style="position: absolute; z-index: 3; " :class="csklik[2] ? 'kotakpil ktkpilhvr' : 'kotakpil'">
            <p class="my-auto" style=" font-size: 34px; font-weight: 700;">3</p>
          </div>
        </div>
        <div class="col  text-center">
          <div style="position: absolute; z-index: 3; " :class="csklik[3] ? 'kotakpil ktkpilhvr' : 'kotakpil'">
            <p class="my-auto" style=" font-size: 34px; font-weight: 700;">4</p>
          </div>
        </div>
        <!-- <div class="col  text-center" ><div class="kotakpil"><p  class="my-auto" style="font-size: 15px;">SIAP</p></div></div>
        <div class="col  text-center" ><div class="kotakpil"><p class="my-auto" style="font-size: 15px;"> Hormat</p></div></div>
        <div class="col  text-center" ><div class="kotakpil"><p class="my-auto" style="font-size: 15px;">Isirahat ditempat</p></div></div>
        <div class="col  text-center" ><div class="kotakpil"><p class="my-auto" style="font-size: 15px;">BALAP</p></div></div> -->
      </div>


    </v-container>



  </div>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";
export default {
  middleware: 'middlewarenext',
  data() {
    return {
      bot: null,
      player: null,
      timerawalcoy: null,
      angkagmnd: 0,
      itgmndg: true,
      skor: 0,
      pilihan: [
        { dtl: 'Siap' },
        { dtl: 'Hormat' },
        { dtl: 'Istirahat Ditempat' },
        { dtl: 'BALAP' },
      ],
      randomNumber: null,
      waktu: 30,
      gemoper: false,
      nyawa: 3,
      ketmain: 0,
      totskor:0,
      gamemulai: false,
      dialogend: false,
      kalah: 0,
      timer: null,
      audioingm: null,
      audkalah: null,
      csklik: [false, false, false, false],
      k: 1,

      achvm1: false,
      achvm2: false,
      achvm3: false,
      intacang: 2,
      audsesgem: null,
      imageUrl: require('~/assets/bg.jpg'),

      gamepause: true,
      dialogpause: false,
    }
  },

  mounted() {
    this.$toast.success('Tekan key d f j k pada keyboard', {
        duration: 3000, // Durasi Toast dalam milidetik (bisa disesuaikan)
      });

    AOS.init();
    document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
    if (this.gamepause === true) {
      this.ubahh()
    }

    // setInterval(this.ubahh, 1000);






  },
  methods: {
    pausee() {
      this.gamepause = false
      this.dialogpause = true
    },
    lanjutps() {
      this.gamepause = true
      this.dialogpause = false

    },
    ubahh() {
      this.timerawalcoy = setInterval(() => {
        if (this.angkagmnd >= 1) {
          this.angkagmnd--;
        } else {
          this.angkagmnd = 0

          this.itgmndg = false
          console.log('kalah')
          clearInterval(this.timerawalcoy);
          this.stargamenya()


        }

      }, 1000)
      // console.log(this.angkagmnd)
      if (this.angkagmnd == 0) {
      }
    },
    playlagucoy() {
      this.audioingm = new Audio('https://zaaa445.iza0005.repl.co/ingame.mp3');
      this.audioingm.play();
    },
    keluargame() {
      // this.gemmoper
      this.dialogend = false
      this.$cookies.remove('setgamemulai')
      window.location.replace("/");
    },
    setz() {
      this.$cookies.set('setgamemulai', 'simpen')
    },
    stargamenya() {
      // if(kalah==0){

      if (this.k == 0) {
        this.audkalah.pause()
      }
      this.k = 1
      this.playlagucoy()
      this.dialogend = false
      this.ketmain = 1


      this.startgame()
      // console.log(this.ketmain)
      // }
    },
    kontrolkey() {
      document.addEventListener('keydown', this.pencetan)
      document.addEventListener('keyup', this.pencetan1)
    },
    pencetan(event) {
      switch (event.key) {
        case 'd':
          this.plihanplayer(1)
          this.csklik[0] = true
          break;
        case 'f':
          this.plihanplayer(2)
          this.csklik[1] = true
          break;
        case 'j':
          this.plihanplayer(3)
          this.csklik[2] = true
          break;
        case 'k':
          this.plihanplayer(4)
          this.csklik[3] = true
          break;

        default:
          break;
      }
    },
    pencetan1(event) {
      switch (event.key) {
        case 'd':
          // this.plihanplayer('Siap')
          this.csklik[0] = false
          break;
        case 'f':
          // this.plihanplayer('Hormat')
          this.csklik[1] = false
          break;
        case 'j':
          // this.plihanplayer('Istirahat Ditempat')
          this.csklik[2] = false
          break;
        case 'k':
          // this.plihanplayer('BALAP')
          this.csklik[3] = false
          break;

        default:
          break;
      }
    },

    startgame() {
      // if(this.waktu !==0 ||this.nyawa !==0){
      this.generatetcoy()
      this.kontrolkey()
      this.waktumundur()
      console.log('lanut')
      // }else{
      console.log('kljh')

      // }
    },
    waktumundur() {
      this.timer = setInterval(() => {
        if (this.waktu >= 1) {
          this.waktu--;

        } else {

          console.log('kalah')
          this.gemmoper()

        }

      }, 1000)
    },
    generatetcoy() {
      // this.waktu =
      // if (!this.gemoper) {

      this.randomNumber = Math.floor(Math.random() * 4) + 1;
      // console.log(this.randomNumber);

      if (this.randomNumber === 1) {
        this.bot = 1
      } else if (this.randomNumber == 2) {
        this.bot = 2
      } else if (this.randomNumber == 3) {
        this.bot = 3
      } else if (this.randomNumber == 4) {
        this.bot = 4
      }
      // }

    },
    plihanplayer(pbalap) {
      //gem oper
      if (this.waktu == 0 || this.nyawa === 0) {
        this.gemmoper()


      } else {
        //main
        this.player = pbalap
        console.log(pbalap)
        console.log(this.bot)
        if (this.bot ===this.player) {
          this.skor += 1
          if (this.skor % 5 === 0) {
            this.waktu += 3
          }

          if (this.skor % 60 === 0) {
            this.intacang = 2 ///achv3
            this.audsesgem = new Audio('https://zaaa445.iza0005.repl.co/ses.mp3');
            this.audsesgem.play();
            setTimeout(() => {
              this.$nextTick(() => {
                this.achvm3 = true,
                  this.imageUrl = require('~/assets/gameaste/ses.png')
                document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
              });
            }, 200);



            const intachv3 = setInterval(() => {
              if (this.intacang >= 1) {
                this.intacang--;
              } else {
                this.imageUrl = require('~/assets/bg.jpg'),
                  document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
                this.achvm3 = false
                this.intacang = 0
                clearInterval(intachv3);
              }
            }, 1000)
          } else if (this.skor === 10) {
            this.intacang = 2 //durasi achv 1
            this.audsesgem = new Audio('https://zaaa445.iza0005.repl.co/okay-meme.mp3');
            this.audsesgem.play();
            setTimeout(() => {
              this.$nextTick(() => {
                this.achvm1 = true,
                  this.imageUrl = require('~/assets/gameaste/ok-okay.gif')
                document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
              });
            }, 200);



            const intachv3 = setInterval(() => {
              if (this.intacang >= 1) {
                this.intacang--;
              } else {
                this.achvm1 = false
                this.imageUrl = require('~/assets/bg.jpg'),
                  document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
                this.intacang = 0
                clearInterval(intachv3);


              }
            }, 1000)
          } else if (this.skor === 30) {
            this.intacang = 2 //durasi achv 2
            let audsesgem = new Audio('https://zaaa445.iza0005.repl.co/wow.mp3');
            audsesgem.play();
            setTimeout(() => {
              this.$nextTick(() => {
                this.achvm2 = true
                this.imageUrl = require('~/assets/gameaste/anime-wow.gif'),
                  document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
              });
            }, 200);
            const intachv3 = setInterval(() => {
              if (this.intacang >= 1) {
                this.intacang--;
              } else {
                this.achvm2 = false
                this.imageUrl = require('~/assets/bg.jpg'),
                  document.documentElement.style.setProperty('--image-url', `url(${this.imageUrl})`);
                this.intacang = 0
                clearInterval(intachv3);


              }
            }, 1000)

          }
          // this.randomNumber = Math.floor(Math.random() * 4) + 1;
          this.generatetcoy()
        } else {
          //salah pencet ilag 1 nyawanya
          this.nyawa -= 1
          console.log('ilang 1 nyawanya')
        }

      }

    },

    gemmoper() {
      this.k = 0
      this.audioingm.pause()
      this.audkalah = new Audio('https://zaaa445.iza0005.repl.co/kuru-kuru (1).mp3');
      this.audkalah.play();
      clearInterval(this.timer);
      document.removeEventListener('keydown', this.pencetan);
      document.removeEventListener('keyup', this.pencetan1);
      this.$toast.error('Kamu kalah', {
        duration: 5000,
        action: {
          text: 'Oke', // Teks tombol
          onClick: (e, toastObject) => {
            // Logika yang akan dieksekusi saat tombol Oke ditekan
            toastObject.goAway(0); // Menutup Toast
          }
        }
      });

      this.resetGame()
      this.dialogend = true
      this.kalah = 1
    },
    resetGame() {
      this.bot = null;
      this.player = null;
      this.totskor= this.skor
      this.skor = 0;
      this.waktu = 30;
      this.gameover = false;
      this.nyawa = 3;
      this.gameStarted = false;
    },

  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.pencetan);
    document.removeEventListener('keyup', this.pencetan1);
  },



  //audio
}


</script>

<style>
:root {
  --image-url: '';
  /* URL gambar akan diatur melalui JavaScript */
}

.v-dialog {
  box-shadow: #2b5387;
}

.tombolpause {

  padding: 10px 15px;
  color: #2b5387;
  background: white;
  font-size: 20px;
  font-weight: 700;
  border-radius: 20px;
  letter-spacing: 5px;
  box-shadow: 3px 4px 11px 1px rgba(0, 0, 0, 0.2);
  transition: 0.3s cubic-bezier(0.075, 0.82, 0.165, 1);
}

.tombolpause:hover {

  color: white;
  background: #2b5387;
  transform: scale(1.1);

}

.tombolend {

  padding: 10px 15px;
  color: #2b5387;
  background: white;
  font-size: 20px;
  font-weight: 700;
  border-radius: 20px;
  letter-spacing: 5px;
  box-shadow: 3px 4px 11px 1px rgba(0, 0, 0, 0.2);
  transition: 0.3s cubic-bezier(0.075, 0.82, 0.165, 1);
}

.tombolend:hover {

  color: white;
  background: #2b5387;
  transform: scale(1.1);

}

.skorak {

  font-size: 20px;
  color: rgb(255, 255, 255);
}

.skorak.atsangskrak {

  color: white;
  margin-top: 20px;
  font-weight: 400;
  font-size: 20px;
}

.angkaskorakhir p {

  color: #2b5387;
  margin-top: 20px;
  font-size: 100px;
}

.skork {
  font-size: 20px;
  color: rgb(255, 255, 255);
}

.botskr {
  color: white;
  margin-top: 20px;
  font-size: 48px;
}

.achv3 {
  position: absolute;
  left: -700px;
  z-index: 1;
  top: 100px;
  animation: muter 3s infinite ease-in-out;
  transition: all 1s cubic-bezier(0.25, 0.1, 0.25, 1);

}

.achv3.achv3aktif {
  transform: rotate(90deg);
  left: 80px;

}

@keyframes muter {
  0% {
    transform: rotate(0);
  }

  50% {
    transform: rotate(90deg);
  }

  100% {
    transform: rotate(0);
  }
}

.achv1 {
  position: absolute;
  left: -700px;
  z-index: 1;
  /* transform: scale(1.5); */
  height: 300px;
  width: 300px;
  top: 100px;
  animation: achv1anm 3s infinite ease-in-out;
  transition: all 1s cubic-bezier(0.25, 0.1, 0.25, 1);
  transform-origin: center center;
  /* transform: scale(0.9); */

}

.achv1.achv1aktif {
  left: 80px;


}

@keyframes achv1anm {
  0% {
    transform: rotate(0);
  }

  50% {
    transform: rotate(90deg);
  }

  100% {
    transform: rotate(0);
  }
}

.achv2 {
  position: absolute;
  left: -700px;
  z-index: 1;
  /* transform: scale(1.5); */
  top: 100px;
  animation: achv2anm 3s infinite ease-in-out;
  transition: all 1s cubic-bezier(0.25, 0.1, 0.25, 1);
  transform-origin: center center;
  /* transform: scale(0.9); */

}

.achv2.achv2aktif {
  left: 80px;


}

@keyframes achv2anm {
  0% {
    transform: rotate(0);
  }

  50% {
    transform: rotate(90deg);
  }

  100% {
    transform: rotate(0);
  }
}

.kotakpil p {
  background: #2b5387a5;
  color: white;
  border-radius: 10px;
  padding: 10px 10px;
  transition: 0.2s ease-in-out;
}

.kotakpil.ktkpilhvr p{
  background: #ffffff;

  color: #2b5387;
}

.v-dialog {
  box-shadow: none;
}

p {
  color: white;
  font-size: 40px;
  font-weight: 700;
  letter-spacing: 5px;
}

.game {
  background: var(--image-url);
  background-size: cover;
  transition: opacity 0.5s ease-in-out;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  transition: background-image 0.5s ease-in-out;
  animation: imageTransition 2s ease-in-out;
}

@keyframes imageTransition {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}</style>
