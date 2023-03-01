from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class TodoItem(BaseModel):
    title: str
    description: str


todo_list = []


@app.post("/todos/")
async def create_todo_item(todo_item: TodoItem):
    todo_list.append(todo_item)
    return {"message": "Todo item created successfully."}


@app.get("/todos/")
async def get_todo_list():
    return todo_list


@app.get("/todos/{item_id}")
async def get_todo_item(item_id: int):
    try:
        return todo_list[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo item not found.")


@app.delete("/todos/{item_id}")
async def del_todo_item(item_id: int):
    try:
        del todo_list[item_id]
        return {"message": "Todo item deleted successfully."}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo item not found.")