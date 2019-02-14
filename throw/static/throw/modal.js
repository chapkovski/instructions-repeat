$(document).ready(function () {
    $('#error_modal').modal('show');
    $('.modal').on('shown.bs.modal', function () {
        $(this).find('[autofocus]').focus();
    });
});

