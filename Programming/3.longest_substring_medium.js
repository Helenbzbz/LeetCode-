// Approach one: Brute Force
var lengthOfLongestSubstring1 = function (s) {
    var index = []
    var max = s.length

    if (!s) { return 0 }

    for (let i = 0; i < max; i++) {
        var new_list = []

        for (let c = i; c < max; c++) {
            var char = s[c]
            if (!new_list.includes(char)) {
                new_list.push(char)
            } else { break }

        }
        index.push(new_list.length)
    }
    index.sort((a,b)=>a-b)
    return index.at(-1)

};

console.log(lengthOfLongestSubstring1("nigzhtkqxr"))

//Approach 2. Window Splicing Optimized
var lengthOfLongestSubstring2 = function (s) {
    var index = 0
    var max = s.length
    var new_list = []
    if (max <= 1) { return max }

    for (let i = 0; i < max;i++) {
        
        var char = s[i]
        
        if (!new_list.includes(char)) {
            new_list.push(char)
        } else {
            var new_len = new_list.length
            if(new_len > index){
                var index = new_len
            }
           var new_list = [s[i]] 
        }

    }
    return index
};
console.log(lengthOfLongestSubstring2("au"))