import java.io.*;
import java.util.*;

public class bj_2533_사회망서비스 {
    static int n ;
    static List<Integer>[] adj_list;
    static int[][] dp;
    static boolean[] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        adj_list = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) adj_list[i] = new ArrayList<>();

        for (int i = 0; i < n-1; i++)
        {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            adj_list[u].add(v);
            adj_list[v].add(u);
        }
        dp = new int[n+1][2];
        visited = new boolean[n+1];
        dfs(1);
        System.out.print(Math.min(dp[1][0], dp[1][1]));
    }
    static void dfs(int curr)
    {
        visited[curr] = true;
        dp[curr][0] = 0;
        dp[curr][1] = 1;

        for(int next : adj_list[curr])
        {// 자식부터 올라가면서 처리
            if(!visited[next])
            {
                dfs(next);
                dp[curr][0] += dp[next][1]; // 현재 노드가 얼리어답터가 아니면 연결된 자식 모두 얼리어답터
                dp[curr][1] += Math.min(dp[next][0], dp[next][1]); // 현재 노드가 얼리어답터면 자식은 상관없음
            }
        }
    }
}
