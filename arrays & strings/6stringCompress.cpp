/** CTCI 1.6 String Compression
 compress string using counts of repeated characters
 @param s is the string to compress
 @returns compressed string if length is shorter; else, s **/
string stringCompress(string s){
    size_t ssize = s.length();
    string res = "";
    
    if (ssize > 0){
        res += s[0];
        int count = 1;
        
        for (int i = 0; i < ssize - 1; i++){
            if (s[i] == s[i+1]){
                count++;
            }
            else{
                res += to_string(count);
                res += s[i+1];
                count = 1;
            }
        }
        res += to_string(count);
    }
    
    if (res.length() > ssize)
        return s;
    
    return res;
}
