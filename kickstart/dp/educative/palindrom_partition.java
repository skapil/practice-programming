/*
Given a string, we want to cut it into pieces such that each piece is a
palindrome. Write a function to return the minimum number of cuts needed.

Example 1:
    Input: "abdbca"
    Output: 3
    Explanation: Palindrome pieces are "a", "bdb", "c", "a".

Example 2:
    Input: = "cddpd"
    Output: 2
    Explanation: Palindrome pieces are "c", "d", "dpd".

Example 3:
    Input: = "pqr"
    Output: 2
    Explanation: Palindrome pieces are "p", "q", "r".

Example 4:
    Input: = "pp"
    Output: 0
    Explanation: We do not need to cut, as "pp" is a palindrome.
*/

class PalindromicPartition {

    public static bollean isPalindrom(String seq) {
        int start = 0;
        int end = seq.length() - 1;
        while (start <= end) {
            if (seq.charAt(start) != seq.charAt(end))
                return False
            start++;
            end--;
        }
        return True
    }

    public static makePalindromicPartiions(String seq) {
        List<List<String>> results = Arrays.asList();
        return helper(min_cuts, start, end);
    }

    public static helper(int min_cuts, int start, int end) {
        if start >= seq.length() && isPalindrom(seq.substring(start, end))
            return 0

        if end == len(seq):
            helper(min_cuts, start + 1, len(seq) - 1)
        else:
            helper(min_cuts, start + 1, len(seq) - 1)
    }

    public static void main(String[] args) {

    }
}
