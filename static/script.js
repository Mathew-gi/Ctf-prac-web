var switchIndicator = document.querySelector(".switch_indicator");
var indicatorPlace = "left";

function switchForm () {
    if (indicatorPlace == "left") {
        switchIndicator.style = "margin-left: 2.7vw;";
        indicatorPlace = "right";
    }
    else {
        switchIndicator.style = "margin-left: 0.4vw;";
        indicatorPlace = "left";
    }
    
}
switchIndicator.addEventListener("click", switchForm);