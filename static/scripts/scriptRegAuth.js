var switchIndicator = document.querySelector(".switch_indicator");
var indicatorPlace = "";
var form = document.querySelector(".reg_auth_form");
var greeting_label = document.querySelector(".greeting_h3");
var form_button = document.querySelector(".submit");
var statusQ = document.querySelector(".status");


if (statusQ.textContent == "Registration") {
    indicatorPlace = "right";
    switchForm();
}
else if (statusQ.textContent == "Authorization"){
    indicatorPlace = "left";
    switchForm();
}

function switchForm () {
    console.log(indicatorPlace);
    if (indicatorPlace == "left") {
        switchIndicator.style = "margin-left: 2.7vw;";
        indicatorPlace = "right";
        greeting_label.textContent = "введите данные для авторизации"
        form.action = "/authorization";
        form_button.textContent = "Войти";
    }
    else {
        switchIndicator.style = "margin-left: 0.4vw;";
        indicatorPlace = "left";
        greeting_label.textContent = "введите данные для регистрации"
        form.action = "/registration";
        form_button.textContent = "Зарегистрироваться";
    }
    
}
switchIndicator.addEventListener("click", switchForm);