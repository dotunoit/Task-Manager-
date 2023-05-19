{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53ee7bcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "tasks = []\n",
    "\n",
    "def add_task():\n",
    "    task = input(\"Enter the task: \")\n",
    "    tasks.append(task)\n",
    "    print(\"Task added successfully.\")\n",
    "\n",
    "def view_tasks():\n",
    "    if not tasks:\n",
    "        print(\"No tasks found.\")\n",
    "    else:\n",
    "        print(\"Tasks:\")\n",
    "        for i, task in enumerate(tasks, 1):\n",
    "            print(f\"{i}. {task}\")\n",
    "\n",
    "def delete_task():\n",
    "    view_tasks()\n",
    "    if not tasks:\n",
    "        return\n",
    "    \n",
    "    task_number = int(input(\"Enter the task number to delete: \"))\n",
    "    if task_number < 1 or task_number > len(tasks):\n",
    "        print(\"Invalid task number.\")\n",
    "    else:\n",
    "        deleted_task = tasks.pop(task_number - 1)\n",
    "        print(f\"Task '{deleted_task}' deleted successfully.\")\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        print(\"\\nTask Manager Menu:\")\n",
    "        print(\"1. Add Task\")\n",
    "        print(\"2. View Tasks\")\n",
    "        print(\"3. Delete Task\")\n",
    "        print(\"4. Quit\")\n",
    "\n",
    "        choice = input(\"Enter your choice (1-4): \")\n",
    "        \n",
    "        if choice == \"1\":\n",
    "            add_task()\n",
    "        elif choice == \"2\":\n",
    "            view_tasks()\n",
    "        elif choice == \"3\":\n",
    "            delete_task()\n",
    "        elif choice == \"4\":\n",
    "            print(\"Thank you for using the Task Manager. Goodbye!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
