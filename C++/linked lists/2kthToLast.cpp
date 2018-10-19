/** CTCI 2.2 Kth to Last
 Find the kth to last element of a singly linked list
 @param head is the first node in linked list
 @param k is the element to find (index: n - k)
 @returns data of kth to last element **/
int kth_to_last(Node* head, int k){
    Node* runner = head;
    for (int i = 0; i < k; i++){
        runner = runner->next;
    }
    
    Node* result = head;
    while (runner){
        result = result->next;
        runner = runner->next;
    }
    
    return result->data;
}
