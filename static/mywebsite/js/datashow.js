






function realtime_datashow(){
    // var ele = document.getElementById("realtime-menu");
    // ele.style.display="block";

    $("#realtime-menu").css("display","block");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","none");


    $("#realtime_showarea").css("display","block");
    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","none");


    $(".function-button .menu-li li").css("color","red")




}

function history_datashow(){


    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","block");
    $("#download-menu").css("display","none");

    $("#realtime_showarea").css("display","none");
    $("#history_showarea").css("display","block");
    $("#download_showarea").css("display","none");
}
function download_datashow(){


    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","block");

    $("#realtime_showarea").css("display","none");
    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","block");
}




var websocket = null;
var chartData = [];


//class .   id #
function realtime_start() {

    var app = {};
    var chartData1 = [];
    var chartData2 = [];
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
    var dom = document.getElementById("realtime_showarea");
    var myChart = echarts.init(dom);
    var option = null;
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
        xAxis: [
            //{scale:'True'},

            {gridIndex: 0, scale: 'True', splitLine:{show:false},type:'value',show:false,},
            {gridIndex: 1, scale: 'True',splitLine:{show:false},type:'value',show:false,},
            {gridIndex: 2, scale: 'True',splitLine:{show:false},type:'value',show:false,},
            {gridIndex: 3, scale: 'True',splitLine:{show:false},type:'value',show:false,}
        ],
        yAxis: [
            {gridIndex: 0, splitLine:{show:false},type:'value',},
            {gridIndex: 1, splitLine:{show:false},type:'value',},
            {gridIndex: 2, splitLine:{show:false},type:'value',},
            {gridIndex: 3, splitLine:{show:false},type:'value', }
        ],
        series: [
            {
                name: 'I',
                type:'scatter',
                symbolSize:5,
                smooth:true,
                xAxisIndex: 0,
                yAxisIndex: 0,
                data: chartData,
            },
            {
                name: 'II',
                type:'scatter',
                symbolSize:5,

                smooth:true,
                xAxisIndex: 1,
                yAxisIndex: 1,
                data: chartData1,

            },
            {
                name: 'III',
                type:'scatter',
                symbolSize:5,

                smooth:true,
                xAxisIndex: 2,
                yAxisIndex: 2,
                data: chartData2,

            },
            {
                name: 'IV',
                type:'scatter',
                symbolSize:5,

                smooth:true,
                xAxisIndex: 3,
                yAxisIndex: 3,
                data: chartData3,

            }
        ]
    };


    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


//判断当前浏览器是否支持WebSocket
    if ('WebSocket' in window) {
        //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
        websocket = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
    } else {
        setMessageInnerHTML('当前浏览器 Not support websocket')
    }

//连接发生错误的回调方法

    websocket.onerror = function () {
        setMessageInnerHTML("WebSocket连接发生错误");
    };

//连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
//     var sub_figure1 = document.getElementById('figure1');
    var sub_figure1=$("#figure1").val();
    var sub_figure2=$("#figure2").val();
    var sub_figure3=$("#figure3").val();
    var sub_figure4=$("#figure4").val();

    websocket.onopen = function () {
        websocket.send(sub_figure1+','+sub_figure2+','+sub_figure3+','+sub_figure4);


        setMessageInnerHTML("WebSocket连接成功");

    }

//接收到消息的回调方法
       websocket.onmessage = function (event) {
/////////////////多个数据共同接收
           //
           // alert('hello world')
           //     var arrstr = event.data;
           //     var numofdata=1;
           //     // alert(arrstr);
           //     msg = JSON.parse(arrstr);
           //     setMessageInnerHTML(msg['sin']);
           //     datasin=msg[sub_figure1];
           //     for (var i=0;i<numofdata;i++) {
           //         chartData.push(datasin[i].split(','));
           //            if (chartData.length >= 62 * 2) {
           //                chartData.shift();
           //            }
           //     }
           //    datasin=msg[sub_figure2];
           //     for (var i=0;i<numofdata;i++) {
           //         chartData1.push(datasin[i].split(','));
           //            if (chartData1.length >= 62 * 2) {
           //                chartData1.shift();
           //            }
           //
           //     }
           //          datasin=msg[sub_figure3];
           //     for (var i=0;i<numofdata;i++) {
           //         chartData2.push(datasin[i].split(','));
           //            if (chartData2.length >= 62 * 2) {
           //                chartData2.shift();
           //            }
           //
           //     }
           //          datasin=msg[sub_figure4];
           //     for (var i=0;i<numofdata;i++) {
           //         chartData3.push(datasin[i].split(','));
           //            if (chartData3.length >= 62 * 2) {
           //                chartData3.shift();
           //            }
           //
           //     }
           ////////////////////单个数据接收///四个数据的部分
           var arrstr = event.data;
           msg = JSON.parse(arrstr);
           // alert(msg['sin']);
           setMessageInnerHTML(msg['sin']);
           chartData.push(msg[sub_figure1]);
           if (chartData.length >= 62 * 2) {
               chartData.shift();
           }
           chartData1.push(msg[sub_figure2]);
           if (chartData1.length >= 62 * 2) {
               chartData1.shift();
           }
           chartData2.push(msg[sub_figure3]);
           if (chartData2.length >= 62 * 2) {
               chartData2.shift();
           }
           chartData3.push(msg[sub_figure4]);
           if (chartData3.length >= 62 * 2) {
               chartData3.shift();
           }
           // reloadData()




       };

       //}
           /*
        if (arrstr.indexOf('triangle')!=-1)
        {
            // setMessageInnerHTML('that us ok');
            var arrnum = arrstr.split('+');
            var arr = arrnum[1].split(',')
            chartData1.push(arr)
            if (chartData1.length >= 62 * 2) {
                chartData1.shift();
                }
        };

        if (arrstr.indexOf('square')!=-1)
        {
            // setMessageInnerHTML('that us ok');
            var arrnum = arrstr.split('+');
            var arr = arrnum[1].split(',')
            chartData2.push(arr)
            if (chartData2.length >= 62 * 2) {
                chartData2.shift();
                }
        };

        if (arrstr.indexOf('sawtooth')!=-1)
        {
            // setMessageInnerHTML('that us ok');
            var arrnum = arrstr.split('+');
            var arr = arrnum[1].split(',')
            chartData3.push(arr)
            if (chartData3.length >= 62 * 2) {
                chartData3.shift();
                }
*/

setInterval(function (){reloadData1();},10);
setInterval(function (){reloadData2();},10);
setInterval(function (){reloadData3();},10);
setInterval(function (){reloadData4();},10);

        //   location.reload();
        // reloadData();
        // websocket.send('we are going to subscribe sin cos');

var reloadData = function () {
    reloadData1();
    reloadData2();
    reloadData3();
    reloadData4();

}



    var reloadData1 = function () {

        option = {

            series: [
                {
                    name: 'I',
                    type:'line',
                    smooth:true,
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    data: chartData,



                }
                ]

        };

        //console.log(option);
        if (option && typeof option === "object") {
            myChart.setOption(option);
        }





}

    var reloadData2 = function () {

        option = {

            series: [

                {
                    name: 'II',
                    type:'line',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    data: chartData1,


                },

            ]
        };

        //console.log(option);
        if (option && typeof option === "object") {
            myChart.setOption(option);
        }





}

    var reloadData3 = function () {

        option = {
            series:
                [
                {
                    name: 'III',
                    type:'line',
                    xAxisIndex: 2,
                    yAxisIndex: 2,
                    data: chartData2,


                },

            ]
        };

        //console.log(option);
        if (option && typeof option === "object") {
            myChart.setOption(option);
        }





}

    var reloadData4 = function () {

        option = {

            series: [

                {
                    name: 'IV',
                    type:'line',
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

};






function setMessageInnerHTML(innerHTML) {
    console.log(innerHTML);

}


function realtime_stop(){

        websocket.close();

}



