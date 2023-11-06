const is_sufficient_fuel = (distance, liter_per_km, fuel_left) =>{
    let liter_needed = distance * liter_per_km
    return liter_needed < fuel_left
}

console.log(is_sufficient_fuel(10, 3, 200))
console.log(is_sufficient_fuel(10, 3, 2))