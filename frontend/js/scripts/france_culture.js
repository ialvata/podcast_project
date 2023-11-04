import { episodesList} from "./episodes.js"; // do not remove .js, we need this!

document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.querySelector(".dropbtn");
    const dropdownContainer = document.getElementById("dropdown_content");
    const france_culture_podcasts = [
        { title: "Cultures Monde", text: "cultures monde" },
        { title: "Affaires Étrangères", text: "affaires étrangères" },
        { title: "Entendez-vous l'éco?", text: "entendez-vous l'éco ?" },
        { title: "Concordance des Temps", text: "concordance des temps" },
    ];
    dropdownButton.addEventListener("mouseover", function () {
        dropdownContainer.innerHTML = "";
        // <a href="podcasts/france_culture.html?podcast=cultures%20monde">Cultures Monde</a>
        for ( let podcast of france_culture_podcasts){
            const anchor = document.createElement('a');
            // anchor.href = `france_culture.html`;
            anchor.podcast = podcast.text
            anchor.textContent = podcast.title
            dropdownContainer.appendChild(anchor)
        }
        dropdownContainer.style.display = "block";
    })
    // Hide the menu when the user moves the mouse away from the trigger
    dropdownButton.addEventListener("mouseout", function (event) {
        if(
            !dropdownContainer.contains(event.relatedTarget) 
            // with mouseout event,  event.relatedTarget indicates the element being entered.
        ){
            dropdownContainer.style.display = "none";
        }
    });
    dropdownContainer.addEventListener("mouseout", function (event) {
        if(
            !dropdownButton.contains(event.relatedTarget)&&
            !dropdownContainer.contains(event.relatedTarget)
            // with mouseout event,  event.relatedTarget indicates the element being entered.
        ){
            dropdownContainer.style.display = "none";
        }
    });
    dropdownContainer.addEventListener("click", function (event) {
        episodesList(event.target.podcast)
    });
});
