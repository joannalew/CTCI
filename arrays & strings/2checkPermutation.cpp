/** CTCI 1.2 Check Permutation
 given two strings, check if one is permutation of other
 assumes strings are 'a - z'
 @param s1 and s2 are strings to check
 @returns true if permutation; false if not **/
bool checkPermutation(string s1, string s2){
    vector<bool> charArray(26, false);
    string s = s1 + s2;
    int index;
    
    for (auto c : s){
        index = c - 'a';
        if (charArray[index])
            charArray[index] = false;
        else
            charArray[index] = true;
    }
    
    for (int i = 0; i < 26; i++){
        if (charArray[i] == true)
            return false;
    }
    return true;
}
