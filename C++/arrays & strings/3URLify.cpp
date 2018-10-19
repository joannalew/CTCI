/** CTCI 1.3 URLify
 replace spaces in strings with '%20'
 @param s is the string to replace spaces in
 @returns string with spaces replaced with '%20' **/
string urlify(string s){
    int ssize = s.length();
    
    for (int i=0; i < ssize; ++i){
        if (s[i] == ' ')
            s.replace(i, 1, "%20");
    }
    
    return s;
}
