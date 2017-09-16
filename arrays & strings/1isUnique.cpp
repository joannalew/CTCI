/** CTCI 1.1 Is Unique
 check if characters in a string is unique
 @parma s is the string to check
 @returns true if string is unique; false if not unique **/
bool is_unique(string s){
    unordered_set<char> set = {};
    
    for (auto character : s){
        if (set.find(character) != set.end())
            return false;
        set.insert(character);
    }
    
    return true;
}
