const btnEl = document.getElementById("btn");
const jokeEl = document.getElementById("joke");


function getJoke() {
    jokeEl.innerText = "clicked !! & get the joke from api";
    console.log("clicked");
}

btnEl.addEventListener("click", getJoke)