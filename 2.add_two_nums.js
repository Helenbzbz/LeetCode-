function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
 
var addTwoNumbers = function(l1, l2) {
    var sum = 0
    var current = new ListNode(0)
    var result = current // set result as the first node
    
    while (l1 || l2){
        if (l1){
            sum += l1.val
            l1 = l1.next
        }
        if (l2){
            sum += l2.val
            l2 = l2.next
        }
        current.next = new ListNode (sum%10) // Create current.next
        current = current.next // Move to the next current
        sum = sum > 9 ? 1 : 0
    }
    if (sum) {
        current.next = new ListNode(sum)
    }
    return result.next
};

/*
Notes
	◦ Linked lists: structure that represents where each element points to the next one
	◦ Create linked lists by:
		ListNode dummy = new ListNode(0);
		dummy.next = head;
		dummy = dummy.next
https://codeburst.io/linked-lists-in-javascript-es6-code-part-1-6dd349c3dcc3
	Creating a node -> node has one value, has one previous, has one next
	=> use each individual nodes and item to connect to each other
	=> 不要从空间的角度去理解，就算是next也只是random存在某一个地方，但是是他的一个property，仅此而已

• if (a) is always faster than add one condition after it 
• This is the use of question mark in JavaScript

*/