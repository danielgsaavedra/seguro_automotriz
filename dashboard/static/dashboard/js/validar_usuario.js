window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("bEnviar").addEventListener('click', validaPassword2, false);
    document.getElementById("id_rut_usuario").addEventListener('keyup',validaRut);
    document.getElementById("p_nombre_usuario").addEventListener('keyup',validaPrimerNombre);
    document.getElementById("telefono_usuario").addEventListener('keyup',validaTelefono);
    document.getElementById("s_nombre_usuario").addEventListener('keyup',validaSegundoNombre);
    document.getElementById("p_apellido_usuario").addEventListener('keyup',validaPrimerApellido);
    document.getElementById("s_apellido_usuario").addEventListener('keyup',validaSegundoApellido);
    document.getElementById("email_usuario").addEventListener('keyup',validaCorreo);
    document.getElementById("rol_usuario").addEventListener('change',validaRol);
    document.getElementById("password1").addEventListener('keyup',validaPassword1);
    document.getElementById("password2").addEventListener('keyup',validaPassword2);
}

function validaRut() {
    var elemento = document.getElementById("id_rut_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_rut(elemento, "Debe introducir un Rut");
        }
        if (elemento.validity.patternMismatch) {
            error_rut(elemento, "Debe ingresar un Rut válido");
        }
        return false;
    }
    clearErrorRut(elemento);
    return true;

}

function error_rut(elemento,mensaje) {
    document.getElementById("error_rut").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorRut(elemento) {
    document.getElementById("error_rut").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPrimerNombre() {
    var elemento = document.getElementById("p_nombre_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_p_nombre(elemento, "Debe introducir primer nombre");
        }
        if (elemento.validity.patternMismatch) {
            error_p_nombre(elemento, "Debe contener al menos 3 caracteres");
        }
        return false;
    }
    clearErrorPNombre(elemento);
    return true;
}

function error_p_nombre(elemento,mensaje) {
    document.getElementById("error_p_nombre").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorPNombre(elemento) {
    document.getElementById("error_p_nombre").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaSegundoNombre() {
    var elemento = document.getElementById("s_nombre_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_s_nombre(elemento, "Debe introducir segundo nombre");
        }
        if (elemento.validity.patternMismatch) {
            error_s_nombre(elemento, "Debe contener al menos 3 caracteres");
        }
        return false;
    }
    clearErrorSNombre(elemento);
    return true;
}

function error_s_nombre(elemento,mensaje) {
    document.getElementById("error_s_nombre").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorSNombre(elemento) {
    document.getElementById("error_s_nombre").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPrimerApellido() {
    var elemento = document.getElementById("p_apellido_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_p_apellido(elemento, "Debe introducir primer apellido");
        }
        if (elemento.validity.patternMismatch) {
            error_p_apellido(elemento, "Debe contener al menos 3 caracteres");
        }
        return false;
    }
    clearErrorPApellido(elemento);
    return true;
}

function error_p_apellido(elemento,mensaje) {
    document.getElementById("error_p_apellido").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorPApellido(elemento) {
    document.getElementById("error_p_apellido").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaSegundoApellido() {
    var elemento = document.getElementById("s_apellido_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_s_apellido(elemento, "Debe introducir segundo apellido");
        }
        if (elemento.validity.patternMismatch) {
            error_s_apellido(elemento, "Debe contener al menos 3 caracteres");
        }
        return false;
    }
    clearErrorSApellido(elemento);
    return true;
}

function error_s_apellido(elemento,mensaje) {
    document.getElementById("error_s_apellido").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorSApellido(elemento) {
    document.getElementById("error_s_apellido").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaTelefono() {
    var elemento = document.getElementById("telefono_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_telefono(elemento, "Debe introducir telefono");
        }
        if (elemento.validity.patternMismatch) {
            error_telefono(elemento, "Debe contener 9 dígitos");
        }
        return false;
    }
    clearErrorTelefono(elemento);
    return true;

}

function error_telefono(elemento,mensaje) {
    document.getElementById("error_telefono").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorTelefono(elemento) {
    document.getElementById("error_telefono").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaCorreo() {
    var elemento = document.getElementById("email_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_correo(elemento, "Debe introducir correo");
        }
        if (elemento.validity.patternMismatch) {
            error_correo(elemento, "Debe ingresar un correo válido");
        }
        return false;
    }
    clearErrorCorreo(elemento);
    return true;
}

function error_correo(elemento,mensaje) {
    document.getElementById("error_correo").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorCorreo(elemento) {
    document.getElementById("error_correo").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaRol() {
    var elemento = document.getElementById("rol_usuario");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_rol(elemento, "Debe seleccionar un rol");
        }
        return false;
    }
    clearErrorRol(elemento);
    return true;
}

function error_rol(elemento,mensaje) {
    document.getElementById("error_rol").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
    elemento.focus();
}

function clearErrorRol(elemento) {
    document.getElementById("error_rol").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPassword1() {
    var elemento = document.getElementById("password1");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_password1(elemento, "Debe ingresar una contraseña");
        }
        if (elemento.validity.patternMismatch) {
            error_password1(elemento, "La contraseña debe contener entre 5 y 12 caracteres");
        }
        return false;
    }
    clearErrorPassword1(elemento);
    return true;
}

function error_password1(elemento,mensaje) {
    document.getElementById("error_password1").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorPassword1(elemento) {
    document.getElementById("error_password1").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPassword2(e) {
    var elemento = document.getElementById("password2");
    var password = document.getElementById("password1").value;
    
    if (elemento.value != password || elemento.value == "") {
        error_password2(elemento, "Contraseña no coincide");
        e.preventDefault();
        return false;
    }
    clearErrorPassword2(elemento);
    return true;
}

function error_password2(elemento,mensaje) {
    document.getElementById("error_password2").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorPassword2(elemento) {
    document.getElementById("error_password2").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validar(e) {
    if (validaRol() && validaRut() && validaTelefono() && validaPrimerNombre()  && validaSegundoNombre() 
    && validaPrimerApellido() && validaSegundoApellido() && validaCorreo() &&  validaPassword1() && validaPassword2()) {
        return true 
    } else {
        e.preventDefault();
        return false;
    }
}



