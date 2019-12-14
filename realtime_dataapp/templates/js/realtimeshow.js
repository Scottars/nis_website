
var chartData = [];
var chartData1 = [];
var chartData2= [];
var chartData3 = [];
var dataAll = [
[
    [10.0, 8.04],
    [8.0, 6.95],
    [13.0, 7.58],
    [9.0, 8.81],
    [11.0, 8.33],
    [14.0, 9.96],
    [6.0, 7.24],
    [4.0, 4.26],
    [12.0, 10.84],
    [7.0, 4.82],
    [5.0, 5.68]
],
[
    [10.0, 9.14],
    [8.0, 8.14],
    [13.0, 8.74],
    [9.0, 8.77],
    [11.0, 9.26],
    [14.0, 8.10],
    [6.0, 6.13],
    [4.0, 3.10],
    [12.0, 9.13],
    [7.0, 7.26],
    [5.0, 4.74]
],
[
    [10.0, 7.46],
    [8.0, 6.77],
    [13.0, 12.74],
    [9.0, 7.11],
    [11.0, 7.81],
    [14.0, 8.84],
    [6.0, 6.08],
    [4.0, 5.39],
    [12.0, 8.15],
    [7.0, 6.42],
    [5.0, 5.73]
],
[
    [8.0, 6.58],
    [8.0, 5.76],
    [8.0, 7.71],
    [8.0, 8.84],
    [8.0, 8.47],
    [8.0, 7.04],
    [8.0, 5.25],
    [19.0, 12.50],
    [8.0, 5.56],
    [8.0, 7.91],
    [8.0, 6.89]
]
];
var dom = document.getElementById("container");
var myChart = echarts.init(dom);

var app = {};
option = null;
option = {
    title: {
        text: 'Anscombe\'s quartet',
        x: 'center',
        y: 0
    },
    grid: [
        {x: '7%', y: '7%', width: '38%', height: '38%'},
        {x2: '7%', y: '7%', width: '38%', height: '38%'},
        {x: '7%', y2: '7%', width: '38%', height: '38%'},
        {x2: '7%', y2: '7%', width: '38%', height: '38%'}
    ],
    tooltip: {
        formatter: 'Group {a}: ({c})'
    },
    xAxis:[
        //{scale:'True'},
        {gridIndex: 0,scale:'True',},
        {gridIndex: 1,scale:'True',},
        {gridIndex: 2,scale:'True',},
        {gridIndex: 3,scale:'True',}
    ],
    yAxis: [
        {gridIndex: 0,scale:'True',},
        {gridIndex: 1,scale:'True',},
        {gridIndex: 2,scale:'True',},
        {gridIndex: 3,scale:'True',}
    ],
    series: [
        {
            name: 'I',
            type: 'scatter',
            xAxisIndex: 0,
            yAxisIndex: 0,
            data: chartData1,

        },
        {
            name: 'II',
            type: 'scatter',
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: chartData,

        },
        {
            name: 'III',
            type: 'scatter',
            xAxisIndex: 2,
            yAxisIndex: 2,
            data: chartData2,

        },
        {
            name: 'IV',
            type: 'scatter',
            xAxisIndex: 3,
            yAxisIndex: 3,
            data: chartData3,

        }
    ]
};


if (option && typeof option === "object") {
myChart.setOption(option, true);
}

var websocket = null;

  //判断当前浏览器是否支持WebSocket
  if ('WebSocket' in window) {
    //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
    websocket = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
  }else {
      setMessageInnerHTML('当前浏览器 Not support websocket')
  }

  //连接发生错误的回调方法

  websocket.onerror = function () {
      setMessageInnerHTML("WebSocket连接发生错误");
  };

  //连接成功建立的回调方法

  websocket.onopen = function () {

      setMessageInnerHTML("WebSocket连接成功");

  }

  //接收到消息的回调方法

  websocket.onmessage = function (event) {

      setMessageInnerHTML(event.data);
      var arr = event.data.split(",");
      //{#alert(event.data);#}
      chartData.push(arr);
      chartData1.push(arr);
      chartData2.push(arr);
      chartData3.push(arr);
      if (chartData.length>=62*2)
      {
          chartData.shift();
            chartData1.shift();
          chartData2.shift();
          chartData3.shift();
      }

    //   location.reload();
      reloadData();

  };


var reloadData = function(){

option = {

    series: [
        {
            name: 'I',
            type: 'scatter',
            xAxisIndex: 0,
            yAxisIndex: 0,
            data: chartData1,

        },
        {
            name: 'II',
            type: 'scatter',
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: chartData,

        },
        {
            name: 'III',
            type: 'scatter',
            xAxisIndex: 2,
            yAxisIndex: 2,
            data: chartData2,

        },
        {
            name: 'IV',
            type: 'scatter',
            xAxisIndex: 3,
            yAxisIndex: 3,
            data: chartData3,

        }
    ]
};

          //console.log(option);
         if (option && typeof option === "object") {
            myChart.setOption(option);
        }


    }

  //连接关闭的回调方法

//   websocket.onclose = function () {

//       setMessageInnerHTML("WebSocket连接关闭");

//   }

  //监听窗口关闭事件，当窗口关闭时，主动去关闭websocket连接，防止连接还没断开就关闭窗口，server端会抛异常。

//   window.onbeforeunload = function () {

//       closeWebSocket();

//   }

  //将消息显示在网页上

  function setMessageInnerHTML(innerHTML) {

      console.log(innerHTML);

  }

  //关闭WebSocket连接

  function closeWebSocket() {

      websocket.close();

  }
