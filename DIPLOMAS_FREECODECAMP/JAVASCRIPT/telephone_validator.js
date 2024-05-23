function telephoneCheck(numero) {
    var regex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;
    if (!regex.test(numero)) {
        return false;
    }
    return true;
}
  
console.log(telephoneCheck("1 (555)555-5555"));