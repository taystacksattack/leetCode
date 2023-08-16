/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let [l,r] = [0, numbers.length - 1]

    while (l<r){
        const sum = numbers[l] + numbers[r]

        if (sum===target) return [l+1, r+1]
        if (target < sum) r--
        if (target > sum) l++
    }
    return -1
};