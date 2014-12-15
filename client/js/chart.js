function get_data(param) {
    $.get(param, function (response) {
        data = jQuery.parseJSON(response);
  // Create the chart
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
    });
}
