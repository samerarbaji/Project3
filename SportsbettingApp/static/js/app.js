//function buildPlot() {
  /* data route */
  const url = "/api/HorseRoute";
  d3.json(url).then(function(response) {

    console.log(response);
  });