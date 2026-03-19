import java.io.*;

public class bj_2579_계단오르기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[n];
        int[][] dp = new int[n][3];

        for(int i = 0; i <n; i++){
            stairs[i] = Integer.parseInt(br.readLine());
            dp[i][1] = stairs[i];

            if(i == 1) {
                dp[i][2] = dp[i-1][1] + stairs[i];
            }
            if(i >= 2){
                dp[i][1] += Math.max(dp[i-2][2], dp[i-2][1]);
                dp[i][2] = dp[i-1][1] + stairs[i];
            }
        }
        System.out.print(Math.max(dp[n-1][1], dp[n-1][2]));
    }

}
