<template>
  <div class="htmlku" >
    <!-- <div class="particle-container">
      <div class="particles">
          <span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span><span class="circle"></span
          ><span class="circle"></span>
        </div>
      </div> -->

      <v-container class="py-4">
      <div class="text-h1 textku playful text-center font-weight-black">
        <span aria-hidden="true">T</span>
        <span aria-hidden="true">I</span>
        <span aria-hidden="true">C</span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"><br /></span>
        <span aria-hidden="true">T</span>
        <span aria-hidden="true">A</span>
        <span aria-hidden="true">C</span>
        <span aria-hidden="true"><br /> </span>
        <span aria-hidden="true">T</span>
        <span aria-hidden="true">O</span>
        <span aria-hidden="true">E</span>
      </div>
      <v-row class="justify-center mt-6" style="padding-bottom: 200px;">
        <v-col cols="12" class="">
          <div class="d-flex justify-center">
            <button class="mulaiawal grey--text text--darken-4 pa-4" @click="$router.push('/play')">
              Mulai Permainan
            </button>
          </div>
        </v-col>
        <v-col cols="12">
          <div class="d-flex justify-center">
            <button class="mulaiawal grey--text text--darken-4 pa-4" @click="$router.push('/carabermain')">
              Cara Bermain
            </button>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {};
</script>
<style >

@import url("https://fonts.googleapis.com/css?family=Rubik:700&display=swap");
html .htmlku  {
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

* {
  box-sizing: border-box;
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

button.mulaiawal {
  font-weight: 600;
  color: var(--text);
  background: var(--light-wrnaku);
  border: 2px solid var(--wrnaku-border);
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1),
    background 150ms cubic-bezier(0, 0, 0.58, 1);
}

button.mulaiawal::before {
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

button.mulaiawal:hover {
  background: var(--wrnaku);
  transform: translate(0, 0.25em);
}

button.mulaiawal:hover::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0.5em 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0.5em, -1em);
}

button.mulaiawal:active {
  background: var(--wrnaku);
  transform: translate(0em, 0.65em);
}

button.mulaiawal:active::before {
  box-shadow: 0 0 0 2px var(--wrnaku-border), 0 0 var(--wrnaku-shadow);
  transform: translate3d(0, 0, -1em);
}
</style>
<style lang="scss" scoped>
@function textShadow($precision, $size, $color) {
  $value: null;
  $offset: 0;
  $length: $size * (1 / $precision) - 1;

  @for $i from 0 through $length {
    $offset: $offset + $precision;
    $shadow: $offset + px $offset + px $color;
    $value: append($value, $shadow, comma);
  }

  @return $value;
}

.playful span {
  position: relative;
  color: #fff8e1;
  text-shadow: textShadow(0.25, 6, #ffca28);
  animation: scatter 1.75s infinite;
}

.playful span:nth-child(2n) {
  color: #fff8e1;
  text-shadow: textShadow(0.25, 6, #ffca28);
  animation-delay: 0.3s;
}

.playful span:nth-child(3n) {
  color: #fff8e1;
  text-shadow: textShadow(0.25, 6, #ffca28);
  animation-delay: 0.15s;
}

.playful span:nth-child(5n) {
  color: #fff8e1;
  text-shadow: textShadow(0.25, 6, #ffca28);
  animation-delay: 0.4s;
}

.playful span:nth-child(7n),
.playful span:nth-child(11n) {
  color: #fff8e1;
  text-shadow: textShadow(0.25, 6, #ffca28);
  animation-delay: 0.25s;
}

@keyframes scatter {
  0% {
    top: 0;
  }
  50% {
    top: -10px;
  }
  100% {
    top: 0;
  }
}

// .circle {
//   border-radius: 50%;
//   position: absolute;
//   // z-index: 1;
// }
// //use a for loop to create a unique keyframe for each element
// //then apply randomized styles to them all
// @for $i from 1 through 31 {
//   @-webkit-keyframes particle-animation-#{$i} {
//     0% {
//       -webkit-transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(90) + deg);
//       transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(90) + deg);
//     }
//     100% {
//       -webkit-transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(180) + deg);
//       transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(180) + deg);
//     }
//   }
//   @keyframes particle-animation-#{$i} {
//     0% {
//       -webkit-transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(110) * 1px)
//         )
//         rotate(random(90) + deg);
//       transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(90) + deg);
//     }
//     100% {
//       -webkit-transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(180) + deg);
//       transform: translate3d(
//           (random(110) * 1vw),
//           (random(100) * 1vh),
//           (random(400) * 1px)
//         )
//         rotate(random(180) + deg);
//     }
//   }

//   //fade in and out
//   @-webkit-keyframes fade-frames {
//     0% {
//       opacity: 0;
//     }
//     25% {
//       opacity: 0.5;
//     }
//     100% {
//       opacity: 1;
//     }
//     75% {
//       opacity: 0.5;
//     }
//     100% {
//       opacity: 0;
//     }
//   }
//   @keyframes fade-frames {
//     0% {
//       opacity: 0;
//     }
//     25% {
//       opacity: 0.5;
//     }
//     100% {
//       opacity: 1;
//     }
//     75% {
//       opacity: 0.5;
//     }
//     100% {
//       opacity: 0;
//     }
//   }

//   //apply keyframes to children of .particles - the circles
//   //and make them a random size, color, and delay
//   .particles span:nth-child(#{$i}) {
//     -webkit-animation: particle-animation-#{$i} 10s ease-in infinite,
//       fade-frames 10s ease-in-out infinite;
//     animation: particle-animation-#{$i} 10s ease-in infinite,
//       fade-frames 10s ease-in-out infinite;
//     $size: random(100) + 1 + px;
//     height: $size;
//     width: $size;
//     $color: random(255);
//     //this will make them all a random shade of greyish
//     background-color: rgb($color, $color, $color);
//     -webkit-animation-delay: -$i + s;
//     animation-delay: -$i + s;
//     // -webkit-transform: translate3d((random(90) * 1vw), (random(90) * 1vh), (random(100) * 1px));
//     // transform: translate3d((random(90) * 1vw), (random(90) * 1vh), (random(100) * 1px));
  // }
// }
</style>
