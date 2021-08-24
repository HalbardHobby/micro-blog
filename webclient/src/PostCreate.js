import React, { useState } from 'react';
import axios from 'axios'

export default () => {
  const [title, setTitle] = useState('');
  const handleSubmit = async (event) => {
    event.preventDefault();
    await axios.post('http://posts.com/posts/', {
      title
    });

    setTitle('');
  };

  return <div>
    <form onSubmit={handleSubmit}>
      <div className="form-groups">
        <label>Title</label>
        <input
          value={title}
          onChange={e => setTitle(e.target.value)}
          className="form-control"
        />
        <button className="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
};