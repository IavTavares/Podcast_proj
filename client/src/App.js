import React, {useState, useEffect} from 'react';
// import './App.css';

function ListItem(props) {
  // Correct! There is no need to specify the key here:
  return <li>{props.value}</li>;
}

async function podcast_list() {
  let podcast_list;
  const headers = { 'Content-Type': 'application/json' };
  const res = await fetch('/list_podcasts', { method: 'GET',headers});
  podcast_list = await res.json();
  console.log(podcast_list);
  return podcast_list
}

function App() {
  // const [podcastList, setPodcastList] = useState(null);
  // const headers = { 'Content-Type': 'application/json' };

  //       .then(data => setPodcastList(data.list_podcast))
  //       .catch(error => console.log(error));

  const podcastList = podcast_list();
  // const listItems = podcastList.map((podcast) =>
  //   // Correct! Key should be specified inside the array.
  //   <ListItem value = {podcast} />);
  return (
    <div className="Podcast_List">
    {/* <p> {podcastList} </p> */}
    </div>
  );
}

export default App;
