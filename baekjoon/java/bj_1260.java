import java.io.*;
import java.util.*;

// bfs와 dfs

public class bj_1260 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i<= n; i++)
        {
            graph[i] = new ArrayList<>();
        }

        for (int j = 0; j< m; j++)
        {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(w);
            graph[w].add(u); // undirected graph
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(graph[i]);
        }

        boolean[] visited = new boolean[n + 1];
        List<Integer>result_dfs = new ArrayList<>();
        dfs(v, graph, visited, result_dfs);

        for (int i = 1; i <= n; i++) {
            visited[i] = false;
        }
        List<Integer>result_bfs = bfs(v, graph, visited);


        for (Integer integer : result_dfs) {
            System.out.print(integer + " ");
        }
        System.out.println("");
        for (Integer integer : result_bfs) {
            System.out.print(integer + " ");
        }





    }
    public static List<Integer> dfs(int start, ArrayList<Integer>[] graph, boolean[] visited, List<Integer> result)
    {
        visited[start] = true;
        result.add(start);
        for (int next : graph[start])
        {
            if(!visited[next])
                dfs(next, graph, visited, result);
        }

        return result;
    }
    public static List<Integer> bfs(int start, ArrayList<Integer>[] graph, boolean[] visited)
    {
        List<Integer> result = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;
        result.add(start);

        while(!queue.isEmpty())
        {
            int x = queue.poll();
            for (int next : graph[x])
            {
                if(!visited[next])
                {
                    visited[next]= true;
                    result.add(next);
                    queue.add(next);
                }
            }
        }
        return result;
    }
}