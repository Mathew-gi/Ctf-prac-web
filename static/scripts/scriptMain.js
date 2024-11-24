const socket = io();

var tasks_difficulties = document.getElementsByClassName("task_difficulty");
var tasks = document.getElementsByClassName("task");
var blurScreen = document.querySelector(".blur");
var blurOn = false;
var tasksLinks = document.getElementsByClassName("task_link");
var flag_submit_buttons = document.getElementsByClassName("task_flag_submit");
var trueFlagMsg = document.querySelector(".trueFlagMsg");
var taskLink = document.querySelector(".task_link");
var taskDescription = document.querySelector(".task_description");
var leadersTab = document.querySelector(".leaders_tab");
var tasksWebExtendedParts = document.getElementsByClassName("extended_task_part_web");
var leadersDiaogram = document.getElementById("leaders_diagram");
var profilePoints = document.querySelector(".profile_points");


var scrollDistance = 0;
window.onscroll = function(e) {
  scrollDistance = window.scrollY;
};

let ctx = document.querySelector(".leadersCanvas");
let lineChart = new Chart(ctx, {
    type: 'line',
    data:
            {
                labels: [],
                datasets: [{
                    label: "CTF-отдел",
                    data: [],
                    backgroundColor: ['#BFFF0000'],
                    borderColor: ['#FF6C5CFF'],
                    borderWidth: 4,
                    lineTension: 0.4
                },
                {
                    label: "ФМШ и Челики",
                    data: [],
                    backgroundColor: ['#121212'],
                    borderColor: ['#00AAFFFF'],
                    borderWidth: 4,
                    lineTension: 0.4
                }
        ]
            },
    options: {
        maintainAspectRatio: true,
        legend: {
            display: true
        }
    }
});




for (var i = 0; i < tasksWebExtendedParts.length; i++) {
    var editPoint = false;
    for (var j = 0; j < tasksWebExtendedParts[i].children.length; j++) {
        if (tasksWebExtendedParts[i].children[j].textContent == "1") {
            editPoint = true;
        }
    }
    if (editPoint) {
        for (var j = 0; j < tasksWebExtendedParts[i].children.length; j++) {
            tasksWebExtendedParts[i].children[j].style = "display: none;";
        }
        tasksWebExtendedParts[i].lastElementChild.style = "display: block;";
    }
}

for (var i = 0; i < tasks_difficulties.length; i++) {
    tasks_difficulties[i].className += " " + tasks_difficulties[i].textContent;

    var easyTasks = document.getElementsByClassName("easy");
    var mediumTasks = document.getElementsByClassName("medium");
    var hardTasks = document.getElementsByClassName("hard");

    for (var j = 0; j < easyTasks.length; j++) { 
        easyTasks[j].textContent = "Легко"
    }
    for (var j = 0; j < mediumTasks.length; j++) { 
        mediumTasks[j].textContent = "Нормально"
    }
    for (var j = 0; j < hardTasks.length; j++) { 
        hardTasks[j].textContent = "Сложно"
    }
}

for (var i = 0; i < tasksLinks.length; i++) {
    tasksLinks[i].lastElementChild.href = tasksLinks[i].lastElementChild.textContent;
    tasksLinks[i].lastElementChild.textContent = "Ссылка на задание";
}

function taskClick() {
    if (blurOn) {
    }
    else {
        this.className = "extended_task";
        console.log(`top: calc(50vh + ${scrollDistance});`);
        this.style = `top: calc(50vh + ${scrollDistance}px);`;
        document.body.style = "overflow-y: hidden;"
        blurScreen.style = "z-index: 2; opacity: 0.7;";
        this.lastElementChild.style = "display: flex;";
        blurScreen.addEventListener("click", () => {blurClickTask(this)});
        blurOn = true;
    }
    
    
}
function blurClickTask(task) {
    task.className = "task";
    document.body.style = "overflow-y: scroll;"
    task.lastElementChild.style = "display: none";
    blurScreen.style = "z-index: 0; opacity: 0;"
    blurOn = false;
}

function blurClickLeaders(leaders_tab) {
    leaders_tab.className = "leaders_tab";
    blurScreen.style = "z-index: 0; opacity: 0;"
    leadersDiaogram.className = "noOpacityDiagram";
    blurOn = false;
}

for (var i = 0; i < tasks.length; i++) {
    tasks[i].addEventListener("click", taskClick);
}

function hideLeadersTab() {
    var leadersTabSubs = this.children;
    for (var i = 0; i < leadersTabSubs.length; i++) {
        leadersTabSubs[i].className += " nonExist";
    }
    this.firstElementChild.className = "leaders_heading";
    this.firstElementChild.textContent = "Развернуть таблицу";
}

function showLeadersTab () {
    var leadersTabSubs = this.children;
    for (var i = 0; i < leadersTabSubs.length; i++) {
        leadersTabSubs[i].className = "leader";
    }
    this.firstElementChild.className = "leaders_heading";
    this.firstElementChild.textContent = "Таблица лидеров";
}

leadersTab.addEventListener("mouseover", hideLeadersTab);
leadersTab.addEventListener("mouseout", showLeadersTab);

socket.emit("user_connected");

socket.on('server_response', (data) => {
    if (data['isFlagValid']) {
        var solvedTask = document.getElementsByClassName(data['taskId'])[0];
        solvedTask.textContent = "1";
        profilePoints.lastElementChild.textContent = "Ваши очки: " + data['points'];
    }

    for (var i = 0; i < tasksWebExtendedParts.length; i++) {
        var editPoint = false;
        for (var j = 0; j < tasksWebExtendedParts[i].children.length; j++) {
            if (tasksWebExtendedParts[i].children[j].textContent == "1") {
                editPoint = true;
            }
        }
        if (editPoint) {
            for (var j = 0; j < tasksWebExtendedParts[i].children.length; j++) {
                tasksWebExtendedParts[i].children[j].style = "display: none;";
            }
            tasksWebExtendedParts[i].lastElementChild.style = "display: block;";
        }
    }
});

socket.on('load_data', (data) => {
    console.log(data);
    if (data.length != 0) {
        console.log(data[0].length);
        for (i = 0; i < data[0].length; i++){
            lineChart.data.labels.push(data[0][i]);
        }
        for (i = 0; i < data[1].length; i++){
            lineChart.data.datasets[0].data.push(data[1][i]);
        }
        for (i = 0; i < data[2].length; i++){
            lineChart.data.datasets[1].data.push(data[2][i]);
        }
        lineChart.update();
    }
    
});


socket.on('gainTeamPoints', (data) => {
    var now = new Date();
    var options = {
        era: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        weekday: 'long',
        timezone: 'UTC',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
      };


    if (now.getMinutes().toLocaleString("ru", options) < 10) {
        time = now.getHours().toLocaleString("ru", options) + ":" + "0" + now.getMinutes().toLocaleString("ru", options);
    }
    else {
        time = now.getHours().toLocaleString("ru", options) + ":" + now.getMinutes().toLocaleString("ru", options);
    }
    lineChart.data.labels.push(time);


    if (data['title'] == "ФМШ и Челики") {
        lineChart.data.datasets[1].data.push(data['points']);
        lineChart.data.datasets[0].data.push(data['otherTeamPoints']);
    }
    else if (data['title'] == "CTF-отдел") {
        lineChart.data.datasets[0].data.push(data['points']);
        lineChart.data.datasets[1].data.push(data['otherTeamPoints']);
    }
    lineChart.update()

    var graphics = {
        'labels': lineChart.data.labels,
        'team1': lineChart.data.datasets[0].data,
        'team2': lineChart.data.datasets[1].data,
    };
    socket.emit('save_graphics', graphics);
    
});

for (var i = 0; i < flag_submit_buttons.length; i++) {

    flag_submit_buttons[i].addEventListener('click', () => {
        var id = event.target.id + "Input";
        var flag_submit_input = document.getElementById(id);
        var data = [ flag_submit_input.value,  event.target.id ];
        socket.emit('client_event', data);
    });
}

function leadersClick() {
    if (blurOn) {
    }
    else {
        leadersDiaogram.className = "leaders_diagram";
        blurScreen.style = "z-index: 2; opacity: 0.7;";
        blurScreen.addEventListener("click", () => {blurClickLeaders(this)});
        blurOn = true;
    }
}

leadersTab.addEventListener("click", leadersClick);

