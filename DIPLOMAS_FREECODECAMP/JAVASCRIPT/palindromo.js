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
  
console.log(palindrome("enoye"));