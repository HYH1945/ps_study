import java.io.*;
import java.util.*;

public class bj_11053_가장긴증가하는부분수열 {
    static int[] dp,arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        dp = new int[n];
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            dp[i] = 1;
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] > arr[j]) dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }
        int max = 0;
        for(int item : dp)
            max = Math.max(max, item);
        System.out.print(max);
    }
}
