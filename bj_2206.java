import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 2206번

class Node {
    int x, y, dist, broken;

    Node(int x, int y, int dist, int broken) {
        this.x = x;
        this.y = y;
        this.dist = dist;
        this.broken = broken; // 0: 안 부숨, 1: 이미 부숨
    }
}
public class bj_2206 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        int[] dx = {-1, 1, 0, 0}; // 상 하 좌 우
        int[] dy = {0, 0, 1, -1}; // 상 하 좌 우
        int[][] arr = new int[n][m];
        boolean[][][] visited = new boolean[n][m][2];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                int val = line.charAt(j) - '0';
                arr[i][j] = val;
            }
        }

        // bfs
        // List<Integer> result = new ArrayList<>();
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 1, 0));
        visited[0][0][0] = true;
        int answer = -1;
        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.x == n - 1 && current.y == m - 1) {
                answer = current.dist;
                break;
            }
            for (int i = 0; i < 4; i++) {
                int curr_x = current.x + dx[i];
                int curr_y = current.y + dy[i];

                if (curr_x < 0 || curr_x >= n || curr_y < 0 || curr_y >= m)
                    continue;

                if (arr[curr_x][curr_y] == 0) {
                    if (!visited[curr_x][curr_y][current.broken]) {
                        visited[curr_x][curr_y][current.broken] = true;
                        queue.add(new Node(curr_x, curr_y, current.dist + 1, current.broken));
                    }
                } else {
                    if (current.broken == 0 && !visited[curr_x][curr_y][1]) {
                        visited[curr_x][curr_y][1] = true;
                        queue.add(new Node(curr_x, curr_y, current.dist + 1, 1));
                    }
                }

            }

        }

        System.out.print(answer);
    }
}
