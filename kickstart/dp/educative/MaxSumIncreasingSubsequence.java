import java.lang.Math;
import java.util.Arrays;

class MaxSumIncreasingSubsequence {

    public void findMaxSumInSequenceRec(int[] input) {
        System.out.println(helper(input, 0, -1));
    }

    private int helper(int[] input, int cur, int prev) {
        if (cur >= input.length) {
            return 0;
        }

        int firstSum = 0;
        if (prev == -1 || input[cur] >= input[prev]) {
            firstSum = input[cur] + helper(input, cur + 1, cur);
        }
        int secondSum = helper(input, cur + 1, prev);
        return Math.max(firstSum, secondSum);
    }

    public void findMaxSumInSequenceDP(int[] input) {
        int[] plow = Arrays.copyOf(input, input.length);

        for (int edge = 1; edge < plow.length; edge++) {
            for (int roll = 0; roll < edge; roll++) {
                if (input[roll] < input[edge] && plow[roll] + input[edge] > plow[edge]) {
                    plow[edge] = plow[roll] + input[edge];
                }
            }
        }
        System.out.println(Arrays.toString(plow));
        System.out.println(plow[plow.length - 1]);
    }

    public static void main(String[] args) {
        MaxSumIncreasingSubsequence maxSum = new MaxSumIncreasingSubsequence();
        int[] nums = { 4, 1, 2, 6, 10, 1, 12 };
        maxSum.findMaxSumInSequenceDP(nums);
        nums = new int[] { -4, 10, 3, 7, 15 };
        maxSum.findMaxSumInSequenceDP(nums);
        nums = new int[] { 1, 3, 8, 4, 14, 6, 14, 1, 9, 4, 13, 3, 11, 17, 29 };
        maxSum.findMaxSumInSequenceDP(nums);
    }

}
