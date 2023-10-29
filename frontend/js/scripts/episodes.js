function episodesList(){
  try {
    const gallery = document.getElementById('gallery');
    const podcast_title = gallery.getAttribute("podcast");
    const body = {"podcast_title": podcast_title};
    console.log("body: " + body);
    fetch("/episodes",{method:"POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    })
    .then(res => res.json())
    .then((episodes_list) => {
      episodes_list.forEach((episode) => {
          // creating card
          const card = document.createElement('div');
          card.className = "card dark-background";
          // Creating a title
          const title = document.createElement('h2');
          title.textContent = `Title: ${episode["title"]}`;
          // Creating a description
          const paragraph = document.createElement('p');
          paragraph.textContent = `Description${episode["title"]}`;
          // Append the title and paragraph to the card
          card.appendChild(title);
          card.appendChild(paragraph);
          gallery.appendChild(card);
      });
    })} catch (error) {
      // Log the error
      console.error("Error:", error);
  }
}

episodesList();