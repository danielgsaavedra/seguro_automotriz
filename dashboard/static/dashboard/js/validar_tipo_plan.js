window.onload = iniciar();

function iniciar() {
    document.getElementById("bEnviar").addEventListener('click', validar, false);
    document.getElementById("nombre_tipo").addEventListener('keyup', validaNombre);
    document.getElementById("valor_tipo_plan").addEventListener('keyup', validaValor);
    document.getElementById("valor_tipo_plan").addEventListener('keydown', function (evento) {
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
            document.getElementById('valor_tipo_plan').value.length === 0 &&
            teclaPresionada == 0;

        if (sePresionoUnaTeclaNoAdmitida || comienzaPorCero) {
            evento.preventDefault();
        }

    });
    document.getElementById("deducible").addEventListener('keyup', validaDeducible);
    document.getElementById("cobertura").addEventListener('keyup', validaCobertura);
    document.getElementById("cobertura").addEventListener('keydown', function (evento) {
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
            document.getElementById('cobertura').value.length === 0 &&
            teclaPresionada == 0;

        if (sePresionoUnaTeclaNoAdmitida || comienzaPorCero) {
            evento.preventDefault();
        }

    });
    document.getElementById("descripcion").addEventListener('keyup', validaDescripcion, false);

}

function validaNombre() {
    var elemento = document.getElementById("nombre_tipo");
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

function validaValor() {
    var elemento = document.getElementById("valor_tipo_plan");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_valor(elemento, "Debe ingresar valor")
        }
        return false;
    }
    clearErrorValor(elemento);
    return true;

}

function error_valor(elemento, mensaje) {
    document.getElementById("error_valor").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorValor(elemento) {
    document.getElementById("error_valor").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaDeducible() {
    var elemento = document.getElementById("deducible");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_deducible(elemento, "Debe ingresar deducible");
        }
        if (elemento.validity.patternMismatch) {
            error_deducible(elemento, "Deben ser solo números");
        }
        return false;
    }
    clearErrorDeducible(elemento);
    return true;

}

function error_deducible(elemento, mensaje) {
    document.getElementById("error_deducible").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorDeducible(elemento) {
    document.getElementById("error_deducible").innerHTML = "";
    elemento.className = "form-control is-valid";
}

function validaCobertura() {
    var elemento = document.getElementById("cobertura");
    if (!elemento.checkValidity()) {
        if (elemento.validity.valueMissing) {
            error_cobertura(elemento, "Debe ingresar cobertura");
        }
        return false;
    }
    clearErrorCobertura(elemento);
    return true;
}

function error_cobertura(elemento, mensaje) {
    document.getElementById("error_cobertura").innerHTML = mensaje;
    elemento.className = "form-control is-invalid";
}

function clearErrorCobertura(elemento) {
    document.getElementById("error_cobertura").innerHTML = "";
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
    if (document.getElementById("descripcion").value.length < 10) {
        error_descripcion(elemento, "Debe contener mínimo 10 caracteres");
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
    if (validaNombre() && validaValor() && validaDeducible() && validaCobertura() && validaDescripcion()) {
        return true
    } else {
        e.preventDefault();
        return false;
    }
}



