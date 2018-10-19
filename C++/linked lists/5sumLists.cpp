/** CTCI 2.5 Sum Lists
 Given two numbers stored backwards in linked lists, find the sum
 i.e. (7 -> 1 -> 6) + (5 -> 9 -> 2) = 617 + 295 = 912
 @param head1 is the first node of one list
 @param head2 is the first node of the other list
 @returns the sum of the two numbers **/
int sumLists(Node* head1, Node* head2){
    int res = 0;
    int tmp = 0;
    int count = 0;
    int carry = 0;
    
    // add both numbers
    while (head1 && head2){
        tmp = head1->data + head2->data + carry;
        if (tmp >= 10){
            carry = 1;
            tmp -= 10;
        }
        else
            carry = 0;
        
        res += tmp * pow(10, count);
        head1 = head1->next;
        head2 = head2->next;
        count++;
    }
    
    // leftover of one list
    while (head1){
        res += (head1->data + carry) * pow(10, count);
        head1 = head1->next;
        carry = 0;
        count++;
    }
    while(head2){
        res += (head2->data + carry) * pow(10, count);
        head2 = head2->next;
        carry = 0;
        count++;
    }
    
    // leftover carry at end
    if (carry == 1){
        res += 1 * pow(10, count);
    }
    
    return res;
}
