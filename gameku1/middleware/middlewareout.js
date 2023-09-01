export default function({ redirect, app}){

  const authToken = app.$cookies.get('setgamemulai');
  if(authToken){
    return redirect('/game')
  }
}
