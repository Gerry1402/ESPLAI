function telephoneCheck(numero) {
    var regex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;
    return regex.test(numero)
}

const buttonChecker = document.querySelector("#check-btn");
const buttonClear = document.querySelector("#clear-btn");
const telephone = document.querySelector("#user-input");
const result = document.querySelector("#results-div");
const emoji1 = document.querySelector("#emoji1");
const emoji2 = document.querySelector("#emoji2");
const aparezco = document.querySelector("#aparezco");


function checkButton() {
    aparezco.style.display = "flex";
    if (telephone.value === "") {
        emoji1.innerText = "\u274C";
        emoji2.innerText = "\u274C";
        result.innerText = "...";
        alert("Please provide a phone number")
    }
    else {
        if (telephoneCheck(telephone.value)) {
            emoji1.innerText = "\u2705";
            emoji2.innerText = "\u2705";
            result.innerText = "Valid US number: "+telephone.value;
        }
        else {
            emoji1.innerText = "\u274C";
            emoji2.innerText = "\u274C";
            result.innerText = "Invalid US number: "+telephone.value;
        }
    }
}

function clearButton() {
    telephone.value = "";
    aparezco.style.display = "none";
    result.innerText = "";
}

buttonChecker.onclick = checkButton;

buttonClear.onclick = clearButton;