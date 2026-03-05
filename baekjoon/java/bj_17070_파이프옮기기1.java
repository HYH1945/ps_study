import java.util.*;
import java.io.*;

// 17070 파이프 옮기기 1 (bfs로 하면 시간초과, DP)

public class bj_17070_파이프옮기기1 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int [][] board = new int[n+1][n+1];

        for (int i = 1; i <= n; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1 ; j <= n; j++)
            {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][][] dp = new int[n+1][n+1][3]; // 0 : 가로    1: 세로    2: 대각
        dp[1][2][0] = 1;

        for (int i = 1; i <= n; i++)
        {
            for (int j = 3; j <=n; j++)
            {
                if(board[i][j] == 1)
                    continue;

                // 가로 경우
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2];


                // 세로 경우
                if(i-1 >= 1)
                {
                    dp[i][j][1] =  dp[i-1][j][1] + dp[i-1][j][2];
                }

                // 대각선 경우 (벽긁으면 안됨)
                if(i - 1 >= 1 && board[i][j] == 0 && board[i-1][j] == 0 && board[i][j-1] == 0)
                {
                    dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
                }
            }
        }

        System.out.print(dp[n][n][0] + dp[n][n][1] + dp[n][n][2]);


    }
}
