import java.io.*;
import java.util.*;

// 17404 RGB 거리 2 -> 첫번째집 마지막집 색 체크때문에 2차원 DP에서 3차원 DP로

public class bj_17404_RGB거리2 {
    private static final int INF = 1000 * 1000 + 1;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[][] home = new int[n][3];

        for(int i = 0 ; i < n; i++)
        {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++) {
                home[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][][] dp = new int[n][3][3]; // [칠한 개수][현재 색깔][첫번째집 색깔]
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (j == k) {
                    dp[0][j][k] = home[0][j]; // 첫번째집 초기화
                } else {
                    dp[0][j][k] = INF;
                }
            }
        }

        for (int i = 1; i<n; i++)
        {
            for (int k = 0; k < 3; k++)
            {
                dp[i][0][k] = home[i][0] + Math.min(dp[i-1][1][k], dp[i-1][2][k]);
                dp[i][1][k] = home[i][1] + Math.min(dp[i-1][0][k], dp[i-1][2][k]);
                dp[i][2][k] = home[i][2] + Math.min(dp[i-1][0][k], dp[i-1][1][k]);
            }
        }

        int answer = INF;
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < 3; k++)
            {
                if (j != k)
                {
                    answer = Math.min(answer, dp[n-1][j][k]);
                }
            }
        }

        System.out.print(answer);
    }
}
