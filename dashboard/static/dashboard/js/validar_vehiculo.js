window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("patente").addEventListener('keyup', validaPatente);
    document.getElementById("modelo").addEventListener('keyup', validaModelo);
    document.getElementById("motor").addEventListener('keyup', validaMotor);
    document.getElementById("anio").addEventListener('keyup', validaAnio);
    document.getElementById("marca_vehi").addEventListener('change', validaMarca);
    document.getElementById("tipo_vehi").addEventListener('change', validaTipo);
    document.getElementById("rut_asegurado_vehi").addEventListener('change', validaRutAsegurado);
}

function validaPatente() {
    var elemento = document.getElementById("patente");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_patente(elemento, "Debe introducir patente")
        }
        if (elemento.validity.patternMismatch) {
            error_patente(elemento, "Ingresa patente con '-' (XX-XX-XX)");
        }
        return false;
    }
    clearErrorPatente(elemento);
    return true;

}

function error_patente(elemento, mensaje) {
    document.getElementById("error_patente").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
    elemento.focus();
}

function clearErrorPatente(elemento) {
    document.getElementById("error_patente").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaModelo() {
    var elemento = document.getElementById("modelo");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_modelo(elemento, "Debe introducir modelo")
        }
        if (elemento.validity.patternMismatch) {
            error_modelo(elemento, "Debe contener al menos 4 caracteres");
        }
        return false;
    }
    clearErrorModelo(elemento);
    return true;

}

function error_modelo(elemento, mensaje) {
    document.getElementById("error_modelo").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorModelo(elemento) {
    document.getElementById("error_modelo").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaMotor() {
    var elemento = document.getElementById("motor");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_motor(elemento, "Debe introducir N° de motor")
        }
        if (elemento.validity.patternMismatch) {
            error_motor(elemento, "Debe contener al menos 4 caracteres");
        }
        return false;
    }
    clearErrorMotor(elemento);
    return true;

}

function error_motor(elemento, mensaje) {
    document.getElementById("error_motor").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorMotor(elemento) {
    document.getElementById("error_motor").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaAnio() {
    var elemento = document.getElementById("anio");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_anio(elemento, "Debe introducir Año")
        }
        if (elemento.validity.patternMismatch) {
            error_anio(elemento, "Ingrese solo Año (YYYY)");
        }
        return false;
    }
    clearErrorAnio(elemento);
    return true;
}

function error_anio(elemento, mensaje) {
    document.getElementById("error_anio").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorAnio(elemento) {
    document.getElementById("error_anio").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaMarca() {
    var elemento = document.getElementById("marca_vehi");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_marca(elemento, "Debe seleccionar marca")
        }
        return false;
    }
    clearErrorMarca(elemento);
    return true;
}

function error_marca(elemento, mensaje) {
    document.getElementById("error_marca").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorMarca(elemento) {
    document.getElementById("error_marca").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaTipo() {
    var elemento = document.getElementById("tipo_vehi");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_tipo(elemento, "Debe seleccionar tipo vehículo")
        }
        return false;
    }
    clearErrorTipo(elemento);
    return true;
}

function error_tipo(elemento, mensaje) {
    document.getElementById("error_tipo").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorTipo(elemento) {
    document.getElementById("error_tipo").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaRutAsegurado() {
    var elemento = document.getElementById("rut_asegurado_vehi");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_rut(elemento, "Debe seleccionar RUT asegurado")
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

function validar(e) {
    if (validaPatente() && validaModelo() && validaMotor() && validaAnio() && validaMarca() && validaTipo() && validaRutAsegurado()) {
        document.getElementById("patente").disabled = false;
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



