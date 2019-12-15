$(document).ready(function () {

   $('#btn-deposito').click(function () {
       var cantida = $('#deposito').val();
       
       $.ajax({
           url : '/Estado/Deposito/Nuevo',
           data : {
               'monto' : cantida
           },
           dataType : 'json',
           success : function(data){
            if(data.is_OK){
                exito();
            }
            else{
                error();
            }  
           }
       })

      
       return false;
   })
   $('#btn-retiro').click(function () {
    var cantida = $('#deposito').val();
    
    $.ajax({
        url : '/Estado/Retiro/Nuevo',
        data : {
            'monto' : cantida
        },
        dataType : 'json',
        success : function(data){
           if(data.is_OK){
               exito();
           }
           else{
               error();
           }
        }
    })

    function exito(){
       $('#alert').append("<h3>La Transaccion ha sido exitosa </h3>");
       $('#deposito').val("00.00");
      
      

    }
    function error(){
        $('#alert').append("<h3>La Transaccion no puede ser ejecutada </h3>");
        $('#deposito').val("00.00");
        sleep(2000);
        $('#alert').append("");

    }
   
    return false;

    })
    $('#btn-report').click(function () {
        var id = $('#val').val();
        
        $.ajax({
            url : '/Estado/reporte',
            data : {
                'id' : id
            },
            dataType : 'json',
            success : function(data){
                console.log(data);
            }
        })
        
        return false
    })
})
