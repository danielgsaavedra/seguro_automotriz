window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("nombre_taller").addEventListener('keyup', validaNombre);
    document.getElementById("razon_social").addEventListener('keyup', validaRazon);
    document.getElementById("telefono_taller").addEventListener('keyup', validaTelefono);
    document.getElementById("correo_taller").addEventListener('keyup', validaCorreo);
    document.getElementById("capacidad").addEventListener('keyup', validaCapacidad);
    document.getElementById('capacidad').addEventListener('keydown', function (evento) {
        const teclaPresionada = evento.key;
        const teclaPresionadaEsUnNumero =
            Number.isInteger(parseInt(teclaPresionada));

        const sePresionoUnaTeclaNoAdmitida =
            teclaPresionada != 'ArrowDown' &&
            teclaPresionada != 'ArrowUp' &&
            teclaPresionada != 'ArrowLeft' &&
            teclaPresionada != 'ArrowRight' &&
            teclaPresionada != 'Backspace' &&
            teclaPresionada != 'Delete' &&
            teclaPresionada != 'Enter' &&
            !teclaPresionadaEsUnNumero;
        const comienzaPorCero =
        document.getElementById('capacidad').value.length === 0 &&
            teclaPresionada == 0;

        if (sePresionoUnaTeclaNoAdmitida || comienzaPorCero) {
            evento.preventDefault();
        }

    });
}

function validaNombre() {
    var elemento = document.getElementById("nombre_taller");
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
    var elemento = document.getElementById("razon_social");
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
    var elemento = document.getElementById("telefono_taller");
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
    var elemento = document.getElementById("correo_taller");
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

function validaCapacidad() {
    var elemento = document.getElementById("capacidad");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_capacidad(elemento, "Debe ingresar capacidad");
        }
        return false;
    }
    clearErrorCapacidad(elemento);
    return true;
}

function error_capacidad(elemento, mensaje) {
    document.getElementById("error_capacidad").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorCapacidad(elemento) {
    document.getElementById("error_capacidad").innerHTML = "";
    elemento.className = "form-control is-valid";
}



function validar(e) {
    if (validaNombre() && validaRazon() && validaTelefono() && validaCapacidad() && validaCorreo() ) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



