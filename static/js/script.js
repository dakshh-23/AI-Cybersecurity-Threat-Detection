const ctx =
document.getElementById(
'trafficChart'
).getContext('2d')

const trafficChart =
new Chart(ctx, {

type:'line',

data:{

labels:[],

datasets:[{

label:'Network Traffic',

data:[],

borderColor:'cyan',

borderWidth:3,

tension:0.4

}]

},

options:{
responsive:true
}

})

async function fetchData(){

const response =
await fetch('/live_data')

const data =
await response.json()

document.getElementById(
'traffic'
).innerText =
data.traffic

document.getElementById(
'threats'
).innerText =
data.threats

document.getElementById(
'cpu'
).innerText =
data.cpu + "%"

document.getElementById(
'ram'
).innerText =
data.ram + "%"

const status =
document.getElementById(
'status'
)

status.innerText =
data.status

if(data.status ==
"THREAT DETECTED"){

status.style.color =
"red"

addLog(
"⚠ Threat Detected"
)

}

else{

status.style.color =
"lime"

addLog(
"✅ Normal Traffic"
)

}

updateChart(data.traffic)

}

function addLog(message){

const logs =
document.getElementById(
'logs'
)

const div =
document.createElement('div')

div.className='log'

div.innerText =
new Date().toLocaleTimeString()
+ " - " + message

logs.prepend(div)

}

function updateChart(value){

trafficChart.data.labels.push('')

trafficChart.data.datasets[0]
.data.push(value)

if(
trafficChart.data.labels.length > 15
){

trafficChart.data.labels.shift()

trafficChart.data.datasets[0]
.data.shift()

}

trafficChart.update()

}

setInterval(fetchData,2000)

fetchData()