/** CTCI 2.3 Delete Middle Node
 Delete the middle node in a linked list
 @param head is the first node of the linked list **/
void del_mid(Node* head){
    if (head == NULL)
        return;
    
    Node* runner = head;
    Node* result = head;
    Node* prev = NULL;
    
    for (int i = 0; i < 2; i++){
        runner = runner->next;
        if (head == NULL)
            return;
    }
    
    while (runner && runner->next != NULL){
        prev = result;
        runner = runner->next;              // runner jumps twice
        runner = runner->next;
        result = result->next;              // result jumps once
    }
    
    if (runner)                             // if odd, delete middle
        result->next = result->next->next;
    else                                    // if even
        prev->next = prev->next->next;      // delete first one
}
