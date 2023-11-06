export function test_alert() {
  alert('Button clicked!');
}

function downloadEpisode(episode_title,url_audio){
  var requestOptions = {
    method: 'POST',
  };
  var url = encodeURI(
    `http://localhost:8001/episodes/download?url_audio=${url_audio}&episode_title=${episode_title}`
  )
  alert(`Starting Download of Episode -> ${episode_title}`)
  fetch(url, requestOptions)
  .then(response => response.text())
  .then(response => {
    if (response==200) {
      alert(`The download has finished with code 200`);
    } else {
      alert(`Something unexpected has happened! Check the logs.`);
    }})
  .catch(error => console.log('error', error));
}
export function episodesList(podcast_title){
  try {
    const gallery = document.getElementById('gallery');
    // const podcast_title = gallery.getAttribute("podcast");
    gallery.innerHTML = ''; // clean gallery
    var requestOptions = {
      method: 'POST',
    };
    console.log('podcast_title -> ', podcast_title)
    var url = encodeURI(`http://localhost:8001/episodes?podcast_title=${podcast_title}`)
    // var url_all = `http://localhost:8001/episodes?`
    fetch(url, requestOptions)
    .then(response => response.json())
    .then((episodes_list) => {
      episodes_list.forEach((episode) => {
          // creating card
          const card = document.createElement('div');
          card.className = "card";
          // Creating a title
          const title = document.createElement('h2');
          title.textContent = episode["title"];
          title.className = "title";
          // Creating a description
          const paragraph = document.createElement('p');
          paragraph.textContent = `Description: ${episode["description"]}`;
          paragraph.className = "description"
          // Creating a download button
          const button = document.createElement('button');
          button.textContent = "Download"
          button.className = "btn fa fa-download"
          button.addEventListener('click', 
          (event)=>{downloadEpisode(`${episode["title"]}.mp3`,episode["url_audio"])}
          )
          // button.addEventListener(type = "click")
          // Append the title and paragraph to the card
          card.appendChild(title);
          card.appendChild(paragraph);
          card.appendChild(button);
          gallery.appendChild(card);
      });
    })} catch (error) {
      // Log the error
      console.error("Error:", error);
  }
}

// episodesList();