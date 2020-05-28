window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("bEnviar").addEventListener('click', validaDescripcion, false);
    document.getElementById("poliza").addEventListener('change',validaNumPoliza);
    document.getElementById("tipo_accidente").addEventListener('change',validaAccidente);
    document.getElementById("taller").addEventListener('change',validaTaller);
    document.getElementById("asegurado_rut").addEventListener('change',validaRutAsegurado);
    document.getElementById("descripcion").addEventListener('keyup',validaDescripcion,false);
    
}

function validaNumPoliza() {
    var elemento = document.getElementById("poliza");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_poliza(elemento, "Debe seleccionar N° Póliza")
        }
        return false;
    }
    clearErrorPoliza(elemento);
    return true;

}

function error_poliza(elemento, mensaje) {
    document.getElementById("error_poliza").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
    elemento.focus();
}

function clearErrorPoliza(elemento) {
    document.getElementById("error_poliza").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaAccidente() {
    var elemento = document.getElementById("tipo_accidente");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_accidente(elemento, "Debe seleccionar tipo accidente")
        }
        return false;
    }
    clearErrorAccidente(elemento);
    return true;

}

function error_accidente(elemento, mensaje) {
    document.getElementById("error_tipo").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorAccidente(elemento) {
    document.getElementById("error_tipo").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaTaller() {
    var elemento = document.getElementById("taller");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_taller(elemento, "Debe seleccionar taller")
        }
        return false;
    }
    clearErrorTaller(elemento);
    return true;

}

function error_taller(elemento, mensaje) {
    document.getElementById("error_taller").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorTaller(elemento) {
    document.getElementById("error_taller").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaRutAsegurado() {
    var elemento = document.getElementById("asegurado_rut");
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
    document.getElementById("error_rut_asegurado").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorRut(elemento) {
    document.getElementById("error_rut_asegurado").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaDescripcion(e) {
    var elemento = document.getElementById("descripcion");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_descripcion(elemento, "Debe ingresar descripción")
        }
        e.preventDefault();
        return false;
    }
    if (document.getElementById("descripcion").value.length < 20) {
        error_descripcion(elemento, "Debe contener mínimo 20 caracteres");
        e.preventDefault();
        return false;
    }
    clearErrorDescripcion(elemento);
    return true;
}

function error_descripcion(elemento, mensaje) {
    document.getElementById("error_descripcion").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorDescripcion(elemento) {
    document.getElementById("error_descripcion").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validar(e) {
    if (validaNumPoliza() || validaAccidente() || validaTaller() || validaRutAsegurado() || validaDescripcion()) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



