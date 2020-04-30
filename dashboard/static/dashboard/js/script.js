$(document).ready(function () {

    var ShowForm = function () {
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

    var SaveForm = function () {
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
                    toastr.success('Exito!');
                } else {
                    $('#modal_poliza .modal-content').html(data.html_form)
                }
            },
            error: function () {
                toastr.error('Error!');
            }

        });
        return false;
    }

    //Crear Poliza
    $('.show_form').click(ShowForm);
    $('#modal_poliza').on('submit', '.create_form', SaveForm);

    // //Modificar Poliza
    $('#table_poliza').on('click', '.show_form_update', ShowForm);
    $('#modal_poliza').on('submit', '.update_form', SaveForm);

    // //Eliminar Producto
    $('#table_poliza').on('click', '.show_form_delete', ShowForm);
    $('#modal_poliza').on('submit', '.delete_form', SaveForm);


});


