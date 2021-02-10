//function buildPlot() {
  /* data route */
  const url = "/api/NFLRoute";
  d3.json(url).then(function(response) {

    console.log(response);

    //const data = response;

    