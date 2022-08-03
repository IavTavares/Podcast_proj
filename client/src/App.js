import React, {useState} from 'react';
// import './App.css';

function ListItem(props) {
  // Correct! There is no need to specify the key here:
  return <li>{props.value}</li>;
}

function App() {
  const [podcastList, setPodcastList] = useState(null);
  const headers = { 'Content-Type': 'application/json' };

  fetch('https://localhost:5000/list_podcasts', { headers })
        .then(response => response.json())
        .then(data => console.log(data))
        .then(data => setPodcastList(data.list_podcast))
        .catch(error => console.log(error));
  
  const listItems = podcastList.map((podcast) =>
    // Correct! Key should be specified inside the array.
    <ListItem value = {podcast} />);
  return (
    <div className="Podcast_List">
    <ul>
      {listItems}
    </ul>
    </div>
  );
}

export default App;
