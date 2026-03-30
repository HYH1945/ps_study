import java.util.*;
import java.io.*;

public class bj_2493_탑 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<int[]> stack = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i<=n; i++){
            int height = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty() && height > stack.peekLast()[0]){
                stack.pollLast();
            }
            if (!stack.isEmpty()) {
                sb.append(stack.peekLast()[1]).append(" ");
            }
            else{
                sb.append("0 ");
            }
            stack.addLast(new int[] {height, i});
        }
        System.out.print(sb.toString().trim());
    }
}
