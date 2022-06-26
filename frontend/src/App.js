import React, {
  Component, 
  useEffect,
  useState,
} from 'react'
import { 
  Link,
  BrowserRouter,
  Routes,
  Route, 
  useParams,
} from 'react-router-dom'
import { Markup } from 'interweave'


var API_ROOT = 'http://127.0.0.1:8000';
console.log(API_ROOT);


class App extends Component {
  constructor(props) {
    super(props);
    this.state = { posts: [] };
  }

  render() {
    return (
    <BrowserRouter>
      <Routes>
          <Route path="/" element={<Menu />} />
          <Route path=":slug" element={<Post />} />
      </Routes>
    </BrowserRouter>
    );
  }
}


class Menu extends Component {
  constructor(props) {
      super(props);
      this.state = { posts: [] };
  }

  componentDidMount() {
    fetch(API_ROOT)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        this.setState({ posts: data });
      });
  }

  render() {
    const postlist = this.state.posts.map(post => {
      return (
        <div>
          <li key={post.slug + '_li'}>
            <Link to={`/${post.slug}`} key={post.slug}>{post.title}</Link>
          </li>
        </div>
      )
    });
    return (
      <div className="Menu">
        <h1>Posts</h1>
        <ul>{postlist}</ul>
      </div>
    );
  }
}


function Post() {
    const params = useParams();
    const [post, setPost] = useState({tags: []});

    useEffect(() => {
      fetch(`${API_ROOT}/posts/${params.slug}`)
        .then(response => response.json())
        .then(data => {
          console.log(data.post);
          setPost(data.post);
        })
      }, []
    );

    return (
      <div>
        <h1>{post.title}</h1>
        <Markup content={post.content} />
        <h2>Tags</h2>
        <b>{post.tags.join(", ")}</b>
      </div>
    )
}


export default App
