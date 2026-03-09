const API = "http://127.0.0.1:8000/tasks";

async function loadTasks(){

const res = await fetch(API);
const tasks = await res.json();

const list = document.getElementById("taskList");
list.innerHTML = "";

tasks.forEach(task => {

const li = document.createElement("li");

li.innerHTML = `
<span class="task-title ${task.completed ? "completed" : ""}">
${task.title}
</span>

<div class="actions">
<button class="done" onclick="completeTask(${task.id})">Done</button>
<button class="delete" onclick="deleteTask(${task.id})">Delete</button>
</div>
`;

list.appendChild(li);

});

}

async function addTask(){

const input = document.getElementById("taskInput");

if(input.value.trim() === "") return;

await fetch(API,{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify(input.value)
});

input.value="";
loadTasks();
}

async function deleteTask(id){

await fetch(`${API}/${id}`,{
method:"DELETE"
});

loadTasks();
}

async function completeTask(id){

await fetch(`${API}/${id}`,{
method:"PUT"
});

loadTasks();
}

loadTasks();