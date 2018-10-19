/** CTCI 1.4 Palindrome Permutation
 given a string, check if it is a permutation of a palindrome
 @param s is the string to check
 @returns true if is permutation & palindrome; false if not **/

/** returns the character in lower case
    note: should probably just use algorithms library
    @param c is the character to lower 
    @returns the lower case letter **/
char tolower(char c){
    int askey = (int)c;
    
    if (askey >= 65 && askey <= 90){
        askey += 32;
    }
    
    return (char)askey;
}

bool paliperm(string s){
    unordered_map<char, int> map;
    bool one = false;
    
    for (auto& character : s){
        if (character == ' ')
            continue;
        
        if (map.find(character) != map.end())
            map[character]++;
        else{
            pair<char, int> p(character, 1);
            map.insert(p);
        }
    }
    
    for (auto& kv : map){
        if (kv.second % 2 == 1){
            if (one)
                return false;
            one = true;
        }
    }
    
    return true;
}
