'''
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
'''

'''
9-line accepted Java code, without the need of handling overflow
public boolean isPalindrome(int x) {
    if (x<0 || (x!=0 && x%10==0)) return false;
    int rev = 0;
    while (x>rev){
    	rev = rev*10 + x%10;
    	x = x/10;
    }
    return (x==rev || x==rev/10);
}

public boolean isPalindrome(int x) {

    if (x < 0) return false;

    int p = x;
    int q = 0;

    while (p >= 10){
        q *=10;
        q += p%10;
        p /=10;
    }

    return q == x / 10 && p == x % 10;
}
// so the reversed version of int is always 1 time short in the factor of 10s .

in case of Int16, check 63556 will finally check if (6553 == 6355 && 6 == 63556%10) so there will have no concerns about the overflow.
'''