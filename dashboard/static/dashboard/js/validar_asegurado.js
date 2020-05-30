window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("id_rut_asegurado").addEventListener('keyup',validaRut);
    document.getElementById("p_nombre_asegurado").addEventListener('keyup',validaPrimerNombre);
    document.getElementById("telefono_asegurado").addEventListener('keyup',validaTelefono);
    document.getElementById("s_nombre_asegurado").addEventListener('keyup',validaSegundoNombre);
    document.getElementById("p_apellido_asegurado").addEventListener('keyup',validaPrimerApellido);
    document.getElementById("s_apellido_asegurado").addEventListener('keyup',validaSegundoApellido);
    document.getElementById("correo_asegurado").addEventListener('keyup',validaCorreo);
    document.getElementById("fecha_asegurado").addEventListener('change',validaFecha);
}

function validaRut() {
    var elemento = document.getElementById("id_rut_asegurado");
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
    elemento.focus();
}

function clearErrorRut(elemento) {
    document.getElementById("error_rut").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPrimerNombre() {
    var elemento = document.getElementById("p_nombre_asegurado");
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
    var elemento = document.getElementById("s_nombre_asegurado");
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
    var elemento = document.getElementById("p_apellido_asegurado");
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
    var elemento = document.getElementById("s_apellido_asegurado");
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
    var elemento = document.getElementById("telefono_asegurado");
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
    var elemento = document.getElementById("correo_asegurado");
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

function validaFecha() {
    var elemento = document.getElementById("fecha_asegurado");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_fecha(elemento, "Debe introducir fecha de nacimiento");
        }
        return false;
    }
    clearErrorFecha(elemento);
    return true;
}

function error_fecha(elemento,mensaje) {
    document.getElementById("error_fecha").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorFecha(elemento) {
    document.getElementById("error_fecha").innerHTML = "";
    elemento.className = "form-control is-valid";
}


function validar(e) {
    if (validaRut() || validaPrimerNombre() || validaTelefono() || validaSegundoNombre() 
    || validaPrimerApellido() || validaSegundoApellido() || validaCorreo() || validaFecha()) {
        return true 
    } else {
        e.preventDefault();
        return false;
    }
}



