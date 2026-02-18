import java.io.*;
import java.util.*;

public class bj_16928_뱀과사다리게임 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x, y, u, v;

        HashMap<Integer, Integer> portal = new HashMap<>();
        for(int i = 0; i < n; i++)
        {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            portal.put(x, y);
        }

        for (int j = 0; j < m; j++)
        {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            portal.put(u, v);
        }

        int[] visited = new int[101];

        for(Integer key: portal.keySet())
        {
            visited[key] = -1;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        while(!queue.isEmpty()) {
            int curr = queue.poll();
            for (int dice = 1; dice <= 6; dice++) {
                if (curr + dice <= 100) {

                    if (visited[curr + dice] == 0) {
                        visited[curr + dice] = visited[curr] + 1;
                        queue.add(curr + dice);
                    }

                    if (visited[curr + dice] == -1) // portal 이 있는 경우
                    {
                        int dst = portal.get(curr + dice);
                        if (visited[dst] == 0) {
                            visited[dst] = visited[curr] + 1;
                            queue.add(dst);
                        }
                    }
                }
            }
        }

        System.out.print(visited[100]);
    }
}
