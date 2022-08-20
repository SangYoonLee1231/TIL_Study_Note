import React from 'react';

import Input from './Input';
import List from './List';

export default function Page({
  newTask, onChangeAddTask, tasks,
  onClickAddTask, onClickDelete,
}) {
  return (
    <div>
      <h1>To-do</h1>
      <Input
        value={newTask}
        onChange={onChangeAddTask}
        onClick={onClickAddTask}
      />
      <List
        tasks={tasks}
        onClick={onClickDelete}
      />
    </div>
  );
}
