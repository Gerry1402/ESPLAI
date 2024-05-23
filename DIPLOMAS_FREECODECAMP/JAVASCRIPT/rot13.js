const abecedary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

function rot13(str) {
    let string='';
    for (var i=0; i<str.length; i++){
        console.log(str[i], abecedary.indexOf(str[i]), abecedary.includes(str[i]));
        if (abecedary.includes(str[i])){
            if (abecedary.indexOf(str[i])+13 > 25){
                string += abecedary[abecedary.indexOf(str[i])+13-26];
            }
            else{
                string += abecedary[abecedary.indexOf(str[i])+13];
            }
        }
        else{
            string += str[i];
        }
    }
    return string;
  }
  
  console.log(rot13("SERR PBQR PNZC"));