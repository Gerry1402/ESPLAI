function palindrome(str) {
    var letters = /[a-zA-Z]/;
    var numbers = /[0-9]/;
    let string = ''
    for (var i = 0; i < str.length; i++) {
        if (letters.test(str.charAt(i))) {
            string += str.charAt(i).toLowerCase();
        }
        if (numbers.test(str.charAt(i))) {
            string += str.charAt(i);
        }
    }
    console.log(string)
    for (i = 0; i < string.length; i++) {
        if (string.charAt(i)!= string.charAt(string.length - 1 - i)) {
            return false;
        }
    }
    return true;
}

const buttonChecker = document.querySelector("#check-btn");
const inputText = document.querySelector("#text-input");
const result = document.querySelector("#result");
const emoji1 = document.querySelector("#emoji1");
const emoji2 = document.querySelector("#emoji2");
const aparezcom = document.querySelector("#aparezcom");


function checkButton() {
    if (inputText.value === "") {
        alert("Please input a value")
    }
    else {
        aparezco.style.display = "flex";
        if (palindrome(inputText.value)) {
            emoji1.innerText = "\u2714";
            emoji2.innerText = "\u2714";
            result.innerText = inputText.value + " is a palindrome";
        }
        else {
            emoji1.innerText = "\u274C";
            emoji2.innerText = "\u274C";
            result.innerText = inputText.value + " is not a palindrome";
        }
    }
}

buttonChecker.onclick = checkButton