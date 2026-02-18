import java.util.*;
import java.io.*;

// 분할정복

public class bj_1074_Z {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int answer = 0;
        while(n > 0)
        {
            n -= 1;
            int half = (int) Math.pow(2, n);
            if (r < half && c < half) // 1사분면
            {
                continue;
            }
            else if (r < half && c >= half) // 2사분면
            {
                answer += half * half;
                c -= half;
            }
            else if (r >= half && c < half) // 3사분면
            {
                answer += 2* (half * half);
                r -= half;
            }
            else // 4사분면
            {
                answer += 3* (half * half);
                r -= half;
                c -= half;
            }
        }

        System.out.println(answer);
    }
}
