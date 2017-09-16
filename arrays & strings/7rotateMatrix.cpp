/** CTCI 1.7 Rotate Matrix
 Given a NxN matrix, rotate it by 90 degrees
 @param matrix is the matrix to be rotated (changed by func) **/
void rotateMatrix(vector<vector<int>>& matrix){
    size_t n = matrix.size();
    if (n == 0 || n != matrix[0].size())
        return;
    
    for (int i = 0; i < n/2 ; i++){
        int first = i;
        int last = n - 1 - i;
        
        for (int j = first; j < last; j++){
            int offset = j - first;
            int hold = matrix[first][j];
            
            matrix[first][j] = matrix[last - offset][first];                // left -> top
            matrix[last - offset][first] = matrix[last][last - offset];     // bottom -> left
            matrix[last][last - offset] = matrix[j][last];                  // right -> bottom
            matrix[j][last] = hold;                                         // top -> right
        }
    }
}
