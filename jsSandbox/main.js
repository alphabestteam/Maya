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
const loremText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at pharetra arcu. Suspendisse potenti. Nulla lectus est, consequat at pretium sed, porta in justo. Nulla nec imperdiet turpis. Mauris semper auctor est sit amet feugiat. Integer euismod sapien in mi bibendum rutrum in vel orci. Nulla eget lectus pulvinar, condimentum metus sed, congue arcu. Nulla commodo non risus eu tristique. Cras in luctus metus. Mauris pulvinar efficitur nulla, sit amet tristique metus vehicula eu. Aliquam tincidunt fermentum dictum. Integer mauris neque, dictum eu est sit amet, tempus pharetra massa. Ut efficitur tincidunt hendrerit. Maecenas porta elit vitae sollicitudin blandit. Maecenas eget egestas dui, eget sollicitudin risus. Proin non tristique leo. In hac habitasse platea dictumst. Ut fermentum purus at elementum feugiat. Phasellus pellentesque ligula sed erat aliquam, et eleifend diam dictum. Pellentesque vitae vestibulum velit, vel interdum mi. Duis ullamcorper iaculis lorem, vitae consectetur diam tincidunt in. Sed pellentesque lacinia risus non feugiat. Curabitur ullamcorper placerat lacus eget euismod. Sed mauris justo, placerat in sodales quis, tristique vitae quam. Nam quis nisl eu turpis rutrum vulputate sit amet rhoncus leo. Curabitur egestas, turpis in placerat tincidunt, lorem ipsum consectetur purus, sed mollis lorem lorem in velit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nisl mi, euismod non massa sed, porta tempus ex. Ut non nisl quis nulla finibus accumsan nec id enim. Suspendisse potenti. Proin facilisis, mi ut viverra convallis, lacus ligula accumsan turpis, non facilisis mauris nisi vitae nunc. Praesent aliquet, velit ut scelerisque aliquet, dui nisi sollicitudin nisl, eu posuere nulla arcu in lacus. Quisque commodo lectus in luctus semper. Vestibulum ornare, lacus a fermentum congue, ante quam egestas nibh, non suscipit elit augue lobortis lectus. Maecenas vitae sem lacus. Morbi mollis augue interdum sapien pharetra auctor. Vivamus in orci rutrum, tempor nunc at, pretium urna. Mauris rhoncus malesuada metus sed volutpat. In finibus congue enim ac cursus. In porttitor, erat et dapibus blandit, ligula velit dictum nulla, mattis aliquam urna enim vitae magna. Etiam id tincidunt arcu. Sed imperdiet libero et dui tincidunt ullamcorper. Sed vulputate, felis ut tincidunt consectetur, velit enim interdum nulla, at blandit ligula ligula sit amet ligula.";
const loremArr = loremText.split(/\s+/);
console.log(loremArr);
const colors = ["red", "orange", "yellow", "greenyellow", "lightblue", "mediumpurple"];

function getRandomColor(){
    return colors[(Math.floor(Math.random() * colors.length))];
}
const randomWords = document.getElementById("random-words");
function changeColor(){
    loremArr.forEach((word) => {
        const span = document.createElement("span");
        const style = "background-color: " + getRandomColor();
        span.setAttribute("style", style);
        span.textContent = word;
        span.className = "random-word";
        randomWords.appendChild(span);
    })
}
changeColor();
const btnLorem = document.createElement("button");
btnLorem.textContent = "click to change color";
document.body.appendChild(btnLorem);

randomColors = () => {return Math.floor(Math.random() * 256)}; 
randomWordClass = document.getElementsByClassName("random-word");

btnLorem.addEventListener("click", function() {
    for (let element of randomWordClass){
        let style = `background-color: rgb(${randomColors()},${randomColors()},${randomColors()})`;
        element.setAttribute("style", style);
    }
});