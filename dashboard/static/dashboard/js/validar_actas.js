window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("bEnviar").addEventListener('click', validaObservaciones, false);
    document.getElementById("observaciones").addEventListener('keyup', validaObservaciones, false);
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

function validar(e) {
    if (validaObservaciones()) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}
