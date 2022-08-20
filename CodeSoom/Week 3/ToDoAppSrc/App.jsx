import React, { useState } from 'react';

import Page from './Page';

export default function App() {
  const [state, setState] = useState({
    newId: 3,
    newTask: '',
    tasks: [
      { id: 1, title: '아무것도 하지 않기 #1' },
      { id: 2, title: '아무것도 하지 않기 #2' },
    ],
  });

  const { newId, newTask, tasks } = state;

  function handleClickAddTask() {
    setState({
      ...state,
      newId: newId + 1,
      newTask: '',
      tasks: [...tasks, { id: newId, title: newTask }],
    });
  }

  function handleChangeAddTask(event) {
    setState({
      ...state,
      newTask: event.target.value,
    });
  }

  function handleClickDelete(id) {
    setState({
      ...state,
      tasks: tasks.filter((task) => (task.id !== id)),
    });
  }

  return (
    <Page
      newTask={newTask}
      tasks={tasks}
      onClickAddTask={handleClickAddTask}
      onChangeAddTask={handleChangeAddTask}
      onClickDelete={handleClickDelete}
    />
  );
}
