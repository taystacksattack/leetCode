/**
 * @param {string} s
 * @return {number}
 */
// var romanToInt = function(s) {
 
//     //  declare result sum
//     let result = 0
//     //  loop over the string
//     for (let i = 0; i < s.length; i++){
//         //  create special conditions for if I is before V or X
//         if ((s[i] === "I")){
//             if (s[i+1] === "V" || s[i+1] === "X") result -= 1
//             else result +=1
//         }
//         else if (s[i]==="V") result += 5
//         else if ((s[i] === "X")){
//             if (s[i+1] === "L" || s[i+1] === "C") result -= 10
//             else result += 10
//         }
//         else if (s[i]==="L") result += 50
//         else if ((s[i] === "C")){
//             if (s[i+1] === "D" || s[i+1] === "M") result -= 100
//             else result += 100
//         }
//         else if (s[i]==="D") result += 500
//         else result += 1000
//     }
//     return result
// };

var romanToInt = function(s) {
    var roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    var result = 0;
    for (var i = 0; i < s.length; i++) {
        if (roman[s[i]] < roman[s[i + 1]])
            result = result - roman[s[i]];
        else
            result = result + roman[s[i]];
    }
return result;

};