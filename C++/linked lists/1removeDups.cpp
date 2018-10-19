/** CTCI 2.1 Remove Dups
    Remove duplicates from an unsorted linked list
    @param head is the pointer to the beginning of the list **/
void removeDups(Node* head){
    unordered_set<int> set;
    Node* prev = NULL;
    
    while (head){
        if (set.find(head->data) != set.end()){
            prev->next = head->next;
        }
        else{
            set.insert(head->data);
            prev = head;
        }
        head = head->next;
    }
}




/** CTCI 2.1.1 Remove Dups (No Temp Buffer)
    Remove duplicates from an unsorted list without using temporary buffer
    @param head is the pointer to the beginning of the list **/
void rdNoBuff(Node* head){
    // if no list, no comparison
    Node* outer = head;
    if (outer == NULL)
        return;
    
    // if one element in list, no comparison
    Node* inner = head->next;
    if (inner == NULL)
        return;
    
    Node* prev = NULL;
    while (outer){
        prev = outer;
        inner = outer->next;
        while (inner){
            if (inner->data == outer->data)
                prev->next = inner->next;
            else
                prev = inner;
            
            inner = inner->next;
        }
        outer = outer->next;
    }
}
