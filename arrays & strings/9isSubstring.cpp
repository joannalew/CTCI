/** CTCI 1.9 String Rotation
 check if a string is a rotation of another
 @param s1 and s2 are strings to check
 @retuns true if strings are the same but rotated; else, false **/
bool isSubstring(string s1, string s2){
    s1 = s1 + s1;
    if (s1.find(s2) != string::npos){
        return true;
    }
    return false;
}
