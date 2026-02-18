import java.io.*;
import java.util.*;

// 백트래킹

public class bj_1987_알파벳 {
    static int[][] board;
    static boolean[] visited = new boolean[26]; // a~z 총 26개
    static int r, c;
    static int answer;
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        board = new int[r][c];

        for (int i = 0; i<r;i++)
        {
            String line = br.readLine();
            for(int j =0 ; j<c; j++)
            {
                board[i][j] = line.charAt(j) - 'A';
            }
        }
        visited[board[0][0]] = true;
        dfs(0, 0, 1);
        System.out.println(answer);
    }

    static void dfs(int row, int col, int count)
    {
        answer = Math.max(answer, count);
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        for(int i = 0; i < 4; i++) {
            int next_row = row + dy[i];
            int next_col = col + dx[i];

            if (0 <= next_row && next_row < r && 0 <= next_col && next_col < c) {
                int alphabet = board[next_row][next_col];
                if (!visited[alphabet])
                {
                    visited[alphabet] = true;
                    dfs(next_row, next_col, count + 1);
                    visited[alphabet] = false;
                }

            }
        }
    }
}


