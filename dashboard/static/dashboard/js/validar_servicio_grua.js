window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("nombre_servicio").addEventListener('keyup', validaNombre);
    document.getElementById("razon_social_servicio").addEventListener('keyup', validaRazon);
    document.getElementById("telefono_servicio").addEventListener('keyup', validaTelefono);
    document.getElementById("correo_servicio").addEventListener('keyup', validaCorreo);
    document.getElementById("direccion").addEventListener('keyup', validaDireccion);
    document.getElementById("comuna").addEventListener('change', validaComuna);
}

function validaNombre() {
    var elemento = document.getElementById("nombre_servicio");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_nombre(elemento, "Debe ingresar nombre")
        }
        if (elemento.validity.patternMismatch) {
            error_nombre(elemento, "Debe contener al menos 3 caracteres");
        }
        return false;
    }
    clearErrorNombre(elemento);
    return true;

}

function error_nombre(elemento, mensaje) {
    document.getElementById("error_nombre").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
    elemento.focus();
}

function clearErrorNombre(elemento) {
    document.getElementById("error_nombre").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaRazon() {
    var elemento = document.getElementById("razon_social_servicio");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_razon(elemento, "Debe ingresar razón social")
        }
        if (elemento.validity.patternMismatch) {
            error_razon(elemento, "Debe contener al menos 4 caracteres");
        }
        return false;
    }
    clearErrorRazon(elemento);
    return true;

}

function error_razon(elemento, mensaje) {
    document.getElementById("error_razon").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorRazon(elemento) {
    document.getElementById("error_razon").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaTelefono() {
    var elemento = document.getElementById("telefono_servicio");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_telefono(elemento, "Debe ingresar telefono");
        }
        if (elemento.validity.patternMismatch) {
            error_telefono(elemento, "Debe contener 9 dígitos");
        }
        return false;
    }
    clearErrorTelefono(elemento);
    return true;

}

function error_telefono(elemento, mensaje) {
    document.getElementById("error_telefono").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorTelefono(elemento) {
    document.getElementById("error_telefono").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaCorreo() {
    var elemento = document.getElementById("correo_servicio");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_correo(elemento, "Debe ingresar correo");
        }
        if (elemento.validity.patternMismatch) {
            error_correo(elemento, "Debe ingresar un correo válido");
        }
        return false;
    }
    clearErrorCorreo(elemento);
    return true;
}

function error_correo(elemento, mensaje) {
    document.getElementById("error_correo").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorCorreo(elemento) {
    document.getElementById("error_correo").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaDireccion() {
    var elemento = document.getElementById("direccion");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_direccion(elemento, "Debe ingresar dirección")
        }
        if (elemento.validity.patternMismatch) {
            error_direccion(elemento, "Debe contener al menos 4 caracteres");
        }
        return false;
    }
    clearErrorDireccion(elemento);
    return true;

}

function error_direccion(elemento, mensaje) {
    document.getElementById("error_direccion").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorDireccion(elemento) {
    document.getElementById("error_direccion").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaComuna() {
    var elemento = document.getElementById("comuna");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_comuna(elemento, "Debe seleccionar una comuna")
        }
        return false;
    }
    clearErrorComuna(elemento);
    return true;

}

function error_comuna(elemento, mensaje) {
    document.getElementById("error_comuna").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorComuna(elemento) {
    document.getElementById("error_comuna").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validar(e) {
    if (validaNombre() && validaRazon() && validaDireccion() && validaComuna() && validaTelefono() && validaCorreo()) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



