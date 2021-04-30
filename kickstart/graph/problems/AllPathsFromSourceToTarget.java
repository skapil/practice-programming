import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.util.Map;
import java.util.List;

public class AllPathsFromSourceToTarget {

    public Map<Integer, List<Integer>> buildGraph(int[][] input) {
        return IntStream.range(0, input.length).boxed().collect(Collectors.toMap(idx -> idx, idx -> input[idx]));
    }

    public static void main(String[] args) {
        AllPathsFromSourceToTarget sourceToTarget = new AllPathsFromSourceToTarget();
        int[][] input = new int[][] { { 1, 2 }, { 3 }, { 3 }, {} };
        System.out.println(sourceToTarget.buildGraph(input).toString());
    }

}
