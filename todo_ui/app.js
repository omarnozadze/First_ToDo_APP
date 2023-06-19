const todo_endpoint = "http://localhost:8000/todos/";

async function fetchTodo(){
    const response = await fetch(todo_endpoint);
    const todos = await response.json()

    return todos

}



function renderTodoTemplate(todos){
   return `<div>
   <h1>${todos.title}</h1>
</div>
<p>${todos.description}</p>
<button>${todos.completed ? "Undone":"Done"}</button>
<button >${todos.delete ? "delete":"delete"}</button> 
</li>`;
}



async function main(){
    const todos = await fetchTodo();
    let todoListString = "";

   for (let todo of todos ){
    let renderedTodoTemplateString = renderTodoTemplate(todo)
    todoListString += renderedTodoTemplateString
   }
   document.getElementById("todolist").innerHTML = todoListString;
   
};
     
main();
