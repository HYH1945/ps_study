import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[][] meeting = new int[n][2];

        int progress = 0;
        int answer = 0;


        for (int i = 0; i<n; i++)
        {
            st = new StringTokenizer(br.readLine());
            meeting[i][0] = Integer.parseInt(st.nextToken());
            meeting[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(meeting, (o1, o2) -> {
            if (o1[1] == o2[1]){
                return Integer.compare(o1[0], o2[0]);
            }
            return Integer.compare(o1[1], o2[1]);
        });

        for (int i = 0; i < n; i++)
        {
            if (progress <= meeting[i][0])
            {
                progress = meeting[i][1];
                answer += 1;
            }
        }

        System.out.print(answer);
    }
}
