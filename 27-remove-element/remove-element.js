/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let index = 0;
    let count = 0
    while (index < nums.length){
        if (nums[index] === val){
            nums.splice(index,1)
        } else{
            index++
            count++
        }
    }
    return count
};