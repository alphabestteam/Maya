const panda_string = " Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages. "

//1.
function splitString(panda_string){
    let splitted_str = panda_string.split(".\n");
    return splitted_str;
}

//2.
function movieToFilm(panda_string){
    let changed_text = panda_string.replace("movie", "film");
    return changed_text;
}

//3.
function allPandaToBear(panda_string){
    let changed_text = panda_string.replaceAll("Panda", "Bear");
    return changed_text;
}

//4.
function convertToUpper(panda_string){
    return panda_string.toUpperCase()
}

//5.
function convertToLower(panda_string){
    return panda_string.toLowerCase()
}

//6.
function findFirstPo(panda_string){
    return panda_string.indexOf("Po")
}

//7.
function startFromPo(panda_string){
    return panda_string.slice(findFirstPo(panda_string))
}

//8.
function without_whitespace(panda_string){
    return panda_string.trim()
}

//9. 
function poToEndPara(panda_string){
    let paragraph = panda_string.substring(findFirstPo(panda_string), panda_string.indexOf(".\n"));
    return paragraph
}

//10.
function arr_from_str(panda_string){
    return panda_string.split(" ")
}

//11.
function ends_with_ages(panda_string){
    return panda_string.endsWith("ages. ")
}

//12.
function add_to_string(panda_string){
    return panda_string + "is one of my favorite movies!"
}
console.log(splitString(panda_string));
console.log(movieToFilm(panda_string));
console.log(allPandaToBear(panda_string));
console.log(convertToUpper(panda_string));
console.log(convertToLower(panda_string));
console.log(findFirstPo(panda_string));
console.log(startFromPo(panda_string));
console.log(without_whitespace(panda_string));
console.log(poToEndPara(panda_string));
console.log(arr_from_str(panda_string));
console.log(ends_with_ages(panda_string));
console.log(add_to_string(panda_string));
