function sendData() {
	var nickname = document.getElementById("username").value
	var tele_id = document.getElementById("tele_id").value
	eel.send_values(nickname, tele_id)//(setImage)
	window.location.href = "start.html"

	//eel.get_id_telegram(tele_id)
}
function stop(){
    eel.start(isActive = false)//(setImage)



}
function init(){

	eel.start(isActive = true)//(setImage)


}
function setImage(base64) {
	document.getElementById("qr").src = base64
}

function red_start(){   // Redirteccionar
    window.location.href = "stop.html"
}
function red_stop(){    // Redireccionar
     window.location.href = "index.html"
}