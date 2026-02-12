import java.util.*;
import java.io.*;

// 중앙값구하기
// 핵심 :
// 다중 입력 로직
// pq 2개사용 중앙값

public class bj_2696 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;

        int t = Integer.parseInt(line.trim());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            int m = Integer.parseInt(st.nextToken());

            PriorityQueue<Integer> minpq = new PriorityQueue<>();
            PriorityQueue<Integer> maxpq = new PriorityQueue<>(Collections.reverseOrder());

            List<Integer> result = new ArrayList<>();
            int count = 0;

            while (count < m) {
                if (!st.hasMoreTokens()) {
                    String nextLine = br.readLine();
                    if (nextLine == null) break;
                    st = new StringTokenizer(nextLine);
                }
                while (st.hasMoreTokens() && count < m) {
                    if(minpq.size() == maxpq.size())
                        maxpq.add(Integer.parseInt(st.nextToken()));
                    else{
                        minpq.add(Integer.parseInt(st.nextToken()));
                    }

                    if(!minpq.isEmpty() && maxpq.peek() > minpq.peek())
                    {
                        int max = maxpq.poll();
                        int min = minpq.poll();
                        minpq.add(max);
                        maxpq.add(min);
                    }
                    count++;

                    if(count % 2 == 1)
                        result.add(maxpq.peek());
                }
            }
            System.out.println(result.size());
            for (int item : result)
                System.out.print(item + " ");
            System.out.println();
        }
    }
}