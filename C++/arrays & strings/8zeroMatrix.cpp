/** CTCI 1.8 Zero Matrix
 if an element is 0, entire row and column are set to 0
 @param matrix is the matrix to change **/
void zeroRow(vector<vector<int>>& matrix, int row){
    int rowsize = matrix[0].size();
    for (int i = 0; i < rowsize; i++)
        matrix[row][i] = 0;
}

void zeroCol(vector<vector<int>>& matrix, int col){
    int colsize = matrix.size();
    for (int i = 0; i < colsize; i++)
        matrix[i][col] = 0;
}

void zeroMatrix(vector<vector<int>>& matrix){
    size_t m = matrix.size();           // rows
    size_t n = matrix[0].size();        // cols
    
    bool top_row = false;
    bool left_col = false;
    
    for (int i = 0; i < n ; i++){
        if (matrix[0][i] == 0){
            top_row = true;
            break;
        }
    }
    
    for (int i = 0; i < m; i++){
        if (matrix[i][0] == 0){
            left_col = true;
            break;
        }
    }
    
    
    // check where the zeros are
    for (int i = 1; i < m; i++){
        for (int j = 1; j < n; j++){
            if (matrix[i][j] == 0){
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    
    // zero out appropriate rows & cols
    for (int i = 1; i < m; i++){
        if (matrix[i][0] == 0)
            zeroRow(matrix, i);
    }
    
    for (int j = 1; j < n; j++){
        if (matrix[0][j] == 0)
            zeroCol(matrix, j);
    }
    
    if (top_row)
        zeroRow(matrix, 0);
    if (left_col)
        zeroCol(matrix, 0);
    
}
