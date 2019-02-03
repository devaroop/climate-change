var tempChartCanvas = document.getElementById("tempChart").getContext('2d');
var tempChart = new Chart(tempChartCanvas, {
  type: 'line',
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
    }]
  }
});
