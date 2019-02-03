var build_charts = function(data){
  var tempChartCanvas = $("#tempChart").getContext('2d'),
      humidityChart = $("#humidityChart").getContext('2d'),
      vehicleChart = $("#vehicleChart").getContext('2d'),
      treeChart = $("#treeChart").getContext('2d'),
      populationChart = $("#populationChart").getContext('2d'),
      waterChart = $("#waterChart").getContext('2d'),
      ozoneChart = $("#ozoneChart").getContext('2d'),
      noxChart = $("#noxChart").getContext('2d'),
      so2Chart = $("#so2Chart").getContext('2d'),
      pm25Chart = $("#pm25Chart").getContext('2d'),
      pm10Chart = $("#pm10Chart").getContext('2d');

  chart_template_build(tempChartCanvas, data["Year"], data["Temp(deg Centigrade)"], "Temp in deg C");
  chart_template_build(humidityChart, data["Year"], data["% Humidity"], "% Humidity");
  chart_template_build(vehicleChart, data["Year"], data["% Humidity"], "Total Vehicles in Pune");
  chart_template_build(treeChart, data["Year"], data["% Humidity"], "Total Forest Cover");
  chart_template_build(populationChart, data["Year"], data["% Humidity"], "Total Population in Pune");
  chart_template_build(waterChart, data["Year"], data["% Humidity"], "Total ground water table");
  chart_template_build(ozoneChart, data["Year"], data["% Humidity"], "Ozone Variation");
  chart_template_build(noxChart, data["Year"], data["% Humidity"], "NOx variation");
  chart_template_build(so2Chart, data["Year"], data["% Humidity"], "SO2 variation");
  chart_template_build(pm25Chart, data["Year"], data["% Humidity"], "PM2.5 variation");
  chart_template_build(pm10Chart, data["Year"], data["% Humidity"], "PM10 variation");
};

var chart_template_build = function(elem, xaxis, yaxis, label){
  new Chart(elem, {
    type: 'line',
    data: {
      labels: xaxis,
      datasets: [{
	label: label,
	data: yaxis,
      }]
    }
  });
};

$(document).ready(function(){
  var date_query = $('#date').val();
  query_for_data(date_query);

  //set on change
  $("#date").change(function(){
    var date_query = $('#date').val();
    query_for_data(date_query);
  });
});

var query_for_data = function(date){
  $.get("/get_data?date=" + date_query, function(data, status){
    console.log(data);
    build_charts(data);
  });
};

