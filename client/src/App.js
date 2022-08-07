import React, {useEffect, useState} from 'react';

function ListItem(props) {
  return <option value = {props.value}> {props.value} </option>;
}

function App() {
  const [podcastList, setPodcastsList] = useState([]);
  const [EpisodeList, setEpisodeList] = useState([]);
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
        setEpisodeList(data["list_episodes_url"]);
        console.log("episode_list_data: " + data);
        // console.log("podcastList: " + podcastList)
      })
  }
  // episodesList({name:"Cultures Monde"})

  return (
    <div className="Podcast_List">
      <h2>Currently followed Podcasts</h2>  
      {podcastList.length ? (
          <form>
            <select name = "dropdown" id= "" multiple onChange={
                (e) => {
                  // console.log(e);
                  console.log(e.target.value);
                  episodesList(e.target.value)}}>{
              podcastList.map(
                (podcast,index) => {
                  //  {console.log("index: " + index);}
                  //  {console.log("value: " + podcast);}
                  return <ListItem index = {index} value = {podcast} />

                }
              )
            }</select>
            <select name = "dropdown" multiple>{
              EpisodeList.map(
                (episode,index) => {
                  //  {console.log("index: " + index);}
                  //  {console.log("value: " + podcast);}
                  return <ListItem index = {index} value = {episode} />

                }
              )
            }</select>
          </form>
        ):<div> Loading...</div> 
      }
    </div>
  );
}

export default App;
