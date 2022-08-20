import React from 'react';

export default function Item({ task: { id, title }, onClick }) {
  return (
    <li>
      id :
      {' '}
      {id}
      {' '}
      -
      {' '}
      {title}
      <button
        id={id}
        type="button"
        onClick={() => onClick(id)}
      >
        완료
      </button>
    </li>
  );
}
