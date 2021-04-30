import java.lang.Math;

class LongestSubsequency {

   public static int getLongestSubsequenceRec(String first, String second, int firstIndex, int secondIndex) {
        if (firstIndex >= first.length() || secondIndex >= second.length()) {
            return 0;
        }

        if (first.charAt(firstIndex) == second.charAt(secondIndex)) {
            return 1 + getLongestSubsequenceRec(first, second, firstIndex + 1, secondIndex + 1);
        }
        int matchFirst = getLongestSubsequenceRec(first, second, firstIndex + 1, secondIndex);
        int matchSecond = getLongestSubsequenceRec(first, second, firstIndex, secondIndex + 1);
        return Math.max(matchFirst, matchSecond);
   }

   public static int getLongestSubsequenceMemo(String first, String second) {
        Integer [][] table = new Integer[first.length()][second.length()];
        return helper(table, first, second, 0, 0);
   }

   public static int helper(Integer[][] table, String first, String second, int firstIndex, int secondIndex) {
        if (firstIndex >= first.length() || secondIndex >= second.length()) {
            return 0;
        }

        if (table[firstIndex][secondIndex] == null) {
            if (first.charAt(firstIndex) == second.charAt(secondIndex)) {
                return 1 + helper(table, first, second, firstIndex + 1, secondIndex + 1);
            } else {
                int firstMatch = helper(table, first, second, firstIndex + 1, secondIndex);
                int secondMatch = helper(table, first, second, firstIndex, secondIndex + 1);
                table[firstIndex][secondIndex] = Math.max(firstMatch, secondMatch);
            }
        }
        return table[firstIndex][secondIndex];
   }


   public static int getLongestSubsequenceDp(String first, String second) {
    int[][] table = new int[first.length() + 1][second.length() + 1];
    int maxLen = 0;

    for (int row = 1; row <= first.length(); row++) {
        for (int col = 1; col <= second.length(); col++) {
            if (first.charAt(row - 1) == second.charAt(col - 1)) {
                table[row][col] = 1 + table[row - 1][col - 1];
            } else {
                table[row][col] = Math.max(table[row - 1][col], table[row][col - 1]);
            }
            maxLen = Math.max(maxLen, table[row][col]);
        }
    }
    return maxLen;
   }

   public static void main(String[] args) {
       System.out.println("Executing the function to get the values");
       System.out.println(getLongestSubsequenceDp("abdca", "cbda"));
       System.out.println(getLongestSubsequenceDp("passport", "ppsspt"));
   }

}
