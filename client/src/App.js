import React, {useEffect, useState} from 'react';

function ListItem(props) {
  return <option value = {props.value}> {props.value} </option>;
}

function App() {
  const [podcastList, setPodcastsList] = useState([]);
  // const headers = { 'Content-Type': 'application/json' };

  useEffect(() => {
    fetch("/list_podcasts",{method:"GET",
      headers: {'Content-Type': 'application/json'}
    })
      .then(res => res.json())
      .then((data) => {
        setPodcastsList(data["list_podcast"]);
        console.log("data: " + data);
        // console.log("podcastList: " + podcastList)
      })
  }, []);
  

  return (
    <div className="Podcast_List">
      <h2>Currently followed Podcasts</h2>  
      {podcastList.length ? (
          <form>
            <select name = "dropdown">{
              podcastList.map(
                (podcast,index) => {
                  //  {console.log("index: " + index);}
                  //  {console.log("value: " + podcast);}
                  return <ListItem index = {index} value = {podcast} />

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
