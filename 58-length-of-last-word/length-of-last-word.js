/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const words =  s.split(" ")
    console.log(words)
    for (let i = words.length - 1; i >= 0; i--){
        const word = words[i]
        console.log("word", word)
        if (!word){
            continue
        } else{
            console.log("here's the word returned", word )
            return word.length
        }

    }
    // return (words[words.length-1]).length
};