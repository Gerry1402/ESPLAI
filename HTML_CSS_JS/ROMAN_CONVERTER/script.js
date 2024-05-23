function convertToRoman(num) {
    const conversions={
        1000:'M',
        900:'CM',
        500:'D',
        400:'CD',
        100:'C',
        90:'XC',
        50:'L',
        40:'XL',
        10:'X',
        9:'IX',
        5:'V',
        4:'IV',
        1:'I',
    };
    if (num<1){
        return "Please enter a number greater than or equal to 1";
    }
    if (num>3999){
        return "Please enter a number less than or equal to 3999";
    }
    let result=''
    for (const number of Object.keys(conversions).reverse()) {
        while (num>=number){
            result+=conversions[number];
            num-=number;
        };
    
    }
    return result;
}

const buttonChecker = document.querySelector("#convert-btn");
const number = document.querySelector("#number");
const output = document.querySelector("#output");
const emoji1 = document.querySelector("#emoji1");
const emoji2 = document.querySelector("#emoji2");
const aparezco = document.querySelector("#aparezco");


function checkButton() {
    aparezco.style.display = "flex";
    output.innerText = convertToRoman(Number(number.value));
    if (output.innerText === "" || number.value === "") {
        emoji1.innerText = "\u274C";
        emoji2.innerText = "\u274C";
        output.innerText = "Please enter a valid number";
    }
    else if (output.innerText === "Please enter a number greater than or equal to 1") {
        emoji1.innerText = "\u274C";
        emoji2.innerText = "\u274C";
    }
    else if (output.innerText === "Please enter a number less than or equal to 3999") {
        emoji1.innerText = "\u274C";
        emoji2.innerText = "\u274C";
    }
    else {
        emoji1.innerText = "\u2714";
        emoji2.innerText = "\u2714";
    }
}

buttonChecker.onclick = checkButton;