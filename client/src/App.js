import React, {useEffect, useState} from 'react';

function ListItem(props) {
  return <option value = {props.value}> {props.value} </option>;
}

function App() {
  const [podcastList, setPodcastsList] = useState([]);
  const [EpisodeList, setEpisodeList] = useState([]);
  const [EpisodeListURLs, setEpisodeListURLs] = useState([]);
  // const headers = { 'Content-Type': 'application/json' };

  useEffect(() => {
    fetch("/list_podcasts",{method:"GET",
      headers: {'Content-Type': 'application/json'}
    })
      .then(res => res.json())
      .then((data) => {
        setPodcastsList(data["list_podcast"]);
        // console.log("data: " + data);
        // console.log("podcastList: " + podcastList)
      })
  }, []);
  
  function episodesList(name){
    const body = {"podcast_name": name};
    console.log("body: " + body);
    fetch("/list_episodes",{method:"POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    })
      .then(res => res.json())
      .then((data) => {
        setEpisodeList(data["list_episodes_names"]);
        setEpisodeListURLs(data["list_episodes_url"]);
        // console.log("episode_list_data: " + data);
      })
  }
  // episodesList({name:"Cultures Monde"})

  return (
    <div className="Podcast_List">
      <h2>Currently followed Podcasts</h2>
      <h3>Choose a Podcast to see the available episodes</h3>
      {podcastList.length ? (
          <form action="/download_episodes" method="post">
            <select name = "podcast" id= "podcastList" multiple onChange={
                (e) => {
                  // console.log(e);
                  console.log(e.target.value);
                  episodesList(e.target.value)}}>{
              podcastList.map(
                (podcast,index) => {
                  //  {console.log("index: " + index);}
                  //  {console.log("value: " + podcast);}
                  return <ListItem index = {podcast} value = {podcast} />

                }
              )
            }</select>
            {/* { if (EpisodeList.length){ */}
              <div>
                <h3>Choose the episodes you want to download.</h3>
                <select name = "episodes" id= "EpisodeList" multiple>{
                  EpisodeList.map(
                    (episode,index) => {
                      //  {console.log("index: " + index);}
                      //  {console.log("value: " + podcast);}
                      return <ListItem index = {episode} value = {episode} />

                    }
                  )
                }</select>
                <input type="submit" value="Download"></input>
              </div>
            {/* }} */}
          </form>
        ):<div> Loading...</div> 
      }
    </div>
  );
}

export default App;