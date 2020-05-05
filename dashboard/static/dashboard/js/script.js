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
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_asegurado .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
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
                    toastr.success('Operación Exitosa!');
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
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_vehiculo .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
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
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_taller .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowTallerDisableForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_taller_disabled').modal('show')
            },
            success: function (data) {
                $('#modal_taller_disabled .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SaveTallerDisableForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_taller_disabled tbody').html(data.talleresDisable);
                    $('#modal_taller_disabled').modal('hide');
                    console.log('Taller Reactivado correctamente!');
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_taller_disabled .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowPolizaDisableForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_poliza_disabled').modal('show')
            },
            success: function (data) {
                $('#modal_poliza_disabled .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

    var SavePolizaDisableForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_poliza_disabled tbody').html(data.polizasDisable);
                    $('#modal_poliza_disabled').modal('hide');
                    console.log('Póliza Habilitada correctamente!');
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_poliza_disabled .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowAseguradoDisableForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_asegurado_disabled').modal('show')
            },
            success: function (data) {
                $('#modal_asegurado_disabled .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };

     var SaveAseguradoDisableForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_asegurado_disabled tbody').html(data.aseguradosDisable);
                    $('#modal_asegurado_disabled').modal('hide');
                    console.log('Asegurado reactivado correctamente!');
                    toastr.success('Operación Exitosa!');
                } else {
                    $('#modal_asegurado_disabled .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
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

    //Crear Taller
    $('.show_taller').click(ShowTallerForm);
    $('#modal_taller').on('submit', '.create_form_taller', SaveTallerForm);

    //Modificar Taller
    $('#table_taller').on('click', '.show_taller_update', ShowTallerForm);
    $('#modal_taller').on('submit', '.update_form_taller', SaveTallerForm);

    //Eliminar Taller
    $('#table_taller').on('click', '.show_taller_delete', ShowTallerForm);
    $('#modal_taller').on('submit', '.delete_form_taller', SaveTallerForm);

    //Reactivar Taller
    $('#table_taller_disabled').on('click', '.show_taller_reactivate', ShowTallerDisableForm);
    $('#modal_taller_disabled').on('submit', '.reactivate_form_taller', SaveTallerDisableForm);

    //Reactivar Póliza
    $('#table_poliza_disabled').on('click', '.show_poliza_reactivate', ShowPolizaDisableForm);
    $('#modal_poliza_disabled').on('submit', '.reactivate_form_poliza', SavePolizaDisableForm);

    //Reactivar Asegurado
    $('#table_asegurado_disabled').on('click', '.show_asegurado_reactivate', ShowAseguradoDisableForm);
    $('#modal_asegurado_disabled').on('submit', '.reactivate_form_asegurado', SaveAseguradoDisableForm);


});


