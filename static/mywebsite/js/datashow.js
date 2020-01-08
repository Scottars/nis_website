






function realtime_datashow(){
    // var ele = document.getElementById("realtime-menu");
    // ele.style.display="block";

    $("#realtime-menu").css("display","block");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","none");
    $("#systemmonitor-menu").css("display","none");
    $("#expinfo-menu").css("display","none");


    $("#realtimeshowall").css("display","block");
    $("#realtime_showarea").css("display","block");
    $("#realtime_showarea1").css("display","block");
    $("#realtime_showarea2").css("display","block");
    $("#realtime_showarea3").css("display","block");

    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","none");


    $(".function-button .menu-li li").css("color","red")
    $("#systemmonitor_showarea").css("display","none");
    $("#expinfo_register_showarea").css("display","none");






}

function history_datashow(){


    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","block");
    $("#download-menu").css("display","none");
    $("#systemmonitor-menu").css("display","none");
    $("#expinfo-menu").css("display","none");


    $("#realtimeshowall").css("display","none");
    $("#realtime_showarea").css("display","none");
    $("#realtime_showarea1").css("display","none");
    $("#realtime_showarea2").css("display","none");
    $("#realtime_showarea3").css("display","none");


    $("#history_showarea").css("display","block");
    $("#download_showarea").css("display","none");
    $("#systemmonitor_showarea").css("display","none");
    $("#expinfo_register_showarea").css("display","none");



}
function download_datashow(){


    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","block");
    $("#systemmonitor-menu").css("display","none");
    $("#expinfo-menu").css("display","none");



    $("#realtimeshowall").css("display","none");
    $("#realtime_showarea").css("display","none");
    $("#realtime_showarea1").css("display","none");
    $("#realtime_showarea2").css("display","none");
    $("#realtime_showarea3").css("display","none");

    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","block");
    $("#systemmonitor_showarea").css("display","none");
    $("#expinfo_register_showarea").css("display","none");


}
function system_monitor(){



    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","none");


    $("#systemmonitor-menu").css("display","block");
    $("#expinfo-menu").css("display","none");



    $("#realtimeshowall").css("display","none");
    $("#realtime_showarea").css("display","none");
    $("#realtime_showarea1").css("display","none");
    $("#realtime_showarea2").css("display","none");
    $("#realtime_showarea3").css("display","none");


    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","none");

    $("#systemmonitor_showarea").css("display","block");
    $("#expinfo_register_showarea").css("display","none");



}

function expinfo_register() {

    $("#realtime-menu").css("display","none");
    $("#history-menu").css("display","none");
    $("#download-menu").css("display","none");
    $("#systemmonitor-menu").css("display","none");
    $("#expinfo-menu").css("display","block");



    $("#realtimeshowall").css("display","none");
    $("#realtime_showarea").css("display","none");
    $("#realtime_showarea1").css("display","none");
    $("#realtime_showarea2").css("display","none");
    $("#realtime_showarea3").css("display","none");
    $("#history_showarea").css("display","none");
    $("#download_showarea").css("display","none");

    $("#systemmonitor_showarea").css("display","none");
    $("#expinfo_register_showarea").css("display","block");





}
var process_monitor_timer;
var monitor_start;
function process_monitor_timer_start() {
    process_monitor_timer=setInterval(process_status_update, 1000);
    monitor_start=setInterval(monitor_start_running_on, 1000);

}


function clearprocess_monitor_timer() {
    clearInterval(process_monitor_timer);
    clearInterval(monitor_start);

}
function monitor_start_running_on() {
        $("#id_monitor_status").attr('class','monitor-running-on')
        setTimeout(monitor_start_running_off,500)
}
function monitor_start_running_off() {
        $("#id_monitor_status").attr('class','monitor-running-off')
}
function process_status_update() {

    console.log('we are at update fuicntion ')

    $.ajax({
            type: "GET",
            url: "/dataview/process_status_update", //后台处理函数的url
            cache: false,
            dataType: "json",
            success: function (result) {

                console.log(result);
                var process_names = result.process_names;
                var process_statuses = result.process_statuses;
                for (i in process_names) {
                    console.log(process_names[i]);
                    console.log(process_statuses[i]);

                    if (process_statuses[i]=='on'){
                        console.log(process_names[i]);
                        console.log(process_statuses[i]);
                        console.log()
                        $("#"+process_names[i]).attr('class','system-process-on')
                    }
                    else {
                        console.log(process_names[i]);
                        console.log(process_statuses[i]);
                        $("#"+process_names[i]).attr('class','system-process-off')
                    }
                }

            },
            error: function () {
                alert("false");
            }
        }
    );

}


laydate.render({
    elem: '#id_start_time'
    , type: 'datetime'
});
var websocket = null;
var websocket1 = null;
var websocket2 = null;
var websocket3 = null;

function realtimestartall() {
    realtime_start();
    realtime_start1();
    realtime_start2();
    realtime_start3();
}
//class .   id #
// function realtime_start() {
//
//     var app = {};
//     var chartData = [];
//
//     var chartData1 = [];
//     var chartData2 = [];
//     var chartData3 = [];
//     var dom = document.getElementById("realtime_showarea");
//     var myChart = echarts.init(dom);
//     var option = null;
//     option = {
//         title: {
//             text: 'Anscombe\'s quartet',
//             x: 'center',
//             y: 0
//         },
//         grid: [
//             {x: '7%', y: '7%', width: '38%', height: '38%'},
//             // {x2: '7%', y: '7%', width: '38%', height: '38%'},
//             // {x: '7%', y2: '7%', width: '38%', height: '38%'},
//             // {x2: '7%', y2: '7%', width: '38%', height: '38%'}
//         ],
//         tooltip: {
//             formatter: 'Group {a}: ({c})'
//         },
//         xAxis: [
//             //{scale:'True'},
//
//             {gridIndex: 0, scale: 'True', splitLine: {show: false}, type: 'value', show: false,},
//             // {gridIndex: 1, scale: 'True', splitLine: {show: false}, type: 'value', show: false,},
//             // {gridIndex: 2, scale: 'True', splitLine: {show: false}, type: 'value', show: false,},
//             // {gridIndex: 3, scale: 'True', splitLine: {show: false}, type: 'value', show: false,}
//         ],
//         yAxis: [
//             {gridIndex: 0, splitLine: {show: false}, type: 'value',},
//             // {gridIndex: 1, splitLine: {show: false}, type: 'value',},
//             // {gridIndex: 2, splitLine: {show: false}, type: 'value',},
//             // {gridIndex: 3, splitLine: {show: false}, type: 'value',}
//         ],
//         series: [
//             {
//                 name: 'I',
//                 type: 'scatter',
//                 symbolSize: 5,
//                 smooth: true,
//                 xAxisIndex: 0,
//                 yAxisIndex: 0,
//                 data: chartData,
//             },
//             // {
//             //     name: 'II',
//             //     type: 'scatter',
//             //     symbolSize: 5,
//             //
//             //     smooth: true,
//             //     xAxisIndex: 1,
//             //     yAxisIndex: 1,
//             //     data: chartData1,
//             //
//             // },
//             // {
//             //     name: 'III',
//             //     type: 'scatter',
//             //     symbolSize: 5,
//             //
//             //     smooth: true,
//             //     xAxisIndex: 2,
//             //     yAxisIndex: 2,
//             //     data: chartData2,
//             //
//             // },
//             // {
//             //     name: 'IV',
//             //     type: 'scatter',
//             //     symbolSize: 5,
//             //
//             //     smooth: true,
//             //     xAxisIndex: 3,
//             //     yAxisIndex: 3,
//             //     data: chartData3,
//             //
//             // }
//         ]
//     };
//
//     var dom1 = document.getElementById("realtime_showarea1");
//     var myChart1 = echarts.init(dom1);
//     var option1 = null;
//     option1=option;
//     var dom2 = document.getElementById("realtime_showarea2");
//     var myChart2 = echarts.init(dom2);
//     var option2 = null;
//     option2=option;
//     var dom3 = document.getElementById("realtime_showarea3");
//     var myChart3 = echarts.init(dom3);
//     var option3 = null;
//     option3=option;
//
//
//
//
//     if (option && typeof option === "object") {
//         myChart.setOption(option, true);
//     }
// if (option1 && typeof option1 === "object") {
//         myChart1.setOption(option1, true);
//     }
// if (option2 && typeof option2 === "object") {
//         myChart2.setOption(option2, true);
//     }
// if (option3 && typeof option3 === "object") {
//         myChart3.setOption(option3, true);
//     }
//
// //判断当前浏览器是否支持WebSocket
//     if ('WebSocket' in window) {
//         //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
//         websocket = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
//     } else {
//         setMessageInnerHTML('当前浏览器 Not support websocket')
//     }
//
// //连接发生错误的回调方法
//
//     websocket.onerror = function () {
//         setMessageInnerHTML("WebSocket连接发生错误");
//     };
//
// //连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
// //     var sub_figure1 = document.getElementById('figure1');
//     var sub_figure = $("#figure1").val();
//     var sub_figure1 = $("#figure2").val();
//     var sub_figure2 = $("#figure3").val();
//     var sub_figure3 = $("#figure4").val();
//
//     websocket.onopen = function () {
//         websocket.send(sub_figure + ',' + sub_figure1 + ',' + sub_figure2 + ',' + sub_figure3);
//
//
//         setMessageInnerHTML("WebSocket连接成功");
//
//     }
//
// //接收到消息的回调方法
//     websocket.onmessage = function (event) {
// /////////////////多个数据共同接收
//         //
//         var arrstr = event.data;
//         var numofdata = 10;
//         // alert(arrstr);
//         // msg = JSON.parse(arrstr);
//         // setMessageInnerHTML(arrstr);
//         // datasin=msg[sub_figure1];
//         //
//         // for (var i=0;i<numofdata;i++) {
//         //     setMessageInnerHTML('daasiniiii')
//         //     setMessageInnerHTML(datasin[i])
//         //     chartData.push(datasin[i].split(','));
//         //        if (chartData.length >= 62 * 2) {
//         //            chartData.shift();
//         //        }
//         // }
//
//         // datasin=msg[sub_figure2];
//         //  for (var i=0;i<numofdata;i++) {
//         //      chartData1.push(datasin[i].split(','));
//         //         if (chartData1.length >= 62 * 2) {
//         //             chartData1.shift();
//         //         }
//         //
//         //  }
//         //       datasin=msg[sub_figure3];
//         //  for (var i=0;i<numofdata;i++) {
//         //      chartData2.push(datasin[i].split(','));
//         //         if (chartData2.length >= 62 * 2) {
//         //             chartData2.shift();
//         //         }
//         //
//         //  }
//         //       datasin=msg[sub_figure4];
//         //  for (var i=0;i<numofdata;i++) {
//         //      chartData3.push(datasin[i].split(','));
//         //         if (chartData3.length >= 62 * 2) {
//         //             chartData3.shift();
//         //         }
//         //
//         //  }
//         ////////////////////单个数据接收///四个数据的部分
//         var arrstr = event.data;
//         msg = JSON.parse(arrstr);
//         // alert(msg['sin']);
//         setMessageInnerHTML(msg);
//         setMessageInnerHTML(sub_figure1);
//         setMessageInnerHTML(msg[sub_figure1]);
//
//         if (msg[sub_figure]!=undefined){
//             setMessageInnerHTML('这个时候才刷新否则不刷新1')
//
//         chartData.push(msg[sub_figure]);
//         if (chartData.length >= 62 * 2) {
//             chartData.shift();
//         }
//             reloadData0()
//         }
//
//         if (msg[sub_figure1]!=undefined){
//             setMessageInnerHTML('这个时候才刷新否则不刷新2')
//
//         chartData1.push(msg[sub_figure1]);
//         if (chartData1.length >= 62 * 2) {
//             chartData1.shift();
//         }
//             reloadData1()
//         }
//
//         if (msg[sub_figure2]!=undefined){
//
//             setMessageInnerHTML('这个时候才刷新否则不刷新3')
//         chartData2.push(msg[sub_figure2]);
//         if (chartData2.length >= 62 * 2) {
//             chartData2.shift();
//         }
//             reloadData2()
//         }
//
//         if (msg[sub_figure3]!=undefined){
//         chartData3.push(msg[sub_figure4]);
//         if (chartData3.length >= 62 * 2) {
//             chartData3.shift();
//         }
//             setMessageInnerHTML('这个时候才刷新否则不刷新4')
//             reloadData3()
//         }
//         // reloadData();
//
//
//         // function reloadData() {
//         //     option = {
//         //
//         //         series: [
//         //             {
//         //                 name: 'I',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 0,
//         //                 yAxisIndex: 0,
//         //                 data: chartData,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'II',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 1,
//         //                 yAxisIndex: 1,
//         //                 data: chartData1,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'III',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 2,
//         //                 yAxisIndex: 2,
//         //                 data: chartData2,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'VI',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 3,
//         //                 yAxisIndex: 3,
//         //                 data: chartData3,
//         //
//         //
//         //             }
//         //
//         //
//         //         ]
//         //
//         //     };
//         //
//         //     //console.log(option);
//         //     if (option && typeof option === "object") {
//         //         myChart.setOption(option);
//         //     }
//         //
//         //      option1 = {
//         //
//         //         series: [
//         //             {
//         //                 name: 'I',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 0,
//         //                 yAxisIndex: 0,
//         //                 data: chartData1,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'II',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 1,
//         //                 yAxisIndex: 1,
//         //                 data: chartData1,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'III',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 2,
//         //                 yAxisIndex: 2,
//         //                 data: chartData1,
//         //
//         //
//         //             },
//         //                       {
//         //                 name: 'VI',
//         //                 type: 'scatter',
//         //                 smooth: true,
//         //                 xAxisIndex: 3,
//         //                 yAxisIndex: 3,
//         //                 data: chartData1,
//         //
//         //
//         //             }
//         //
//         //
//         //         ]
//         //
//         //     };
//         //
//         //     //console.log(option);
//         //     if (option1 && typeof option1 === "object") {
//         //         myChart1.setOption(option1);
//         //     }
//         //
//         //
//         // }
//
//
//         // setInterval(function () {
//         //     reloadData3();
//         // }, 100);
//         // setInterval(function () {
//         //     reloadData4();
//         // }, 100);
//
//
//     }
//
//         function reloadData0() {
//             option = {
//
//                 series: [
//                     {
//                         name: 'I',
//                         type: 'scatter',
//                         smooth: true,
//                         xAxisIndex: 0,
//                         yAxisIndex: 0,
//                         data: chartData,
//                     },
//
//
//                 ]
//
//             };
//
//             //console.log(option);
//             if (option && typeof option === "object") {
//                 myChart.setOption(option);
//             }
//
//
//
//         }
//         function reloadData1() {
//
//
//             //console.log(option);
//
//              option1 = {
//
//                  series: [
//
//                      {
//                          name: 'I',
//                          type: 'scatter',
//                          smooth: true,
//                          xAxisIndex: 0,
//                          yAxisIndex: 0,
//                          data: chartData1,
//
//
//
//                      },
//                  ]
//              }
//
//             //console.log(option);
//             if (option1 && typeof option1 === "object") {
//                 myChart1.setOption(option1);
//             }
//
//
//         }
//       function reloadData2() {
//
//
//             //console.log(option);
//
//              option2 = {
//
//                  series: [
//
//                      {
//                          name: 'I',
//                          type: 'scatter',
//                          smooth: true,
//                          xAxisIndex: 0,
//                          yAxisIndex: 0,
//                          data: chartData2,
//
//
//
//                      },
//                  ]
//              }
//
//             //console.log(option);
//             if (option2 && typeof option2 === "object") {
//                 myChart2.setOption(option2);
//             }
//
//
//         }
//       function reloadData3() {
//
//
//             //console.log(option);
//              option3 = {
//
//                  series: [
//
//                      {
//                          name: 'I',
//                          type: 'scatter',
//                          smooth: true,
//                          xAxisIndex: 0,
//                          yAxisIndex: 0,
//                          data: chartData3,
//
//
//
//                      },
//                  ]
//              }
//
//             //console.log(option);
//             if (option3 && typeof option3 === "object") {
//                 myChart3.setOption(option3);
//             }
//
//
//         }
//
//
//
//         //
//         // setInterval(function () {
//         //     reloadData0();
//         // }, 100);
//         // setInterval(function () {
//         //     reloadData1();
//         // }, 100);
// }
function realtime_start() {

    var app = {};
    var chartData1 = [];
    var chartData2 = [];
    var chartData3 = [];

    var dom = document.getElementById("realtime_showarea");
    var myChart = echarts.init(dom);
    var option = null;
      option = null;
        option = {
            xAxis: [{
                splitLine:{show:false},
                show:false,
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData1,
                type: 'scatter'
            }]
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
    websocket.onclose = function () {


        setMessageInnerHTML("WebSocket关闭连接");

    }
//连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
//     var sub_figure1 = document.getElementById('figure1');
//     var sub_figure1 = $("#figure1").val();
    var sub_figure = $("#figure1").val();
    // var sub_figure3 = $("#figure3").val();
    // var sub_figure4 = $("#figure4").val();

    websocket.onopen = function () {
        websocket.send(sub_figure);


        setMessageInnerHTML("WebSocket连接成功");

    }

//接收到消息的回调方法
    websocket.onmessage = function (event) {
/////////////////多个数据共同接收
        //
        var arrstr = event.data;
        var numofdata = 10;
        // alert(arrstr);
        // msg = JSON.parse(arrstr);
        // setMessageInnerHTML(arrstr);
        // datasin=msg[sub_figure1];
        //
        // for (var i=0;i<numofdata;i++) {
        //     setMessageInnerHTML('daasiniiii')
        //     setMessageInnerHTML(datasin[i])
        //     chartData.push(datasin[i].split(','));
        //        if (chartData.length >= 62 * 2) {
        //            chartData.shift();
        //        }
        // }

        // datasin=msg[sub_figure2];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData1.push(datasin[i].split(','));
        //         if (chartData1.length >= 62 * 2) {
        //             chartData1.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure3];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData2.push(datasin[i].split(','));
        //         if (chartData2.length >= 62 * 2) {
        //             chartData2.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure4];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData3.push(datasin[i].split(','));
        //         if (chartData3.length >= 62 * 2) {
        //             chartData3.shift();
        //         }
        //
        //  }
        ////////////////////单个数据接收///四个数据的部分
        var arrstr = event.data;
        msg = JSON.parse(arrstr);
        // alert(msg['sin']);
        setMessageInnerHTML(sub_figure);
        setMessageInnerHTML(msg[sub_figure]);
        // chartData.push(msg[sub_figure1]);
        chartData1.push(msg[sub_figure]);
        if (chartData1.length >= 62 * 2) {
            chartData1.shift();
        }
        // reloadata1()
        }





        // setInterval(function () {
        //     reloadData2();
        // }, 100);
        // setInterval(function () {
        //     reloadData3();
        // }, 100);
        // setInterval(function () {
        //     reloadData4();
        // }, 100);
    function reloadata1() {
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData1,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    }
    setInterval(function () {reloadata1(); }, 100);
}
function realtime_start1() {

    var app = {};
    var chartData1 = [];
    var chartData2 = [];
    var chartData3 = [];

    var dom = document.getElementById("realtime_showarea1");
    var myChart = echarts.init(dom);
    var option = null;
      option = null;
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData1,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


//判断当前浏览器是否支持WebSocket
    if ('WebSocket' in window) {
        //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
        websocket1 = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
    } else {
        setMessageInnerHTML('当前浏览器 Not support websocket')
    }

//连接发生错误的回调方法

    websocket1.onerror = function () {
        setMessageInnerHTML("WebSocket连接发生错误");
    };
    websocket1.onclose = function () {


        setMessageInnerHTML("WebSocket关闭连接");

    }

//连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
//     var sub_figure1 = document.getElementById('figure1');
//     var sub_figure1 = $("#figure1").val();
    var sub_figure1 = $("#figure2").val();
    // var sub_figure3 = $("#figure3").val();
    // var sub_figure4 = $("#figure4").val();

    websocket1.onopen = function () {
        websocket1.send(sub_figure1);


        setMessageInnerHTML("WebSocket连接成功");

    }

//接收到消息的回调方法
    websocket1.onmessage = function (event) {
/////////////////多个数据共同接收
        //
        var arrstr = event.data;
        var numofdata = 10;
        // alert(arrstr);
        // msg = JSON.parse(arrstr);
        // setMessageInnerHTML(arrstr);
        // datasin=msg[sub_figure1];
        //
        // for (var i=0;i<numofdata;i++) {
        //     setMessageInnerHTML('daasiniiii')
        //     setMessageInnerHTML(datasin[i])
        //     chartData.push(datasin[i].split(','));
        //        if (chartData.length >= 62 * 2) {
        //            chartData.shift();
        //        }
        // }

        // datasin=msg[sub_figure2];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData1.push(datasin[i].split(','));
        //         if (chartData1.length >= 62 * 2) {
        //             chartData1.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure3];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData2.push(datasin[i].split(','));
        //         if (chartData2.length >= 62 * 2) {
        //             chartData2.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure4];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData3.push(datasin[i].split(','));
        //         if (chartData3.length >= 62 * 2) {
        //             chartData3.shift();
        //         }
        //
        //  }
        ////////////////////单个数据接收///四个数据的部分
        var arrstr = event.data;
        msg = JSON.parse(arrstr);
        // alert(msg['sin']);
        setMessageInnerHTML(sub_figure1);
        setMessageInnerHTML(msg[sub_figure1]);
        // chartData.push(msg[sub_figure1]);
        chartData1.push(msg[sub_figure1]);
        if (chartData1.length >= 62 * 2) {
            chartData1.shift();
        }
        // reloadata1()
        };




        setInterval(function () {reloadata1(); }, 100);
        // setInterval(function () {
        //     reloadData2();
        // }, 100);
        // setInterval(function () {
        //     reloadData3();
        // }, 100);
        // setInterval(function () {
        //     reloadData4();
        // }, 100);
    function reloadata1() {
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData1,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    }


    }
function realtime_start2() {

    var app = {};
    var chartData = [];
    var chartData1 = [];
    var chartData2 = [];
    var chartData3 = [];

    var dom = document.getElementById("realtime_showarea2");
    var myChart = echarts.init(dom);
    var option = null;
      option = null;
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


//判断当前浏览器是否支持WebSocket
    if ('WebSocket' in window) {
        //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
        websocket2 = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
    } else {
        setMessageInnerHTML('当前浏览器 Not support websocket')
    }

//连接发生错误的回调方法

    websocket2.onerror = function () {
        setMessageInnerHTML("WebSocket连接发生错误");
    };
websocket2.onclose = function () {


        setMessageInnerHTML("WebSocket关闭连接");

    }
//连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
    var sub_figure2 = $("#figure3").val();

    websocket2.onopen = function () {
        websocket2.send(sub_figure2);


        setMessageInnerHTML("WebSocket连接成功");

    }

//接收到消息的回调方法
    websocket2.onmessage = function (event) {
/////////////////多个数据共同接收
        //
        var arrstr = event.data;
        var numofdata = 10;
        // alert(arrstr);
        // msg = JSON.parse(arrstr);
        // setMessageInnerHTML(arrstr);
        // datasin=msg[sub_figure1];
        //
        // for (var i=0;i<numofdata;i++) {
        //     setMessageInnerHTML('daasiniiii')
        //     setMessageInnerHTML(datasin[i])
        //     chartData.push(datasin[i].split(','));
        //        if (chartData.length >= 62 * 2) {
        //            chartData.shift();
        //        }
        // }

        // datasin=msg[sub_figure2];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData1.push(datasin[i].split(','));
        //         if (chartData1.length >= 62 * 2) {
        //             chartData1.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure3];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData2.push(datasin[i].split(','));
        //         if (chartData2.length >= 62 * 2) {
        //             chartData2.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure4];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData3.push(datasin[i].split(','));
        //         if (chartData3.length >= 62 * 2) {
        //             chartData3.shift();
        //         }
        //
        //  }
        ////////////////////单个数据接收///四个数据的部分
        var arrstr = event.data;
        msg = JSON.parse(arrstr);
        chartData.push(msg[sub_figure2]);
        if (chartData.length >= 62 * 2) {
            chartData.shift();
        }
        // reloadata1()
        }




        setInterval(function () {reloadata1(); }, 100);
        // setInterval(function () {
        //     reloadData2();
        // }, 100);
        // setInterval(function () {
        //     reloadData3();
        // }, 100);
        // setInterval(function () {
        //     reloadData4();
        // }, 100);
    function reloadata1() {
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    }


    }
function realtime_start3() {

    var app = {};
    var chartData = [];
    var chartData1 = [];
    var chartData2 = [];
    var chartData3 = [];

    var dom = document.getElementById("realtime_showarea3");
    var myChart = echarts.init(dom);
    var option = null;
      option = null;
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


//判断当前浏览器是否支持WebSocket
    if ('WebSocket' in window) {
        //建立连接，这里的/websocket ，是ManagerServlet中开头注解中的那个值
        websocket3 = new WebSocket('ws://' + window.location.host + '/ws/realtimeshow/');
    } else {
        setMessageInnerHTML('当前浏览器 Not support websocket')
    }

//连接发生错误的回调方法

    websocket3.onerror = function () {
        setMessageInnerHTML("WebSocket连接发生错误");
    };
    websocket3.onclose = function () {


        setMessageInnerHTML("WebSocket关闭连接");

    }

//连接成功建立的回调方法,如果这个函数，还没有执行，就已经执行了发送的部分，就会发送不成功了啊
    var sub_figure3 = $("#figure4").val();

    websocket3.onopen = function () {
        websocket3.send(sub_figure3);


        setMessageInnerHTML("WebSocket连接成功");

    }

//接收到消息的回调方法
    websocket3.onmessage = function (event) {
/////////////////多个数据共同接收
        //
        var arrstr = event.data;
        var numofdata = 10;
        // alert(arrstr);
        // msg = JSON.parse(arrstr);
        // setMessageInnerHTML(arrstr);
        // datasin=msg[sub_figure1];
        //
        // for (var i=0;i<numofdata;i++) {
        //     setMessageInnerHTML('daasiniiii')
        //     setMessageInnerHTML(datasin[i])
        //     chartData.push(datasin[i].split(','));
        //        if (chartData.length >= 62 * 2) {
        //            chartData.shift();
        //        }
        // }

        // datasin=msg[sub_figure2];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData1.push(datasin[i].split(','));
        //         if (chartData1.length >= 62 * 2) {
        //             chartData1.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure3];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData2.push(datasin[i].split(','));
        //         if (chartData2.length >= 62 * 2) {
        //             chartData2.shift();
        //         }
        //
        //  }
        //       datasin=msg[sub_figure4];
        //  for (var i=0;i<numofdata;i++) {
        //      chartData3.push(datasin[i].split(','));
        //         if (chartData3.length >= 62 * 2) {
        //             chartData3.shift();
        //         }
        //
        //  }
        ////////////////////单个数据接收///四个数据的部分
        var arrstr = event.data;
        msg = JSON.parse(arrstr);
        chartData.push(msg[sub_figure3]);
        if (chartData.length >= 62 * 2) {
            chartData.shift();
        }
        // reloadata1()
        }




        setInterval(function () {reloadata1(); }, 100);
        // setInterval(function () {
        //     reloadData2();
        // }, 100);
        // setInterval(function () {
        //     reloadData3();
        // }, 100);
        // setInterval(function () {
        //     reloadData4();
        // }, 100);
    function reloadata1() {
        option = {
            xAxis: [{
                splitLine:{show:false},
                scale:true,
                type:'value',
            }
            ],
            yAxis: [{
                splitLine:{show:false},
                type:'value',
            }],
            series: [{
                symbolSize: 5,
                data: chartData,
                type: 'scatter'
            }]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    }


    }
function filtertest(){
    alert('test okay');

    $("#filter_f_watercolddown").html('this is new');
}
// $('#refresh').click(function() {
//     comment.children().remove();
//     comment.load('comment.html #comment');//用法参考jQuery的load函数
// });

// $(document).ready(function(){               //元素加载完成之后，绑定事件
//     $("#historydata_show").click(function(){       //给按钮的点击效果，绑定一个事件
//         console.log('we are ready to ajsax')
//         $.ajaxSetup({
//             data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
//         });
//
//         $.ajax({                    //调用ajax
//             url:"{% url 'datasearch' %}",  //发出请求的地址
//             success:function(result){$("#forasynload").html(result);}
//             // 服务器成功响应后，绑定的事件
//         });
//     });
// });
function down(){
    var url = "http://192.168.1.101:8080/"
    var request = new XMLHttpRequest();
    request.open("POST", url);
    request.send("F")
}
function drawhistory(result) {

    var dom = document.getElementById(result.v_name);
    var myChart = echarts.init(dom);
    var chartData = [];
    var option = null;
    option = null;
    var v_data_times = result.v_data_times;
    var v_data_value = result.v_data_values;
    var v_data_xy = []
    var time_value = []
    chartData = v_data_value;
    // console.log(chartData);
    // console.log(v_data_times);
    for (i in v_data_times) {
        // console.log(v_data_times[i]);

        var date = new Date(v_data_times[i]);
        // console.log(date.getTime());

        // console.log(date.getSeconds()*1000+date.getMilliseconds());

        v_data_xy.push([date.getSeconds() * 1000 + date.getMilliseconds(), v_data_value[i]]);
        // time_value.push(date.getSeconds()*1000+date.getMilliseconds())
    }
    // console.log(v_data_xy);

    option = {
        tooltip: {
            /*返回需要的信息*/
            show:true,
            // formatter: 'Group {a}: ({c})'
        },

        dataZoom: [
            {
                type: 'slider',
                xAxisIndex: 0,
                start: 0,
                end: 100
            },
            {
                type: 'inside',
                xAxisIndex: 0,
                start: 0,
                end: 100
            },
            {
                type: 'slider',
                yAxisIndex: 0,
                start: 0,
                end: 100
            },
            {
                type: 'inside',
                yAxisIndex: 0,
                start: 0,
                end: 100
            }
        ],
        xAxis: [{
            splitLine: {show: false},
            // show:false,
            scale: true,
            type: 'value',
            // data:charx,
        }
        ],
        yAxis: [{
            splitLine: {show: false},
            type: 'value',
            // data:chary,
        }],
        series: [{
            symbolSize: 5,
            data: v_data_xy,
            type: 'scatter'
        }]
    };

    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


}


// 这个函数是用来多选用的
$(document).ready(function() {
    $('#v_namechoose').multiselect();
    $('#download_v_namechoose').multiselect();
});
//这个函数用来获取搜索的数据
$('#historydata_show').click(function(){
    console.log('we are at clickc fuicntion ')
    var expid= $("#expid").val();
    var timechoose=$("#v_timechoose").val();
    // var namechoose=$("#v_namechoose").val();
    var multinamechoose=$("#v_namechoose").val();
    console.log(multinamechoose);
    var data1={'expid':expid,'timechoose':timechoose,'namechoose':JSON.stringify(multinamechoose)};
    console.log(data1);

    $.ajax({
        type:"GET",
        data: data1,
        url: "/dataview/getdata", //后台处理函数的url
        cache: false,
        dataType: "json",
        success: function(result){

            // console.log(result);
            var managers = result.exp_managers;
            var resultsub=result.v_names_datas;
            // document.getElementById("filter_f_watercolddown").innerHTML='this is after'
            // var test = "<div id='' style='color: yellow'>"+managers[0]+"</div>";
            // $("#fortest").html(test);
            console.log(resultsub)
            for (a in resultsub){
                drawhistory(resultsub[a])

            }
        },
        error: function(){
            alert("false");
        }
    });
    return false;
});
//这个函数用来下载得到的数据
// var postDownLoadFile = function (options) {
//     var config = $.extend(true, { method: 'post' }, options);
//     var $iframe = $('<iframe id="down-file-iframe" />');
//     var $form = $('<form target="down-file-iframe" method="' + config.method + '" />');
//     $form.attr('action', config.url);
//     for (var key in config.data) {
//         $form.append('<input type="hidden" name="' + key + '" value="' + config.data[key] + '" />');
//     }
//     $iframe.append($form);
//     $(document.body).append($iframe);
//     $form[0].submit();
//     $iframe.remove();
// }
// $("#datadownload_btn").on('click',
//         function() {
//           var param={};
//           postDownLoadFile({
//             url:'/dataview/data_download',
//             data:param,
//             method:'post'
//           });
//         });

$('#datadownload_btn').click(function(){
    console.log('we are at download fuicntion ')
    var expid= $("#expid").val();
    var timechoose=$("#v_timechoose").val();
    // var namechoose=$("#v_namechoose").val();
    var multinamechoose=$("#v_namechoose").val();
    console.log(multinamechoose);
    expid=3;
    var data1={'expid':'2','timechoose':timechoose,'namechoose':JSON.stringify(multinamechoose)};
    console.log(data1);
    // $.ajaxSetup({
    //     headers: { "X-CSRFToken": getCookie("csrftoken") }
    // });

    $.ajax({
        type:"POST",
        data: data1,
        url: "/dataview/excel_export/", //后台处理函数的url
        dataType: "json",
        success: function(arg){
                console.log('后台反应会的数据');
                console.log(arg.data);
                 if (arg.code===0){
                    window.location.href='/dataview/excel_download?data='+arg.data+'';
                }else{
                    alert(arg.data)
                }

        },
        error: function(){
            alert("false");
        }
    });
    return false;
});

//导出事件
//             $('#btnExport').click(function (e) {
//                 e.preventDefault();//阻止a链接的跳转行为
//                 $.ajax({
//                     type: "post",
//                     url: "/FileExport/Export",
//                     dataType: "json",
//                     data: { address: addr},
//                     success: function (data) {
//                         $.download('/FileExport/DownLoadFile', 'post', data.value); // 下载文件
//                     },
//                     error: function (data) {
//                         alert("对不起，出现错误，请稍后重试或联系管理员");
//                     }
//                 });
//             });

// $(".historydata_show").click(function(){
//     $.ajax({
//         type:"get",
//         // data:{classify_id:$(this).attr("data-classify_id")},  //获取商品id
//         url:,  //调用后台方法
//         success:function(data){  //data是后台方法执行后的返回值
//             if(data.status==1){
//                 $("#table-info").load(location.href+" #table-info");  //这里是第一次用的局部刷新
//                 window.location.reload();  //刷新当前页面（这是最新加的刷新页面，自动执行完就可以二次点击了）
//             }
//         }
//     });
// });

/*最新补充，不能点击的原因是因为我的新增点击元素是动态新增的，所以需要重新绑定点击事件，如下：*/






function datashow_stop() {
    alert('this is history datashow stop');


}

function setMessageInnerHTML(innerHTML) {
    console.log(innerHTML);

}


function realtime_stop(){
    // websocket.disconnect();
    // websocket1.disconnect();
    // websocket2.disconnect();
    // websocket3.disconnect();

        websocket.close();
        websocket1.close();

        websocket2.close();
websocket3.close();
}







//History data 查询功能
function filterconditionchange() {

    console.log('we have trigger the  condition');

}