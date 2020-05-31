window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("fecha_fin").addEventListener('change', validaFin);
    document.getElementById("poli_rut_asegurado").addEventListener('change', validaRutAsegurado);
    document.getElementById("poli_patente").addEventListener('change', validaPatente);
}

function validaFin() {
    var elemento = document.getElementById("fecha_fin");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_fin(elemento, "Debe introducir fecha de termino");
        }
        return false;
    }
    clearErrorFin(elemento);
    return true;
}

function error_fin(elemento, mensaje) {
    document.getElementById("error_fin").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorFin(elemento) {
    document.getElementById("error_fin").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaRutAsegurado() {
    var elemento = document.getElementById("poli_rut_asegurado");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_rut(elemento, "Debe seleccionar RUT asegurado");
        }
        return false;
    }
    clearErrorRut(elemento);
    return true;
}

function error_rut(elemento, mensaje) {
    document.getElementById("error_rut").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorRut(elemento) {
    document.getElementById("error_rut").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaPatente() {
    var elemento = document.getElementById("poli_patente");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_patente(elemento, "Debe seleccionar patente");
        }
        return false;
    }
    clearErrorPatente(elemento);
    return true;
}

function error_patente(elemento, mensaje) {
    document.getElementById("error_patente").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorPatente(elemento) {
    document.getElementById("error_patente").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validar(e) {
    if (validaFin() && validaRutAsegurado() && validaPatente()) {
        document.getElementById("poli_patente").disabled = false;
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



