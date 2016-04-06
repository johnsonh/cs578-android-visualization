var width = 1000,
    height = 1000;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("https://raw.githubusercontent.com/johnsonh/cs578-android-visualization/master/d3/graph.json", function(error, graph) {
  if (error) throw error;

  force
      .nodes(graph.nodes)
      .links(graph.links)
      .size([width, height])
      .linkDistance(function(l, i) {
          var n1 = l.source, n2 = l.target;
          var strength = 150;
          if (n1.parentApp == n2.parentApp) {
            return strength / 5;
          }
          return strength;
        })
      .linkStrength(function(l, i) {
          var n1 = l.source, n2 = l.target;
          var strength = 10;
          if (n1.parentApp == n2.parentApp) {
            return strength * 2;
          }
          return 10;
        })
      .gravity(0.1)   // gravity+charge tweaked to ensure good 'grouped' view (e.g. green group not smack between blue&orange, ...
      .charge(-100)    // ... charge is important to turn single-linked groups to the outside
      .friction(0.5)   // friction adjusted to get dampened display: less bouncy bouncy ball [Swedish Chef, anyone?]

      .start();

  var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.parentApp); })
      .on("mouseover", mouseover)
      .on("mouseout", mouseout)
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.name; });

      // // Append the labels to each group
  // var labels = node.enter().append("text")
  //   // .text(function(d) { return d.group });
  //   .text(function(d) { console.log(d.group) });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });

  function mouseover() {
    d3.select(this).select("circle").transition()
        .duration(750)
        .attr("r", 160);
  }

  function mouseout() {
    d3.select(this).select("circle").transition()
        .duration(750)
        .attr("r", 8);
  }
});

