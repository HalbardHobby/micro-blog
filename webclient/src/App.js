import './App.css';
import PostCreate from './PostCreate';

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
    </div>
  );
}
