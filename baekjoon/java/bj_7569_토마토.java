import java.util.*;
import java.io.*;

public class bj_7569_토마토 {
    static int[][][]box;
    static int m, n, h;
    static int[] dx = {0, 0, -1, 1, 0, 0};
    static int[] dy = {1, -1, 0, 0, 0, 0};
    static int[] dz = {0, 0, 0, 0, 1, -1};
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        box = new int[h][n][m];
        Queue<int[]> queue = new LinkedList<>();

        for(int i = 0; i < h; i++)
        {
            for (int j = 0 ; j < n; j++)
            {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++)
                {
                    box[i][j][k] = Integer.parseInt(st.nextToken());
                    if (box[i][j][k] == 1)
                    {
                        queue.add(new int[]{i, j, k});
                    }

                    //System.out.print(box[i][j][k]);

                }
            }
        }
        int max_count = 0;
        while(!queue.isEmpty())
        {
            int[] curr = queue.poll();
            max_count = Math.max(max_count, box[curr[0]][curr[1]][curr[2]]);
            for(int i = 0; i< 6; i++)
            {
                int next_row = curr[1] + dy[i];
                int next_col = curr[2] + dx[i];
                int next_height = curr[0] + dz[i];

                if(0 <= next_row && next_row < n && 0 <= next_col && next_col < m && 0 <= next_height && next_height < h)
                {
                    if(box[next_height][next_row][next_col] == 0)
                    {
                        box[next_height][next_row][next_col] = box[curr[0]][curr[1]][curr[2]] + 1;
                        queue.add(new int[]{next_height, next_row, next_col});
                    }
                }
            }
        }

        for(int i = 0; i<h; i++)
        {
            for(int j = 0; j < n; j++)
            {
                for(int k = 0; k < m; k++)
                {
                    if(box[i][j][k] == 0)
                    {
                        System.out.print(-1);
                        return;
                    }
                }
            }
        }
        System.out.print(max_count - 1);
    }

}
