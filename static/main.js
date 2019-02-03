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
  chart_template_build(vehicleChart, data["Year"], data["Total Vehicles"], "Total Vehicles in Pune");
  chart_template_build(treeChart, data["Year"], data["TreeCover(sqkm)"], "Total Forest Cover");
  chart_template_build(populationChart, data["Year"], data["Population"], "Total Population in Pune");
  chart_template_build(waterChart, data["Year"], data["August(MONSOON)"], "Total ground water table");
  chart_template_build(ozoneChart, data["Year"], data["Ozone"], "Ozone Variation");
  chart_template_build(noxChart, data["Year"], data["NOx"], "NOx variation");
  chart_template_build(so2Chart, data["Year"], data["SO2"], "SO2 variation");
  chart_template_build(pm25Chart, data["Year"], data["PM2.5"], "PM2.5 variation");
  chart_template_build(pm10Chart, data["Year"], data["PM10"], "PM10 variation");
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
  var date_query = $('#show_date').val();
  query_for_data(date_query);

  //set on change
  $("#show_date").change(function(){
    var date_query = new Date($('#show_date').val()).toLocaleDateString();
    query_for_data(date_query);
  });
});

var query_for_data = function(date){
  if(date == ""){
    $('#show_date').val(new Date().toISOString().slice(0, 10))
    date = new Date().toLocaleDateString();
  }
  
  $.get("/get_data?date=" + date, function(data, status){
    console.log(data);
    build_charts(data);
  });
};

