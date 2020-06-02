window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("bEnviar").addEventListener('click', validaObservaciones, false);
    document.getElementById("observaciones").addEventListener('keyup', validaObservaciones, false);
    document.getElementById("sev_dano").addEventListener('change', validaSevDanos);
    document.getElementById("tipo_dano").addEventListener('change', validaTipoDanos);
}

function validaObservaciones(e) {
    var elemento = document.getElementById("observaciones");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_observaciones(elemento, "Debe ingresar observaciones")
        }
        e.preventDefault();
        return false;
    }
    if (document.getElementById("observaciones").value.length < 20) {
        error_observaciones(elemento, "Debe contener mínimo 20 caracteres");
        e.preventDefault();
        return false;
    }
    clear_error_observaciones(elemento);
    return true;
}

function error_observaciones(elemento, mensaje) {
    document.getElementById("error_observaciones").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clear_error_observaciones(elemento) {
    document.getElementById("error_observaciones").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaSevDanos(e) {
    var elemento = document.getElementById("sev_dano");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_sevDanos(elemento, "Debe seleccionar severidad de daños")
        }
        e.preventDefault();
        return false;
    }
    clear_error_sevDanos(elemento);
    return true;
}

function error_sevDanos(elemento, mensaje) {
    document.getElementById("error_sev_danos").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clear_error_sevDanos(elemento) {
    document.getElementById("error_sev_danos").innerHTML = "";
    elemento.className = "form-control is-valid";
}


function validaTipoDanos(e) {
    var elemento = document.getElementById("tipo_dano");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_tipoDanos(elemento, "Debe seleccionar tipo de daños")
        }
        e.preventDefault();
        return false;
    }
    clear_error_sevDanos(elemento);
    return true;
}

function error_tipoDanos(elemento, mensaje) {
    document.getElementById("error_tipo_dano").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clear_error_tipoDanos(elemento) {
    document.getElementById("error_tipo_dano").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validar(e) {
    if (validaTipoDanos() && validaSevDanos() && validaObservaciones()) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}
