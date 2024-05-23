const coin_value = {
    "ONE HUNDRED":100,
    "TWENTY":20.0,
    "TEN":10.0,
    "FIVE":5.0,
    "ONE":1.0,
    "QUARTER":0.25,
    "DIME":0.1,
    "NICKEL":0.05,
    "PENNY":0.01
    }
  function add(a, b, precision) {
    var multiplier = Math.pow(10, precision || 0);
    return Math.round((a + b) * multiplier) / multiplier;
  }
  function rest(a, b, precision) {
    var multiplier = Math.pow(10, precision || 0);
    return Math.round((a - b) * multiplier) / multiplier;
  }
function checkCashRegister(price, cash, cid) {
    if (cid[0][0]==="ONE HUNDRED"){
        cid.reverse();
    }
    let change = rest(cash, price, 2);
    let result = {'status': "INSUFFICIENT_FUNDS", 'change':[]};
    let total_amount = 0;
    for (const coin_type of cid.reverse()){
        let [coin, total] = coin_type;
        total_amount = total_amount + total;
        let amount = Math.round(total/coin_value[coin]);
        // console.log(change/coin_value[coin], amount)
        if (change/coin_value[coin]>=1 && amount>0){
            let add_coin_type = [coin,0];
            // console.log(change/coin_value[coin], amount)
            while (change/coin_value[coin]>=1 && amount>0){
                // console.log(change, coin_value[coin], amount)
                add_coin_type[1] = add(add_coin_type[1], coin_value[coin], 2);
                change = rest(change, coin_value[coin], 2);
                amount--;
            }
            result['change'].push(add_coin_type);
        }
        // console.log(total_amount, rest(cash, price, 2));
        if (change == 0){
            result['status'] = "OPEN";
            if (total_amount == cash - price){
                result['status'] = "CLOSED";
                result['change'] = cid.reverse();
            }
            return result
        }
    }
    result['change']=[]
    return result
}

const buttonPurchase = document.querySelector("#purchase-btn");
const buttonClear = document.querySelector("#clear-btn");
const cash = document.querySelector("#cash");
const priceText = document.querySelector("#price");
const changeDue = document.querySelector("#change-due");
const emoji1 = document.querySelector("#emoji1");
const emoji2 = document.querySelector("#emoji2");
const aparezco = document.querySelector("#aparezco");
const avalaible = document.querySelector("#avalaible");
const change = document.querySelector("#change");
const statusText = document.querySelector("#StatusText");
const changedue = document.querySelector("#change-due");

let price = 1.87;
let cid = [
  ["PENNY", 1.03],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100]
];

for (let i = 0; i < cid.length; i++){
    avalaible.innerHTML += "<div class = coinAvailable>" + cid[i][0] + ": $" + cid[i][1] +"</div>"+"\n";
}
priceText.innerText = "TOTAL:\n$"+price

function purchase() {
    change.innerHTML = ""
    if (cash.value == ""){
        alert('Insert the cash of the customer in "CASH CUSTOMER"')
    }
    else if (Number(cash.value)<price){
        alert("Customer does not have enough money to purchase the item")
    }
    else{
        let result = checkCashRegister(price, Number(cash.value), cid);
        statusText.innerText = result["status"];
        changedue.innerText = "Status: " + result["status"];
        let columns;
        let rows;
        if (result["change"].length === 3) {
            columns = "1fr 1fr 1fr";
            rows = "1fr";
        }
        else if (result["change"].length === 4) {
            columns = "1fr 1fr";
            rows = "1fr 1fr";
        }
        else if (result["change"].length === 5 || result["change"].length === 6) {
            columns = "1fr 1fr 1fr";
            rows = "1fr 1fr";
        }
        else if (result["change"].length >= 7) {
            columns = "1fr 1fr 1fr";
            rows = "1fr 1fr 1fr";
        }
        else {
            columns = "1fr";
            rows = "1fr";
            if (result["status"] === "OPEN" && result["change"].length === 0){
                changedue.innerText = "No change due - customer paid with exact cash";
            }
        }
        change.style.display = "grid";
        change.style.gridTemplateColumns = columns;
        change.style.gridTemplateRows = rows;
        for (let i = 0; i < result["change"].length; i++){
            // console.log(result["change"][i][0], result["change"][i][1])
            change.innerHTML += "<div class = coinChange>" + result["change"][i][0] + ": $" + result["change"][i][1] +"</div>"+"\n";
            changedue.innerText += " " + result["change"][i][0] + ": $" + result["change"][i][1]
        }
    }
    changedue.style.display = "None"
}


function clearButton() {
    cash.value = "";
    change.innerHTML = "";
    statusText.innerText = "OPEN";
}

buttonPurchase.onclick = purchase;

buttonClear.onclick = clearButton;