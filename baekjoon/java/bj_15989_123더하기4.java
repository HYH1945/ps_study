import java.io.*;

public class bj_15989_123더하기4 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(br.readLine());
        int[] dp = new int[10001];
        dp[0] = 1;

        for(int i = 1; i < 10001; i++){
            dp[i] += dp[i-1];
        }

        for(int i = 2; i < 10001; i++){
            dp[i] += dp[i-2]; // i-2를 만든 경우의수 + 2하나 붙이기
        }

        for(int i = 3; i < 10001; i++){
            dp[i] += dp[i-3];
        }

        for(int i = 0; i< t; i++){
            int n = Integer.parseInt(br.readLine());
            System.out.println(dp[n]);
        }

    }
}
