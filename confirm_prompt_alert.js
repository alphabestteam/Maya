/*-------JAVASCRIPT EXERCISE 1--------
a. alert:
alert() is a popup window when you do something that activates the alert() method.
so for example if you click on a button and the button function has alert method in it, when you click on it a
box is going to popup with a message on it.
prompt:
prompt() is very similar to alert, it also activates a popup box. However the difference is that the popup box it opens, 
has a place for the user to add an input. so for example when a prompt() method is activated, a popup box opens with an option to write a message (such as name or anything)
and the function gets the user's input and performs a certain action with it(so for example writing back a message that includes the user's input).
confirm:
a confirm() method also opens a popup box, but with the options of buttons cancel and OK. so the user can choose which button to click and it will act accordingly.
Mostly we use confirm() for validation or asking the user to accept or decline something.*/


function process_start(){
    document.body.addEventListener("load", alert_bob());
}

process_start();
//b.

function alert_bob(){
    alert("OMG BOBBB!! Patrick got lost! You have to find himmmmmm fastttttt!!!!!!!");
    is_bob_going()
}

//c.
function is_bob_going(){ 
    let answer = prompt("Dear Bob, are you going to look for you dear friend Patrick? (pleasee write yes)");
    if (answer =="yes")
        announce_hooray()
    else
        process_start()
}

//d.
function announce_hooray(){
    alert("HOORAYYYY! You are going to find Patrick! How wonderful!");
    was_patrick_found()
}

//e.
function was_patrick_found(){
    let answer = prompt("Was Patrick found?");
    if (answer == "yes")
        patrick_was_found()
    else
        process_start()

}

function patrick_was_found(){
    alert("Bob found Patrickkk!!! Great Great Great");
}

