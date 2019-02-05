var build_charts = function(data){
  var tempChartCanvas = $("#tempChart")[0].getContext('2d'),
      humidityChart = $("#humidityChart")[0].getContext('2d'),
      vehicleChart = $("#vehicleChart")[0].getContext('2d'),
      treeChart = $("#treeChart")[0].getContext('2d'),
      populationChart = $("#populationChart")[0].getContext('2d'),
      waterChart = $("#waterChart")[0].getContext('2d'),
      ozoneChart = $("#ozoneChart")[0].getContext('2d'),
      noxChart = $("#noxChart")[0].getContext('2d'),
      so2Chart = $("#so2Chart")[0].getContext('2d'),
      pm25Chart = $("#pm25Chart")[0].getContext('2d'),
      pm10Chart = $("#pm10Chart")[0].getContext('2d');

  chart_template_build(tempChartCanvas, data["Year"], data["Temp"], "Temp in deg C", "line");
  chart_template_build(humidityChart, data["Year"], data["Humidity"], "% Humidity", "line");
  chart_template_build(vehicleChart, data["Year"], data["Total Vehicles"], "Total Vehicles in Pune", "line");
  chart_template_build(treeChart, data["Year"], data["TreeCover(sqkm)"], "Total Forest Cover (sq. km)", "bar");
  chart_template_build(populationChart, data["Year"], data["Population"], "Total Population in Pune", "line");
  chart_template_build(waterChart, data["Year"], data["August(MONSOON)"], "Total ground water table (mts)", "line");
  chart_template_build(ozoneChart, data["Year"], data["Ozone"], "Ozone Variation (ppm)", "bar");
  chart_template_build(noxChart, data["Year"], data["NOx"], "NOx variation (ppm)", "bar");
  chart_template_build(so2Chart, data["Year"], data["SO2"], "SO2 variation (ppm)", "bar");
  chart_template_build(pm25Chart, data["Year"], data["PM2.5"], "PM2.5 variation (ppm)", "bar");
  chart_template_build(pm10Chart, data["Year"], data["PM10"], "PM10 variation (ppm)", "bar");
};

var randomColorGenerator = function () { 
  return '#' + (Math.random().toString(16) + '0000000').slice(2, 8); 
};

var chart_template_build = function(elem, xaxis, yaxis, label, graph_type){
  new Chart(elem, {
    type: graph_type,
    data: {
      labels: xaxis,
      datasets: [{
	label: label,
	data: yaxis,
	borderColor: randomColorGenerator(),
	fillColor: randomColorGenerator(), 
        strokeColor: randomColorGenerator(), 
        highlightFill: randomColorGenerator(),
        highlightStroke: randomColorGenerator(),
      }]
    }
  });
};

$(document).ready(function(){
  var date_query = $('#show_date').val();
  query_for_data(date_query);

  $( document ).ajaxError(function( event, jqxhr, settings, thrownError ) {
    console.log(thrownError);
  });
  
  //set on change
  $("#show_date").change(function(){
    var date_query = new Date($('#show_date').val()).toLocaleDateString();
    query_for_data(date_query);
  });
});

var current_data_display = function(data){
  if("current" in data){
    var current_data = data["current"];
    $("#current_temp").text(current_data["temp"]);
    $("#current_humidity").text(current_data["humidity"]);
    $("#current_precipitation").text(current_data["rainProbability"]);
    $("#current_ozone").text(current_data["ozone"]);
    $("#current_data_show").show();
  }
};

var query_for_data = function(date){
  $('#date_display').text("Fetching.....");
  $('#design_spinners').show();
  $("#current_data_show").hide();

  var display_current_details = false;
  if(date == ""){
    $('#show_date').val(new Date().toISOString().slice(0, 10))
    date = new Date().toLocaleDateString();
    display_current_details = true;
  }

  $.get("/get_data?date=" + date + "&current=" + display_current_details, function(data){
    //string data (there are reasons why, ask me)
    data = data.replace(/NaN/g, null);
    var parsed_data = $.parseJSON(data);
    build_charts(parsed_data);
    current_data_display(parsed_data);
    $('#date_display').text(date.slice(0, -5));
    $('#design_spinners').hide();
  });
};

