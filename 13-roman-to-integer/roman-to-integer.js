/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
 
    //  declare result sum
    let result = 0
    //  loop over the string
    for (let i = 0; i < s.length; i++){
        //  create special conditions for if I is before V or X
        if ((s[i] === "I")){
            if (s[i+1] === "V" || s[i+1] === "X") result -= 1
            else result +=1
        }
        else if (s[i]==="V") result += 5
        else if ((s[i] === "X")){
            if (s[i+1] === "L" || s[i+1] === "C") result -= 10
            else result += 10
        }
        else if (s[i]==="L") result += 50
        else if ((s[i] === "C")){
            if (s[i+1] === "D" || s[i+1] === "M") result -= 100
            else result += 100
        }
        else if (s[i]==="D") result += 500
        else result += 1000
    }
    return result
};