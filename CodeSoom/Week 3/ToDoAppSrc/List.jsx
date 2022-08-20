import React from 'react';

import Item from './Item';

export default function List({ tasks, onClick }) {
  return (
    <ol>
      {tasks.map((task) => (
        <Item key={task.id} task={task} onClick={onClick} />
      ))}
    </ol>
  );
}
