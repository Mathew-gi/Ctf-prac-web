var switchIndicator = document.querySelector(".switch_indicator");
var indicatorPlace = "";
var form = document.querySelector(".reg_auth_form");
var greeting_label = document.querySelector(".greeting_h3");
var form_button = document.querySelector(".submit");
var statusQ = document.querySelector(".status");
var nameInput = document.querySelector(".name");
var passwordInput = document.querySelector(".password");


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
        nameInput.value = "";
        passwordInput.value = "";
    }
    else {
        switchIndicator.style = "margin-left: 0.4vw;";
        indicatorPlace = "left";
        greeting_label.textContent = "введите данные для регистрации"
        form.action = "/registration";
        form_button.textContent = "Зарегистрироваться";
        nameInput.value = "";
        passwordInput.value = "";
    }
    
}
switchIndicator.addEventListener("click", switchForm);