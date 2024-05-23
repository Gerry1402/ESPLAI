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
}
function convertToRoman(num) {
    let result=''
    for (const number of Object.keys(conversions).reverse()) {
        while (num>=number){
            result+=conversions[number]
            num-=number
        }
    }
    return result;
   }
   
console.log(convertToRoman(97));