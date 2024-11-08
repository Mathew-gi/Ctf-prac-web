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

function checkFlag(trueFlag) {
    if (trueFlag) {
        flag_submit_button.style = "display: none;";
        flag_submit_input.style = "display: none;";
        taskLink.style = "display: none;";
        taskDescription.style = "display: none;";
        trueFlagMsg.style = "display: block;";
    }
}