function addTask(){
    var taskinput = document.getElementById('taskinput').value;


    var li = document.createElement('li')
    var textNode = document.createTextNode(taskinput)
    li.appendChild(textNode)

    var deletebtn = document.createElement('button')
    deletebtn.innerHTML = 'Delete'
    deletebtn.className = 'deleteBtn'
    li.appendChild(deletebtn,' ')

    var editebtn = document.createElement('button')
    editebtn.innerHTML = 'Edit'
    editebtn.className = 'EditeBtn'
    li.appendChild(editebtn)

    document.getElementById('TaskList').appendChild(li)

    document.getElementById('taskinput').value ="";

    
}
document.getElementById('AddtaskBtn').addEventListener('click',addTask)