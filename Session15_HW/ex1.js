let $ulElement = document.querySelector('ul');

$ulElement.addEventListener("click", (event) => {
    let $target = event.target;
    if($target.classList.contains('close')){
        let $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
        deleteTodoList('todoList', $parentTarget.firstChild.innerText);
    }
    $target.classList.toggle('checked');
})

function newElement() {


    // let $liElement = document.createElement("li");

    // let $textElement = document.createElement("span");
    // let inputValue = document.getElementById("myInput").value;
    // $textElement.innerText = inputValue;

    // let $closeElement = document.createElement("span");
    // let $closeText = document.createTextNode("\u00D7");
    // $closeElement.className = "close";
    // $closeElement.appendChild($closeText);

    // $liElement.appendChild($textElement);
    // $liElement.appendChild($closeElement);

    const inputValue = document.getElementById("myInput").value;
    const $liElement = `
    <li>
        <span>${inputValue}</span>
        <span class="close">&#215;</span>
    </li>
    `
    if (inputValue === ''){
        alert("You must write something!");
    }
    else {
        $ulElement.insertAdjacentHTML('beforeend', $liElement);
        addTodoList('todoList', inputValue);
    }
    document.getElementById("myInput").value = "";
}

// 두번째 실습

function init() {
    let todoArray = getTodoList('todoList');
    for (let i = 0; i < todoArray.length; i++){
        const liElement = `
        <li>
            <span>${todoArray[i]}</span>
            <span class="close">&#215;</span>
        </li>
        `
        $ulElement.insertAdjacentHTML('beforeend', liElement);
    }
}

function getTodoList(key) {
    let data = localStorage.getItem(key);
    if (data){
        return data.split(',');
    }
    return [];
}

function addTodoList(key, value) {
    let todoArray = getTodoList(key);
    todoArray.push(value);
    localStorage.setItem(key, todoArray);
}

function deleteTodoList(key,value) {
    let todoArray = getTodoList(key);
    todoArray.splice(todoArray.indexOf(value), 1);
    localStorage.setItem(key, todoArray);
}

init()

var modal = document.getElementById('myModal');
var btn = document.getElementById('myBtn');
var cls = document.getElementsByClassName('cls')[0];
var header = document.getElementsByClassName('header')[0];
var color = document.getElementById('color');

btn.addEventListener("click", () => {
    modal.style.display = "block";
})

cls.addEventListener("click", () => {
    modal.style.display = "none";
})

color.addEventListener("click", () => {
    header.classList.toggle('blue');
})

