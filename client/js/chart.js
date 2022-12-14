function getData(param) {
$.ajax({url: 'temp',
        async: false,
        contentType: false,
        processData: false,
        type: 'GET',
        success: function (result, status, xhr) {
                data = jQuery.parseJSON(result);
        drawGraph(data);
        },
        error: function(xhr, status, error){
                alert(status + "::" + error);
        }});
}

function drawGraph(data){
    // Create the chart
    Highcharts.setOptions({
        global: {
            timezoneOffset: new Date().getTimezoneOffset(),
            useUTC: false
        }
    });

    $('#container').highcharts('StockChart', {
        rangeSelector : {
            selected : 1
        },
        title : {
            text : 'Weather Data'
        },
        series : [{
            name : 'Temperature',
            data : data,
            tooltip: {
                valueDecimals: 2
            }
        }]
    });	
}
