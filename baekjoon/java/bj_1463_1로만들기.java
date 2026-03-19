import java.io.*;
// 1로 만들기 (DP)

public class bj_1463_1로만들기 {
    static int x;
    static int[] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        x = Integer.parseInt(br.readLine());
        dp = new int[x+1];
        for(int i = 0; i < dp.length; i++){
            dp[i] = Integer.MAX_VALUE;
        }
        dp[x] = 0;
        while(x != 1) {
            if(dp[x] == Integer.MAX_VALUE)
                continue;

            if (x % 3 == 0) {
                dp[x/3] = Math.min(dp[x/3], dp[x] + 1);
            }
            if (x % 2 == 0) {
                dp[x/2] = Math.min(dp[x/2], dp[x] + 1);
            }
            dp[x-1] = Math.min(dp[x-1], dp[x] + 1);

            x--;
        }
        System.out.print(dp[1]);
    }
}
