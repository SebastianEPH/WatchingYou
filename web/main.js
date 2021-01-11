function sendData() {
	var fullname = document.getElementById("username").value
	var tele_id = document.getElementById("tele_id").value
	eel.check_id(tele_id, fullname)((pass_id)=>{
		if (pass_id){
			console.log('El ID es aceptado')
			eel.start_software()//(setImage)
			window.location.href = "on-line.html"
		}else{
			console.log('El ID fue rechazado ')
			window.location.href = "index_fail.html"

		}
	})

	console.log("init")

	console.log('pasando.... ')
	//window.location.href = "on-line.html"
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


