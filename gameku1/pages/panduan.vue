<template>
  <div>
    <div class="prntpdn" style="position: relative;">
      <div class="bolakiri"></div>
      <div class="bolakanan"></div>
      <div class="div" style="padding-left: 40px;padding-top: 40px;">
        <v-icon size="40" @click="$router.push('/')">mdi-keyboard-backspace</v-icon>
      </div>
      <v-row class=" pa-8" style="position: relative;">

        <div class="">
          <v-img class="imgparent" :src="require('~/assets/3.png')"></v-img>
        </div>
        <v-col cols="10" class="my-auto" style="margin-left:200px;padding-top: 50px;padding-right: 80px;">
          <v-card class="" style="height:450px;background: #2b5387;">
            <div class="bgnyakart">
              <p class="jdpdann mt-3 ml-10">Bagaimana cara bermainnya?</p>
              <div class="pl-10 pt-2 tulisa ">
                <p class="bdpann ma-0">Kamu diarahkan untuk memilih pilihan dengan pilihan yang cocok dengan pilihan bot.
                </p>
                <p class="bdpann ma-0">Kamu diberi durasi
                  30 detik dan 3 nyawa untuk permainan ini.</p>
                  <ul>
                    <li class="mt-2"> <p class="bdpann ma-0">
                  Jika kamu benar dalam memilih, poinmu bertambah 1
                </p></li>
                    <li class="mt-2"><p class="bdpann ma-0">
                  Jika poinmu lebih dari 5 maka diberi tambahan durasi 3 detik</p></li>
                    <li class="mt-2">  <p class="bdpann ma-0">
                  Jika kamu salah dalam memilih nyawanya berkurang 1</p></li>
                    <li class="mt-2">  <p class="bdpann ma-0">
                  Jika nyawa atau waktu kamu habis game selesai</p></li>
                  </ul>




              </div>
            </div>
          </v-card>
        </v-col>

      </v-row>
    </div>
  </div>
</template>
<script>
export default {
  mounted() {


    window.addEventListener('DOMContentLoaded', function () {
      const bawahgaris = document.querySelector('.bolakiri');
      bawahgaris.classList.add('active');
    });

    window.addEventListener('DOMContentLoaded', function () {
      const bawahgaris = document.querySelector('.bolakanan');
      bawahgaris.classList.add('active');
    });
  },
}
</script>
<style>
p{
  margin:0px;
  color:white;
}
.bdpann{

  font-weight: 500;
  font-size: 20px;
}
.jdpdann {
  font-weight: 700;
  font-size: 50px;
}
.bolakiri {
  position: fixed;
  /* padding:40px; */
  width: 650px;
  height: 650px;

  left: -100px;
  top: 100px;
  overflow: hidden;
  border-radius: 100%;
  background: #434247;
  transform: scale(0);
  transition: 1s cubic-bezier(0.175, 0.85, 0.32, 1.275);
}

.bolakiri.active {
  /* transition-delay: 0.95s ; */
  transform: scale(1);

}

.bolakanan {
  position: fixed;
  /* padding:40px; */
  width: 350px;
  height: 350px;
  transform: scale(0);
  right: -100px;
  top: -60px;
  overflow: hidden;
  border-radius: 100%;
  background: #434247;
  transition: 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.bolakanan.active {
  transform: scale(1);

}

.prntpdn {
  position: relative;
  background: url('~/assets/bgawal.png');
  object-fit: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
}




.tulisa {

  width: 100%;
}

.imgparent {
  /* position: relative; */
  position: absolute;
  width: 350px;
  z-index: 2;
  height: 620px;
  left: 0px;
}

/* p::before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  bottom: 100%;
  left: 1.5em;
  border: 0.75rem solid transparent;
  border-top: none;

  border-bottom-color: #fff;
  filter: drop-shadow(0 -0.0625rem 0.0625rem rgba(0, 0, 0, 0.1));
} */



</style>
