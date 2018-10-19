/** CTCI 1.5 One Away
 check if two strings are at most one edit away (insert, delete, replace)
 @param s1 and s2 are strings to check **/
bool one_away_replace(string s1, string s2){
    size_t ssize = s1.length();
    bool one = false;
    
    for (int i = 0; i < ssize; i++){
        if (s1[i] != s2[i]){
            if (one)
                return false;
            else
                one = true;
        }
    }
    
    return true;
}

bool one_away_insert(string s1, string s2){
    int idx1 = 0;
    int idx2 = 0;
    size_t ssize = s1.length();
    bool one = false;
    
    for (int i = 0; i < ssize; i++){
        if (s1[idx1] != s2[idx2]){
            if (one)
                return false;
            else{
                one = true;
                idx2++;
                i--;
            }
        }
    }
    
    return true;
}


bool one_away(string s1, string s2){
    size_t s1size = s1.length();
    size_t s2size = s2.length();
    if (s1size == s2size){
        return one_away_replace(s1, s2);
    }
    else if (s1size + 1 == s2size){
        return one_away_insert(s1, s2);
    }
    else if (s2size + 1 == s1size){
        return one_away_insert(s2, s1);
    }
    
    return false;
}
