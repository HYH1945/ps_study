import java.io.*;
import java.util.*;

// 16724 피리부는사나이
// 사이클 탐지

public class bj_16724_피리부는사나이 {
    static int n, m;
    static int[] parent;
    static int[][] visited;
    static char[][] map;
    static int answer = 0;


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new int[n][m];
        map = new char[n][m];

        for (int i = 0; i < n; i++)
        {
            map[i] = br.readLine().toCharArray();
        }
        int count = 1;
        for (int i = 0; i < n; i++)
        {
            for (int j =0 ; j < m; j++)
            {
                if (visited[i][j] == 0)
                {

                    dfs(i,j,count);
                    count++;
                }
            }
        }

        System.out.print(answer);
    }


    static void dfs(int row, int col, int count)
    {
        visited[row][col] = count;
        int nextrow = row;
        int nextcol = col;

        if (map[row][col] == 'U') nextrow--;

        else if (map[row][col] == 'D') nextrow++;

        else if (map[row][col] == 'L') nextcol--;

        else if (map[row][col] == 'R') nextcol++;


        if(visited[nextrow][nextcol] == 0)
            dfs(nextrow, nextcol, count);
        else if (visited[nextrow][nextcol] == count)
            answer++; // 사이클 발견, 탐색종료
    }

}
