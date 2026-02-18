import java.io.*;
import java.util.*;

// 백준 7576 토마토
// multisource bfs

public class bj_7576_토마토 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int [][] box = new int[n][m];
        Queue<int[]> queue = new LinkedList<>();

        for(int i = 0;i<n; i++)
        {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<m; j++)
            {
                box[i][j] =Integer.parseInt(st.nextToken());
                if (box[i][j] == 1)
                {
                    queue.add(new int[]{i, j});
                }

            }
        }

        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        while (!queue.isEmpty())
        {
            int[] curr = queue.poll();
            int row = curr[0];
            int col = curr[1];

            for (int i = 0; i<4;i++)
            {
                int next_row = row + dy[i];
                int next_col = col + dx[i];

                if(0 <= next_row && next_row < n && 0 <= next_col && next_col < m) {
                    if (box[next_row][next_col] == 0) {
                        box[next_row][next_col] = box[row][col] + 1;
                        queue.add(new int[]{next_row, next_col});
                    }
                }
            }
        }

        int answer = -1;
        for(int i =0; i<n; i++)
        {
            for (int j = 0 ; j<m; j++)
            {
                answer = Math.max(answer, box[i][j]);
                if(box[i][j] == 0) {
                    answer = -1;
                    System.out.println(answer);
                    return;
                }
            }
        }
        System.out.println(answer - 1);
    }
}
