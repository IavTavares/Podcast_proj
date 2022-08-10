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
        let names = data["list_episodes_names"];
        let urls = data["list_episodes_url"];
        let EpisodeListTuples = [];
        for (let i=0; i < urls.length; i++) {
          var tuple = [names[i], urls[i]];
          EpisodeListTuples.push(tuple);
        }
        setEpisodeList(EpisodeListTuples);
        // setEpisodeListURLs(data["list_episodes_url"]);
        // console.log("episode_list_data: " + data);
      })
  }
 
  
  function downloadMP3(){
    const body = {"episodes_url_list": EpisodeListURLs};
    console.log("body: " + body);
    fetch("/download_episodes",{method:"POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    })
      .then(res => res.json())
      .then((response)=> {
        if (response['success']){
          alert("Download was a success. See files " + response["list_episodes_names"] + "on folder " + response["podcast_name"] );
        }else{
          alert("There was a problem with the download.");
        }
        

      })
  }

  return (
    <div className="Podcast_List">
      <h2>Currently followed Podcasts</h2>
      <h3>Choose a Podcast to see the available episodes</h3>
      {podcastList.length ? (
          <form >
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
                <select name = "episodes" id= "EpisodeList" multiple onChange={
                (e) => {
                  // console.log(e);
                  console.log(e.target.selectedOptions);
                  
                  let url_list =[];
                  for (let episode_tuple of EpisodeList) {
                    let selected_episode_names = e.target.selectedOptions;
                    for (let episode of selected_episode_names){
                      if (episode.value == episode_tuple[0]){
                        url_list.push(episode_tuple[1])
                      }
                    }
                  }
                  setEpisodeListURLs(url_list);
                  for (let i=0; i < url_list.length; i++){
                    console.log("EpisodeListURLs["+i+"]"+ EpisodeListURLs[i]);
                  }
                }}>{
                  EpisodeList.map(
                    (episode_tuple) => {
                      //  {console.log("index: " + index);}
                      //  {console.log("value: " + podcast);}
                      return <ListItem index = {episode_tuple[1]} value = {episode_tuple[0]} />

                    }
                  )
                }</select>
                <button onClick={downloadMP3} type="button"> Download MP3s</button>
              </div>
            {/* }} */}
          </form>
        ):<div> Loading...</div> 
      }
    </div>
  );
}

export default App;