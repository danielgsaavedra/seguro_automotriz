window.onload = iniciar();
function iniciar() {
    var element = document.getElementById('patente');
    var caseMask = IMask(element, {
        mask: 'aa-**-00',
        prepare: function (str) {
            return str.toUpperCase();
        },
    });
}