$(document).ready(function(){
  $.ajax({
    url: "https://danielrebich.000webhostapp.com/Chartjs/data.php", // location of the datafile
    method: "GET",
    success: function(data) {
      console.log(data);
      var x_axis = []; // a generic variable
      var y_axis = [];

      for(var i in data) {
        x_axis.push(data[i].time_received); // must match your dBase columns
        y_axis.push(data[i].temperature);
      }

      var chartdata = {
        labels: x_axis,
        datasets : [
          {
            label: 'Temp',//'Node_1', //Title
            // Change colors: https://www.w3schools.com/css/tryit.asp?filename=trycss3_color_rgba 
            backgroundColor: 'rgba(0, 255, 0, 0.75)', 
            borderColor: 'rgba(200, 200, 200, 0.75)', 
            hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
            hoverBorderColor: 'rgba(200, 200, 200, 1)',
            data: y_axis
          }
        ],
      };

    
    
  
      var ctx = $("#mycanvas");

      var barGraph = new Chart(ctx, {
        type: 'bar',   //Chart Type 
        data: chartdata,
        options: {
            plugins:{
                legend: {
                    display: false
                }, 
                title:{
                    display:true,
                    text: "Node_1",
                    align: 'end',
                    font:{
                        size: 32
                    }
                }
            },
            
            scales:{
                x:{
                    title:{
                        display: true,
                        text: 'Time',
                        font:{
                            size:20
                        }
                    }
                },
                y:{
                    title:{
                        display: true,
                        text: 'Temperature',
                        font:{
                            size:20
                        }
                    }
                }
                
            }
        }
        
      });
    },
    error: function(data) {
      console.log(data);
    }
  });
});
