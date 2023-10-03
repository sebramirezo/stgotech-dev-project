$(document).ready(function() {
    $('#id_bodega_fk').select2();
    $('#id_origen_fk').select2();

          
    $('#id_bodega_fk').siblings('.select2-container').find('.select2-selection__rendered').text('Ingresa Bodega');
    $('#id_origen_fk').siblings('.select2-container').find('.select2-selection__rendered').text('Ingresa Origen');

    

 });

    