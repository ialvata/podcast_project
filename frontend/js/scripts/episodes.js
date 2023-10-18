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