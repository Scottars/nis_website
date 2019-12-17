


var chartData = [];
var chartData1 = [];
var chartData2= [];
var chartData3 = [];
var chartData4 = [];
var chartData5 = [];
var chartData6= [];
var chartData7 = [];
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
        {x: '2%', y: '5%', width: '40%', height: '20%'},                    {x2: '2%', y: '5%', width: '40%', height: '20%'},
        {x: '2%', y: '28%', width: '40%', height: '20%'},                   {x2: '2%', y: '28%', width: '40%', height: '20%'},

        {x: '2%', y2: '28%', width: '40%', height: '20%'},                   {x2: '2%', y2: '28%', width: '40%', height: '20%'},

        {x: '2%', y2: '5%', width: '40%', height: '20%'},                   {x2: '2%', y2: '5%', width: '40%', height: '20%'},


        // {x: '42%', y: '22%', width: '20%', height: '20%'},
        // {x2: '2%', y2: '2%', width: '20%', height: '20%'},

        // {x: '2%', y2: '7%', width: '20%', height: '20%'},
        // {x2: '2%', y2: '2%', width: '20%', height: '20%'},
        // {x: '2%', y: '2%', width: '20%', height: '20%'},
        // {x2: '2%', y: '2%', width: '20%', height: '20%'},
        // {x: '22%', y2: '7%', width: '20%', height: '20%'},
        // {x2: '22%', y2: '2%', width: '20%', height: '20%'},
        // {x3: '7%', y: '7%', width: '38%', height: '38%'},
        // {x4: '7%', y: '7%', width: '38%', height: '38%'},
        // {x: '7%', y2: '7%', width: '38%', height: '38%'},
        // {x2: '7%', y2: '7%', width: '38%', height: '38%'}
    ],
    // tooltip: {
    //     formatter: 'Group {a}: ({c})'
    // },
    xAxis:[
        //{scale:'True'},
        {gridIndex: 0,scale:'True',},
        {gridIndex: 1,scale:'True',},
        {gridIndex: 2,scale:'True',},
        {gridIndex: 3,scale:'True',},
        {gridIndex: 4,scale:'True',},
        {gridIndex: 5,scale:'True',},
        {gridIndex: 6,scale:'True',},
        {gridIndex: 7,scale:'True',}
    ],
    yAxis: [
        {gridIndex: 0,scale:'True',},
        {gridIndex: 1,scale:'True',},
        {gridIndex: 2,scale:'True',},
        {gridIndex: 3,scale:'True',},
        {gridIndex: 4,scale:'True',},
        {gridIndex: 5,scale:'True',},
        {gridIndex: 6,scale:'True',},
        {gridIndex: 7,scale:'True',}
    ],
    series: [
        {
            name: 'I',
            type: 'scatter',
            xAxisIndex: 0,
            yAxisIndex: 0,
            data: dataAll[1],

        },
        {
            name: 'II',
            type: 'scatter',
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: dataAll[1],

        },
        {
            name: 'III',
            type: 'scatter',
            xAxisIndex: 2,
            yAxisIndex: 2,
            data: dataAll[1],

        },
        {
            name: 'IV',
            type: 'scatter',
            xAxisIndex: 3,
            yAxisIndex: 3,
            data: dataAll[1],

        },
                {
            name: 'V',
            type: 'scatter',
            xAxisIndex: 4,
            yAxisIndex: 4,
            data: dataAll[1],

        },
        {
            name: 'VI',
            type: 'scatter',
            xAxisIndex: 5,
            yAxisIndex: 5,
            data: dataAll[1],

        },
        {
            name: 'VII',
            type: 'scatter',
            xAxisIndex: 6,
            yAxisIndex: 6,
            data: dataAll[1],

        },
        {
            name: 'VIII',
            type: 'scatter',
            xAxisIndex: 7,
            yAxisIndex: 7,
            data: dataAll[1],

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
    // {#alert(window.location.host)#}
}else {
    setMessageInnerHTML('当前浏览器 Not support websocket')
}

//连接发生错误的回调方法


//接收到消息的回调方法

websocket.onmessage = function (event) {

    setMessageInnerHTML(event.data);
    var arr = event.data.split(",");
    //{#alert(event.data);#}
    chartData.push(arr);
    chartData1.push(arr);
    chartData2.push(arr);
    chartData3.push(arr);
    chartData4.push(arr);
    chartData5.push(arr);
    chartData6.push(arr);
    chartData7.push(arr);
    if (chartData.length>=62*2)
    {
        chartData.shift();
        chartData1.shift();
        chartData2.shift();
        chartData3.shift();
        chartData4.shift();
        chartData5.shift();
        chartData6.shift();
        chartData7.shift();
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

        },
                {
            name: 'V',
            type: 'scatter',
            xAxisIndex: 4,
            yAxisIndex: 4,
            data: chartData4,

        },
        {
            name: 'VI',
            type: 'scatter',
            xAxisIndex: 5,
            yAxisIndex: 5,
            data: chartData5,

        },
        {
            name: 'VII',
            type: 'scatter',
            xAxisIndex: 6,
            yAxisIndex: 6,
            data: chartData6,

        },
        {
            name: 'VIII',
            type: 'scatter',
            xAxisIndex: 7,
            yAxisIndex: 7,
            data: chartData7,

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

