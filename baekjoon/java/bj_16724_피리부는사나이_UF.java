import java.io.*;
import java.util.*;

// 16724 피리부는사나이
// 사이클 탐지

public class bj_16724_피리부는사나이_UF {
    static int n, m;
    static int[] parent;
    static char[][] map;
    static int answer = 0;


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][m];
        parent = new int[n*m];

        for (int i = 0; i < n*m; i++)
            parent[i] = i;

        for (int i = 0; i < n; i++)
        {
            map[i] = br.readLine().toCharArray();
        }

        int answer = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0 ; j < m; j++)
            {
                int nextrow = i;
                int nextcol = j;

                if (map[i][j] == 'U') nextrow--;
                else if (map[i][j] == 'D') nextrow++;
                else if (map[i][j] == 'L') nextcol--;
                else if (map[i][j] == 'R') nextcol++;

                int curr_idx = (i * m) + j;
                int next_idx = (nextrow * m) + nextcol;

                if(find(curr_idx) != find(next_idx))
                    union(curr_idx, next_idx);
                else
                    answer++;
            }
        }

        System.out.print(answer);
    }

    static int find(int x)
    {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int x, int y)
    {
        x = find(x);
        y = find(y);

        if (x != y)
            parent[y] = x;
    }

}
