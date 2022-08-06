import React, {useEffect, useState} from 'react';


function ListItem(props) {
  return <li>{props.value}</li>;
}


function App() {
  const [podcastList, setPodcastsList] = useState(0);
  const headers = { 'Content-Type': 'application/json' };
  useEffect(() => {
    fetch("/list_podcasts", {method: 'GET',headers})
      .then(res => res.json())
      .then(data => {
        setPodcastsList(data);
        console.log(podcastList)
      });
  }, []);

  console.log("2nd print:"+Promise.resolve(podcastList))
  return (
    <div className="Podcast_List">
      <h2>Current followed Podcasts</h2>  
      {podcastList.length ? (
          <ul>{
            podcastList.map(
              (podcast) =>
              <ListItem value = {podcast} />
            )
          }</ul>
        ):<div> Loading...</div> 
      }
    </div>
  );
}

export default App;
