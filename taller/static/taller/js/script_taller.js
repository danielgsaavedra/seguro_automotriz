$(document).ready(function (){
    
    function actualizar(){location.reload();}

    var ShowFormActaRecepcion = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_acta_recepcion').modal('show')
            },
            success: function (data) {
                $('#modal_acta_recepcion .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormActaRecepcion = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_siniestro_recepcion tbody').html(data.siniestros);
                    $('#modal_acta_recepcion').modal('hide');
                    console.log('Success!');
                    toastr.success('Operación Exitosa!');
                    setTimeout(actualizar,500);
                    
                } else {
                    $('#modal_acta_recepcion .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    $('.show_acta_recepcion').click(ShowFormActaRecepcion);
    $('#modal_acta_recepcion').on('submit', '.create_form_acta_recepcion', SaveFormActaRecepcion);


    var ShowFormActaRetiro = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_acta_retiro').modal('show')
            },
            success: function (data) {
                $('#modal_acta_retiro .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormActaRetiro = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_siniestro_retiro tbody').html(data.siniestros);
                    $('#modal_acta_retiro').modal('hide');
                    console.log('Success!');
                    toastr.success('Operación Exitosa!');
                    setTimeout(actualizar,500);
                } else {
                    $('#modal_acta_retiro .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    $('.show_acta_retiro').click(ShowFormActaRetiro);
    $('#modal_acta_retiro').on('submit', '.create_form_acta_retiro', SaveFormActaRetiro);


    var ShowFormActaRechazo = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_acta_rechazo').modal('show')
            },
            success: function (data) {
                $('#modal_acta_rechazo .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormActaRechazo = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_siniestro_retiro tbody').html(data.siniestros);
                    $('#modal_acta_rechazo').modal('hide');
                    console.log('Success!');
                    toastr.success('Operación Exitosa!');
                    setTimeout(actualizar,500);
                } else {
                    $('#modal_acta_rechazo .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    $('.show_acta_rechazo').click(ShowFormActaRechazo);
    $('#modal_acta_rechazo').on('submit', '.create_form_acta_rechazo', SaveFormActaRechazo);


    var ShowFormInformeDanos = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_info_dano').modal('show')
            },
            success: function (data) {
                $('#modal_info_dano .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormInformeDanos = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_info_dano tbody').html(data.siniestros);
                    $('#modal_info_dano').modal('hide');
                    console.log('Success!');
                    toastr.success('Operación Exitosa!');
                    setTimeout(actualizar,400);
                } else {
                    $('#modal_info_dano .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    $('.show_info_dano').click(ShowFormInformeDanos);
    $('#modal_info_dano').on('submit', '.create_form_info_dano', SaveFormInformeDanos);

});