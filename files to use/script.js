function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA();
/* first it prints Bob, then it prints Sponge because first js does all the synchronic functions then goes to async functions, 
so even though the wait time is 0 seconds, it will still run the synchronic functions before */

// questionB();
/* first it prints Promise at B, then it prints Timeout at B. Because js runs first the microtask queue before the callback queue and promise
is microtask queue so it will run first.*/
// questionC();
/* The output Promise at C, and then Timeout at C. This happens because still the microtask queue executes before callback queue */
// questionD();
/*The output is Sponge, Bob, Pants, Square. Because first it preforms all the sync tasks, then it preforms the Promise task because it is microtask queue,
 then it preforms callback queue  */
questionE();
/*First it preforms all the microtask queues so it executes Promise at B, and then Promise at C. then it preforms all the callback queues.
so Timeout at B, Timeout at C. */