import java.io.*;
import java.util.*;

// topological sort

public class bj_2252 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] graph = new ArrayList[n+1];

        for (int i = 1; i<= n; i++)
        {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i<m; i++)
        {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(w); // directed graph
        }

        boolean[] visited = new boolean[n+1];
        List<Integer> result = new ArrayList<>();

        for(int i = 1; i<=n; i++)
            if(!visited[i])
                dfs(i, graph, visited, result);

        Collections.reverse(result);
        for(int item : result)
            System.out.print(item + " ");

    }

    public static List<Integer> dfs(int start, ArrayList<Integer>[] graph, boolean[] visited, List<Integer> result)
    {
        visited[start] = true;
        for (int next : graph[start])
        {
            if(!visited[next])
                dfs(next, graph, visited, result);
        }
        result.add(start);
        return result;
    }

}
