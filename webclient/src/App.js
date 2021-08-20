import './App.css';
import PostCreate from './PostCreate';
import PostList from './PostList';

export default () => {
  return (
    <div>
      <header className="App-header">
        <p>
          Blog App
        </p>
      </header>
      <div className="container">
        <h1>Create Post</h1>
        <PostCreate />
      </div>
      <hr />
      <div className="container">
        <h1>Post List</h1>
        <PostList />
      </div>
    </div>
  );
}
