<template>
  <div class="game" >
    <img src="~/assets/4.png" class="cweprnt" alt="">
    <!-- <div class="cweprn">
    </div> -->
      <v-row>
        <v-col>
          <div class="kri">
            <div class="garis mx-auto mt-2 mb-3" style="height: 20px; width: 80px; background: #434247;"></div>
            <div class="textkiri" >
              <div class="d-flex txtdlmkiri pl-2 " >
                <p class="ma-0 p-0 ">
                  game game game game game  game game game game game game game game game game game game game game game game game game game game game game game
                </p>
              </div>
            </div>
          </div>


          <div class="kiribawhnya" style="margin-bottom: 40px;">
            <div class="textkiribwh text-center" style="margin-right: 140px;">
              <div class="jdlkr">
                <p class="ma-0">
                  game
                </p>
              </div>
              <div class="jdlkr2">
               <p class="ma-0">game.</p>
              </div>
              <div class="deskrbwh">
                <p class="ma-0">
                  game game game game game game game game game game game game game game game game game game game game game game
                </p>
              </div>
              <div class="garis mx-auto mt-2" style="height: 20px; width: 80px; background: #2b5387;">
              </div>

              <div class="lingprn d-flex justify-center mt-4" >
                <div class="lingkaran2 mr-2">

                </div>
                <div class="lingkaran1">

                </div>
              </div>
            </div>
          </div>
        </v-col>
        <v-col>
          <div class="r ">
          <div class="prnt-tbl text-center ">
            <button @click="mulaigame" @mouseover="hovrtbl" class="tombol">Mulai</button>
          </div>
          <audio ref="audio" preload="auto">
      <source src="~/assets/gameaste/hover.mp3" type="audio/mpeg">
    </audio>
          <div class="prnt-tbl text-center ">
            <button @click="pushpanduan" @mouseover="hovrtbl" class="tombol">Panduan</button>
          </div>
        </div>
        </v-col>

        <v-col class="pa-0">
            <div class="textkanan text-center">
              <div class="jdl">
                <p class="ma-0">
                  game
                </p>
              </div>
              <div class="jdl2">
               <p class="ma-0">  game,  game.</p>
              </div>
              <div class="deskanan">
                <p class="ma-0">
                  game game game game game game  game game game game game game game game game game game game game game game game game game game
                </p>
              </div>
              <div class="garis mx-auto mt-2" style="height: 20px; width: 80px; background: #2b5387;">

              </div>
            </div>

            <div class="kananbwh">
              <div class="grskananbawah">

              </div>
              <div class="imgkontener">
                <!-- <img src="~/assets/tu.webp" alt="" srcset=""> -->
              </div>
              <div class="text-center txtbwhkn ">
                <a href="https://prftme-izanagi05.vercel.app/" target="_blank" class="ma-0 text-decoration-none" >by: zaahayyuk</a>
              </div>
            </div>
        </v-col>
      </v-row>
      <v-row class="m-0">
        <div class="atasgaris d-flex">

          <div class="pku">
            <p class="">   game game game game game  game game game</p>
          </div>
          <div class="lp" style="margin:auto 0px;">
            <div class="line"></div>
          </div>
        </div>
      </v-row>
      <v-row class="m-0">
        <div class="bawahgaris">
          <div class="bawahgaris-content">

          game game game game game game game game game game game game game game game game game game game game game game game game</div> </div>
      </v-row>


  </div>
</template>

<script>
export default {
  data() {
    return {
      audioawal:null,
      audiohover:null,
      pacek:0,
      isVisible:false
    }
  },
  mounted() {

    window.addEventListener('DOMContentLoaded', function() {
      const bawahgaris = document.querySelector('.bawahgaris');
      bawahgaris.classList.add('active');
    })
    window.addEventListener('DOMContentLoaded', function() {
      const bawahgaris = document.querySelector('.atasgaris');
      bawahgaris.classList.add('active');
    })
    window.addEventListener('DOMContentLoaded', function() {
  const bawahgaris = document.querySelector('.pku');
  setTimeout(function() {
    bawahgaris.classList.add('active');
  }, 5000); // Penundaan selama 5 detik (5000 milidetik) sebelum menampilkan elemen
});
    window.addEventListener('DOMContentLoaded', function() {
  const bawahgaris = document.querySelector('.atasgaris');
  setTimeout(function() {
    bawahgaris.classList.add('active2');
  }, 5000); // Penundaan selama 5 detik (5000 milidetik) sebelum menampilkan elemen
});



      this.audioplay()

  },
  middleware:'middlewareout',
  methods: {
    hovrtbl(){

      this.audiohover= new Audio('https://zaaa445.iza0005.repl.co/hover.mp3');
      this.audiohover.play();
    },
    stopSound() {
      // Menghentikan suara
      this.audiohover.pause();
      this.audiohover.currentTime = 0;
    },
    audioplay(){
      // if(this.pacek==0){

        this.audioawal = new Audio('https://zaaa445.iza0005.repl.co/awal.mp3');

        this.audioawal.play();
      // }

    },
    mulaigame(){
      const audio = new Audio('https://zaaa445.iza0005.repl.co/klik1.mp3');
     audio.play();
     this.audioawal.pause();
     this.$cookies.set('setgamemulai', 'simpan')
     this.$router.push('/game')

    },
    pushpanduan(){
      this.pacek=1
      const audio = new Audio('https://zaaa445.iza0005.repl.co/klik1.mp3');
     audio.play();
     this.audioawal.pause();
     if(audio.play){
       this.$router.push('/panduan')
      }
    }
  },
}
</script>
<style>

*{}
.hide-atasgaris{
  opacity: 0;
  transition: opacity 1s ease-in-out;
}
.visible-atasgaris {
  opacity: 1;
}
.cweprnt{
  width: 300px;
  position: absolute;
  z-index: 4;
  height: 620px;
  left: 220px;
  animation: floating 3s infinite ease-in-out;
  /* bottom: 0px4 */
}
.cweprnt{
  object-fit: cover;
}
/* .cweprnt { */
  /* position: relative; */
/* } */

@keyframes floating {
  0% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(0, 20px);
  }
  100% {
    transform: translate(0, 0);
  }
}
.lingkaran1{
  background: whitesmoke;
  border: 4px solid #2b5387;
  border-radius: 100%;
  padding: 20px;
}
.lingkaran2{
  background: whitesmoke;
  border: 4px solid #434247;
  border-radius: 100%;
  padding: 20px;
}
.txtbwhkn{
  color: #2b5387;
  font-weight: 600;
  font-size: 24px;
}
.grskananbawah{
  height: 10px; width: 100%; background: #2b5387; margin-bottom: 10px;
}
.imgkontener{

  height: 150px;
  width: 400px;
  background: url('~/assets/tu.webp');
  /* overflow: hidden; */
  background-position: center;
  background-size: cover;
}
.imgkontener > img{
  /* max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  object-position: center; */
}
.kiribawhnya{
  padding-top: 100px;
}
.kri{
  padding-right:160px;
  padding-top: 20px;
}
.textkanan{
  padding: 10px 50px;
  padding-top: 20px;
}
.jdl p{
  line-height: 44px;
  font-size: 60px;
  font-weight: 700;
  color: #434247;
}
.bawahgaris-content {
  width: auto;
  white-space: nowrap;
}
.jdl2 p{
  color: #434247;
  font-size: 30px;
  font-weight: 700;
  line-height: 44px;
}
.deskanan p{
  color: #434247;
  font-size: 10px;
  padding:0px 50px;
  /* font-weight: 700; */
}
.jdlkr p{
  color: #434247;
  font-size: 80px;
  font-weight: 700;
  line-height: 54px;
}
.jdlkr2 p{
  color: #434247;
  font-size: 50px;
  line-height: 54px;
  font-weight: 700;
}
.deskrbwh p{
  color: #434247;
  font-size: 10px;
  /* padding:0px 80px; */
  /* font-weight: 700; */
}
.line{
  background: whitesmoke;
  width:150px;
  height: 25px;
  margin-left: 100px;
}
.atasgaris{
  background: #434247;
  /* display:block; */

  width:0px;
  height:30px;
  transition: width 1s, height 1s;
  padding-left: 20px;
  margin-bottom: 20px;
  color: whitesmoke;
}
.atasgaris p{
  margin: 0px;
  padding: 4px;
  font-size: 40px;
  font-weight: 700;
}
.bawahgaris{

  transition: width 1s;
  width: 0px;
  background: #2b5387;
  padding:5px;
}
.bawahgaris.active{
  width: 100vw;
}
.atasgaris.active{
  transition: width 1s, height 1s;
  width: 100vw;
}
.atasgaris.active2{
  transition: width 1s, height 1s;
  height:80px;
}
.pku{
  opacity: 0;
  height:0px;
  transition: height 1s, opacity 1s;
}
.pku.active{
  height:auto;
  opacity: 1;
}
.textkiri{
  /* margin:auto 0px; */
  border-left: solid #2b5387 20px;
  padding:2px 0px ;


}
.txtdlmkiri p {
  font-size: 12px;
}
.game{
  position: relative;
  background: url('~/assets/bgawal.png');
  object-fit: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
}
.prnt-tbl{
  z-index: 6;
  margin-top: 60px;
}
.tombol{

  padding:10px 15px;

  color:white;
  background: #2b5387;
  font-size: 40px;
  font-weight: 700;
  border-radius: 20px;
  letter-spacing: 5px;
  box-shadow: 3px 4px 11px 1px rgba(0, 0, 0, 0.2);
  transition: 0.3s cubic-bezier(0.075, 0.82, 0.165, 1);
}
.tombol:hover{
  color: #2b5387;
  background:white;
  transform: scale(1.3);

}
</style>
