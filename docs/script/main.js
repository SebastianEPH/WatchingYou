
let $ficha_tecnica= document.getElementById('ficha_tecnica')
let $manual_user= document.getElementById('manual_user')
let $manual_docente = document.getElementById('manual_docente')
let $main = document.getElementById('main')
let $code_documentation = document.getElementById('code_documentation')
let $about = document.getElementById('about')

function all(){
    $manual_docente.style.display = 'none'
    $manual_user.style.display = 'none'
    $ficha_tecnica.style.display = 'none'
    $main.style.display = 'none'
    $code_documentation.style.display = 'none'
    $about.style.display = 'none'
}
function main(){
    all()
    $main.style.display = 'block'
}

function fichaTecnica(){
    all()
    $ficha_tecnica.style.display = 'block'
}
function manualUser(){
    all()
    $manual_user.style.display = 'block'
}
function manualDocente(){
    all()
    $manual_docente.style.display = 'block'
}
function code_documentation(){
    all()
    $code_documentation.style.display = 'block'
}
function about(){
    all()
    $about.style.display = 'block'
}

code_documentation()

