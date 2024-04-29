//Formulario para comprobación de los campos del formulario

function validate_form_data() {
    var data_nombre = document.getElementById("nombre").value
    var data_apellido1 = document.getElementById("apellido1").value
    var data_apellido2 = document.getElementById("apellido2").value
    var data_telefono = document.getElementById("telefono").value
    var data_edad = document.getElementById("edad").value
    var data_contrasena = document.getElementById("contrasena").value

    if (check_nombre(data_apellido1) && check_nombre(data_apellido2) && check_nombre(data_nombre)
        && (check_edad(data_edad)) && check_telefono(data_telefono) && check_contrasena(data_contrasena)) {
        return true
    } else {
        return false
    }
}

function check_contrasena(data_contrasena) {
    if (data_contrasena.length < 1) {
        alert("No puedes dejar la contraseña en blanco")
        return false
    }
    else return true
}

function check_telefono(data_telefono) {
    //En esta función comprobamos si se han introducido 9 carácteres y que todos
    //ellos sean numéricos
    if (((data_telefono.length == 9)) && (data_telefono.match(/^[0-9]+$/) != null)) {
        return true
    } else {
        alert('El teléfono debe contener solo números y 9 caracteres')
        return false
    }
}

function check_nombre(data) {
    //Comprobamos que los datos introducidos sean todos letras espacios o
    //letras acentuadas
    var regex = /^[a-zA-ZÀ-ÿ ]+$/
    if (regex.test(data)) {
        return true
    } else {
        alert("Los campos nombre y apellidos únicamente deben contener letras, letras acentuadas o espacios")
        return false
    }
}

function check_edad(data_edad) {
    //Comprobamos que el valor sea numérico y menor de 100
    if (((data_edad < 100)) && (data_edad.match(/^[0-9]+$/) != null)) return true
    else {
        alert("La edad debe ser un valor númerico menor de 100")
        return false
    }
}