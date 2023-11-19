const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`Spongebob identified a ${jellyfish.color} jellyfish!`);
    identifyJellyfishAndAddPoints(jellyfish, addPoints);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    let species = identifySpecies(jellyfish.color);
    console.log(`Patrick identified a ${species} jellyfish!`);
    addPoints(species);
}

// Score keeping callback function
function addPoints(species) {
    if (speciesPoints[species]){
        score += speciesPoints[species];
    }
    else{
        score += 1;
    }
    console.log(`Score: ${score}`);
}

// Helper functions
function identifySpecies(jellyfish) {
    for (const point in speciesPoints){
        if (point.split(" ")[0] == jellyfish){
            return point;
        }
    }
    return "common";
}

let score = 0;
//The Adventure Starts Here! 
for(const day of jellyfishDays){
    console.log("Let's got jellyfishing!");
    for (const jelly of day){
        catchJellyfish(jelly, identifyJellyfishAndAddPoints);
    }
    console.log(`Great job, SpongeBob and Patrick!\nFinal score: ${score}`);
    score = 0;
}