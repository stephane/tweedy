var margin = {top: 20, right: 20, bottom: 30, left: 30},
    width = 1170 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var xScale = d3.time.scale()
      .rangeRound([0, width]);

var yScale = d3.scale.linear()
      .range([height, 0]);

var xAxis = d3.svg.axis()
      .scale(xScale)
      .orient('bottom')
      .ticks(d3.time.day)
      .tickFormat(d3.time.format('%d %b'))
      .tickPadding(6);

var yAxis = d3.svg.axis()
      .scale(yScale)
      .orient('left')
      .tickFormat(d3.format("d"))
      .tickPadding(8);

var svg = d3.select('#yield-bar-chart').append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')');

d3.json("json/", function(error, data) {
  var yields = data.yields;

  xScale.domain([new Date(yields[0].date), new Date(yields[yields.length - 1].date)]);

  var max_total = d3.max(yields, function(d) { return d.total; });
  yScale.domain([0, max_total]);
  yAxis.ticks(max_total);

  svg.append('g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0, ' + height + ')')
    .call(xAxis);

  svg.append('g')
    .attr('class', 'y axis')
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Œufs");

  svg.selectAll('.bar')
    .data(yields)
    .enter().append('rect')
    .attr('class', 'bar')
    .attr('x', function(d) { return xScale(new Date(d.date)); })
    .attr('width', 30)
    .attr('y', function(d) { return yScale(d.total); })
    .attr('height', function(d) { return height - yScale(d.total); });
});
