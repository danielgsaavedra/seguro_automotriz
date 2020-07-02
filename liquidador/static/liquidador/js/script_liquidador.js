$(document).ready(function () {

    function actualizar() {
        location.reload();
    }

    var ShowFormTipoPlan = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_tipo_plan').modal('show')
            },
            success: function (data) {
                $('#modal_tipo_plan .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormTipoPlan = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#table_tipo_plan tbody').html(data.tipos_plan);
                    $('#modal_tipo_plan').modal('hide');
                    console.log('Success!');
                    toastr.success('Operación Exitosa');

                } else {
                    $('#modal_tipo_plan .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var ShowFormPresupuestoAproRech = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modal_presupuesto_liquidador').modal('show')
            },
            success: function (data) {
                $('#modal_presupuesto_liquidador .modal-content').html(data.html_form)
            },
            error: function () {
                alert('Algo salió mal, intenta nuevamente.')
            }
        });
    };


    var SaveFormPresupuestoAproRech = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#modal_presupuesto_liquidador').modal('hide');
                    console.log('Success!');
                    setTimeout(volveratras,1000);
                    toastr.success('Operación Exitosa');

                } else {
                    $('#modal_presupuesto_liquidador .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Algo salió mal, intenta nuevamente.')
            }
        });
        return false;
    }

    var volveratras = function() {
        history.back();
    }

    //Create Tipo Plan
    $('.show_tipo_plan').click(ShowFormTipoPlan);
    $('#modal_tipo_plan').on('submit', '.create_form_tipo_plan', SaveFormTipoPlan);
    //Update Tipo Plan
    $('#table_tipo_plan').on('click', '.show_tipo_update', ShowFormTipoPlan);
    $('#modal_tipo_plan').on('submit', '.update_form_tipo_plan', SaveFormTipoPlan);
    //Delete logic Tipo Plan
    $('#table_tipo_plan').on('click', '.show_tipo_delete', ShowFormTipoPlan);
    $('#modal_tipo_plan').on('submit', '.delete_form_tipo_plan', SaveFormTipoPlan);
    //Reactivar Tipo Plan
    $('#table_tipo_plan').on('click', '.show_tipo_reactive', ShowFormTipoPlan);
    $('#modal_tipo_plan').on('submit', '.reactive_form_tipo_plan', SaveFormTipoPlan);

    //Aprobar Presupuesto
    $('.show_aprobar_presupuesto').click(ShowFormPresupuestoAproRech);
    $('#modal_presupuesto_liquidador').on('submit', '.aprobar_form_presupuesto', SaveFormPresupuestoAproRech);

    //Rechazar Presupuesto
    $('.show_rechazar_presupuesto').click(ShowFormPresupuestoAproRech);
    $('#modal_presupuesto_liquidador').on('submit', '.rechazar_form_presupuesto', SaveFormPresupuestoAproRech);



});