function ufcresponse() {

    // if the SVG area isn't empty when the browser loads,
    // remove it and replace it with a resized version of the chart
  var svgArea = d3.select("body").select("svg");
  
  if (!svgArea.empty()) {
    svgArea.remove();
  }
  
    // svg params
  var svgHeight = window.innerHeight;
  var svgWidth = window.innerWidth;
  
  
  var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 100
  };
  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;
  // Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
   var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
   var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);
  // Import Data
   var url ="/api/UFC1"
   d3.json(url).then( function(data) {
        console.log(data)
    // formating data
      data.forEach(function (d) {
      d.Odds_Red_Fighter =+d.Odds_Red_Fighter;
      d.Odds_Blue_Fighter = + d.Odds_Blue_Fighter;
      d.Red_Corner_Fighter =  d.Red_Corner_Fighter;
      d.Blue_Corner_Fighter =  d.Blue_Corner_Fighter;
      d.Winner =  d.Winner;
      //console.log(d.Odds_Red_Fighter);
      //console.log(Odds_Blue_Fighter);
      //console.log(Red_Corner_Fighter);
      //console.log(Blue_Corner_Fighter)
    });
    // creating scale functions
    var xScale = d3.scaleLinear()
                   .domain([d3.min(data, d => (d.Odds_Red_Fighter-0.2)) ,
  
                            d3.max(data, d => d.Odds_Red_Fighter) ])               
                   .range([0, width]);
                     
    var yScale = d3.scaleLinear()
                   .domain([d3.min(data, d=> (d.Odds_Blue_Fighter-1)),
                            d3.max(data, d => d.Odds_Blue_Fighter) ])
                   .range([height, 0]);
                            
                   
  
    // creating axis functions 
    var bottomAxis= d3.axisBottom(xScale).ticks(20);
    var leftAxis = d3.axisLeft(yScale).ticks(20);
    
  
    // set xscale to the bottom of the chart
    chartGroup.append("g")
              .attr("transform", `translate(0, ${height})`)
              .call(bottomAxis);
   
   // set yscale to the left of the chart
    chartGroup.append("g")
      // Define the color of the axis text
              .classed("blue", true)
              .call(leftAxis);
  
         
  
   var circlesGroup = chartGroup.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", d => xScale(d.Odds_Red_Fighter))
      .attr("cy", d => yScale(d.Odds_Blue_Fighter))
      .attr("r", "12")
      .attr("fill", "Purple")
      .attr("opacity", ".5");
  
  
  
  
  
  
  //adding text element
  var text = chartGroup.selectAll(".Red_Corner_FighterText")
             
                    .data(data)
                    .enter()
                    .append("text")
                    .classed ("Red_Corner_Fighter", true)
                    .attr("x", d => xScale(d.Odds_Red_Fighter))
                    .attr("y", d => yScale(d.Odds_Blue_Fighter))
                    .attr("font-size", "8px")
                    .text(d => d.index)
                    .attr("text-anchor", "middle")
                    .attr("fill", "white");

  var text1 = chartGroup.selectAll(".Blue_Corner_FighterText1")
                    .data(data)
                    .enter()
                    .append("text1")
                    .classed ("Blue_Corner_Fighter", true)
                    .attr("x", d => xScale(d.Odds_Red_Fighter))
                    .attr("y", d => yScale(d.Odds_Blue_Fighter))
                    .attr("font-size", "8px")
                    .text(d => d.index)
                    .attr("text-anchor", "middle")
                    .attr("fill", "white");
  
 var text2 = chartGroup.selectAll(".WinnerText2")
                    .data(data)
                    .enter()
                    .append("text2")
                    .classed ("Winner", true)
                    .attr("x", d => xScale(d.Odds_Red_Fighter))
                    .attr("y", d => yScale(d.Odds_Blue_Fighter))
                    .attr("font-size", "8px")
                    .text(d => d.index)
                    .attr("text-anchor", "middle")
                    .attr("fill", "white");  
  // Create axes labels
      chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Odds Blue Fighter");
  
      chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
        .attr("class", "axisText")
        .text("Odds Red Fighter");
  
    //ToolTip (initialize tooltip)  
      var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
          //console.log(d.)
          //console.log(d.)
        return (`<strong>Red Fighter:${d.Red_Corner_Fighter}<br>Blue Fighter:${d.Blue_Corner_Fighter}<br>Red Fighter Odds:${d.Odds_Red_Fighter}%<br>Blue Fighter Odds:${d.Odds_Blue_Fighter}%<br>Winner:${d.Winner}<strong>`);
        });
      // Step 2: Create the tooltip in chartGroup.
      chartGroup.call(toolTip);
  
      // Step 3: Create "mouseover" event listener to display tooltip
      circlesGroup.on("mouseover", function(d) {
        toolTip.show(d, this);
      })
      // Step 4: Create "mouseout" event listener to hide tooltip
        .on("mouseout", function(d) {
          toolTip.hide(d);
        });
  
    })
    // .catch(function(error) {
    //   console.log(error);
    // }); 
  
  
  };
  
  ufcresponse();
  
  // Event listener for window resize.
  // When the browser window is resized, makeResponsive() is called.
  d3.select(window).on("resize", ufcresponse);