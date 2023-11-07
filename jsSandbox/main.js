const mainHeading = document.getElementById('main-heading');
console.log(mainHeading.id);
console.log(mainHeading.className);
console.log(mainHeading.classList);
console.log(mainHeading.dataset);
console.log(mainHeading.getAttribute("nonStandard"));
mainHeading.classList.add("border");
mainHeading.classList.add("bg-lightcyan");
console.log(mainHeading.textContent);
console.log(mainHeading.textContent.trim());
mainHeading.textContent = "Hello there pearl!";
mainHeading.innerHTML += `<br><span>its me SpongeBob<span>`;
console.log(mainHeading);
const cloned = mainHeading.cloneNode(true);
console.log(cloned);
const subheading = document.createElement("h2");
subheading.textContent = "jellyfish hunting is the best";
document.body.appendChild(subheading);
const loremText = document.getElementsByTagName("p")[1].innerText;
const loremArr = loremText.split(/\s+/);
console.log(loremArr);
const colors = ["red", "orange", "yellow", "greenyellow", "lightblue", "mediumpurple"];

function getRandomColor(){
    return colors[(Math.floor(Math.random() * colors.length))];
}
const randomWords = document.getElementById("random-words");
loremArr.forEach((word) => {
    const span = document.createElement("span");
    const style = "background-color: " + getRandomColor();
    span.setAttribute("style", style);
    span.textContent = word;
    span.className = "random-word";
    randomWords.appendChild(span)
})
