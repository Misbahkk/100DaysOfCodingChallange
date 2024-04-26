function clearScreen(){
    document.getElementById('result').value ="";
}

function display(value){
    document.getElementById('result').value += value;
}
function calculate(){
    var q = document.getElementById('result').value;
    var p = eval(q);
    document.getElementById('result').value = p;
}