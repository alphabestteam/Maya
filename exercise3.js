function find_index_sum(target_num, num_arr){
    for (num of num_arr){
        if (num_arr.includes(target_num - num, num_arr.indexOf(num) + 1))
            return [num_arr.indexOf(num), num_arr.indexOf(target_num - num)]
    }
    return []
}

console.log(find_index_sum(10, [5, 10, 15, 21, 25]))
console.log(find_index_sum(30, [5, 10, 15, 21, 25]))