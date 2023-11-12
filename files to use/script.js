function addEvent() {
    counter = parseInt(document.getElementById("counter-display").textContent);
    return function () {counter += 1; 
        document.getElementById("counter-display").textContent = counter;
        return counter;
    };
}

document.addEventListener("click", addEvent());
