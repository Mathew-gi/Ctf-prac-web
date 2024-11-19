var tasks_difficulties = document.getElementsByClassName("task_difficulty");
var tasks = document.getElementsByClassName("task");
var blurScreen = document.querySelector(".blur");
var blurOn = false;
var tasksLinks = document.getElementsByClassName("task_link");
var flag_submit_button = document.querySelector(".task_flag_submit");
var flag_submit_input = document.querySelector(".task_flag_input");
var trueFlagMsg = document.querySelector(".trueFlagMsg");
var taskLink = document.querySelector(".task_link");
var taskDescription = document.querySelector(".task_description");
var leadersTab = document.querySelector(".leaders_tab");
var trueFlag =document.querySelector(".true_flag");
var tasksWebExtendedParts = document.getElementsByClassName("extended_task_part_web");

for (var i = 0; i < tasksWebExtendedParts.length; i++) {
    console.log(tasksWebExtendedParts[i]);
    var editPoint = false;
    for (var j = 0; j < tasksWebExtendedParts[i].children.length; j++) {
        console.log(tasksWebExtendedParts[i].children[j]);
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
        blurScreen.style = "z-index: 2; opacity: 0.7;";
        this.lastElementChild.style = "display: flex;";
        blurScreen.addEventListener("click", () => {blurClick(this)});
        blurOn = true;
    }
    
    
}
function blurClick(task) {
    task.className = "task"
    blurScreen.style = "z-index: 0; opacity: 0;"
    task.lastElementChild.style = "display: none;";
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

function getLeaders() {
    
}