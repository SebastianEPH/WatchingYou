function sendData() {
	var nickname = document.getElementById("username").value
	var tele_id = document.getElementById("tele_id").value
	console.log("init")
	eel.send_values(nickname, tele_id)//(setImage)

	console.log('funcion')
	window.location.href = "on-line.html"
	//eel.get_id_telegram(tele_id)
}
function retry(){
    eel.stop___()(()=>{
    	window.location.href = "index.html"
	})
}
function stopped(){
	eel.start___()(()=>{
		window.location.href = "stopped.html"
	})
}
function __exit(){
	eel.exit___()(()=>{
		window.close();
		return false
	})
}


