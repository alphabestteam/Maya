const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function(){
    if (bobGif.style.display === "none"){
        bobGif.setAttribute("style", "display:block");
        button.textContent = "Hide Bob;)";
    }
    else{
    button.textContent = "Show me Bob;)";
    bobGif.setAttribute("style", "display:none");
    }
};

button.textContent = "Show me Bob;)";
bobGif.setAttribute("style", "display:none");

button.onclick = toggleBob;