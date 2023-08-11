/**
 * @param {string} s
 * @return {number}
 */
// var lengthOfLastWord = function(s) {
//     const words =  s.split(" ")
//     for (let i = words.length - 1; i >= 0; i--){
//         const word = words[i]
//         console.log("word", word)
//         if (!word){
//             continue
//         } else{
//             return word.length
//         }

//     }
//     // return (words[words.length-1]).length
// };


// var lengthOfLastWord = function(s) {
//     let count = 0
//     // let words = s.split("")
//     for (let i = s.length - 1; i >= 0; i--){
//         let char = s[i]
//         let next = s[i-1]
//         // console.log(char)
//         if (char === " ") continue
//         count++
//         if (next === " ") break
//     }
//     return count
// }

var lengthOfLastWord = function(s) {
    let trimmed = s.trim()
    // console.log(trimmed)
    // console.log("here is that space", trimmed[trimmed.lastIndexOf(' ')])
    // return (trimmed.slice(trimmed[trimmed.lastIndexOf(' ')])).length
    if (trimmed.includes(' ')){
        return (trimmed.slice(trimmed.lastIndexOf(' '))).length -1
    }
    return trimmed.length
}