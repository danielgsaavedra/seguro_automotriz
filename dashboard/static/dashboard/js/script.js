$(document).ready(function () {

    var ShowFormPoliza = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_poliza').modal('show')
            },
            success: function (data) {
                $('#modal_poliza .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SaveFormPoliza = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_poliza tbody').html(data.polizas);
                    $('#modal_poliza').modal('hide');
                    console.log('Success!');
                    toastr.success('Yeah!');
                } else {
                    $('#modal_poliza .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowAseguradoForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_asegurado').modal('show')
            },
            success: function (data) {
                $('#modal_asegurado .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SaveAseguradoForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_asegurado tbody').html(data.asegurados);
                    $('#modal_asegurado').modal('hide');
                    console.log('Asegurado registrado correctamente!');
                    toastr.success('Exito');
                } else {
                    $('#modal_asegurado .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('No se pudo registrar asegurado, intente nuevamente.')
            }
        });
        return false;
    }


    var ShowFormSiniestro = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_siniestro').modal('show')
            },
            success: function (data) {
                $('#modal_siniestro .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormSiniestro = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_siniestro tbody').html(data.siniestros);
                    $('#modal_siniestro').modal('hide');
                    console.log('Success!');
                    toastr.success('Yeah!');
                } else {
                    $('#modal_siniestro .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowVehiculoForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_vehiculo').modal('show')
            },
            success: function (data) {
                $('#modal_vehiculo .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SaveVehiculoForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_vehiculo tbody').html(data.vehiculos);
                    $('#modal_vehiculo').modal('hide');
                    console.log('Vehículo registrado correctamente!');
                    toastr.success('Exito');
                } else {
                    $('#modal_vehiculo .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('No se pudo registrar vehículo, intente nuevamente.')
            }
        });
        return false;
    }

    var ShowTallerForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_taller').modal('show')
            },
            success: function (data) {
                $('#modal_taller .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SaveTallerForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_taller tbody').html(data.talleres);
                    $('#modal_taller').modal('hide');
                    console.log('Taller registrado correctamente!');
                    toastr.success('Exito');
                } else {
                    $('#modal_taller .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('No se pudo registrar taller, intente nuevamente.')
            }
        });
        return false;
    }



    //Crear Poliza
    $('.show_poliza').click(ShowFormPoliza);
    $('#modal_poliza').on('submit', '.create_form_polizas', SaveFormPoliza);

    // //Modificar Poliza
    $('#table_poliza').on('click', '.show_poliza_update', ShowFormPoliza);
    $('#modal_poliza').on('submit', '.update_form_poliza', SaveFormPoliza);

    // //Eliminar Poliza
    $('#table_poliza').on('click', '.show_poliza_delete', ShowFormPoliza);
    $('#modal_poliza').on('submit', '.delete_form_poliza', SaveFormPoliza);

    //Crear Asegurado
    $('.show-asegurado ').click(ShowAseguradoForm);
    $('#modal_asegurado').on('submit', '.asegurado_form', SaveAseguradoForm);

    //Modificar Asegurado
    $('#table_asegurado').on('click', '.show_asegurado_update', ShowAseguradoForm);
    $('#modal_asegurado').on('submit', '.asegurado_form_update', SaveAseguradoForm);

    //Eliminar Asegurado
    $('#table_asegurado').on('click', '.show_asegurado_delete', ShowAseguradoForm);
    $('#modal_asegurado').on('submit', '.asegurado_delete_form', SaveAseguradoForm);

    // //Crear Siniestro
    $('.show_siniestro').click(ShowFormSiniestro);
    $('#modal_siniestro').on('submit', '.create_form_siniestro', SaveFormSiniestro);

    // //Modificar Siniestro
    $('#table_siniestro').on('click', '.show_siniestro_update', ShowFormSiniestro);
    $('#modal_siniestro').on('submit', '.update_form_siniestro', SaveFormSiniestro);

    // //Eliminar Siniestro
    $('#table_siniestro').on('click', '.show_siniestro_delete', ShowFormSiniestro);
    $('#modal_siniestro').on('submit', '.delete_form_siniestro', SaveFormSiniestro);


    //Crear Vehiculo
    $('.show-vehiculo').click(ShowVehiculoForm);
    $('#modal_vehiculo').on('submit', '.vehiculo_form', SaveVehiculoForm);

    //Modificar Vehiculo
    $('#table_vehiculo').on('click', '.show_vehiculo_update', ShowVehiculoForm);
    $('#modal_vehiculo').on('submit', '.vehiculo_form_update', SaveVehiculoForm);

    // //Crear Taller
    $('.show_taller').click(ShowTallerForm);
    $('#modal_taller').on('submit', '.create_form_taller', SaveTallerForm);


});


