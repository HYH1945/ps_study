import java.util.*;
import java.io.*;

// 1. bfs로 이동가능한 국경선끼리 모두 탐색하면서 list에 집어넣기
// 2. bfs 끝났으면 뭉친덩어리끼리 계산해서 인구이동
// 3. 메인 반복문 조건을 move의 true false 여부로 두고, 기본 move = false로 둔다음
// 4. bfs 돌리면서 한번이라도 인구이동이 일어난다면 move = true로 돌리기
// 5. 인구이동 한번도 안일어난다면 기본값은 move = false 이므로 종료

public class bj_16234_인구이동 {
    static int n, l, r;
    static int[][] visited;
    static int[][] board;
    static boolean move;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                System.out.print(board[i][j]);
//            }
//            System.out.println();
//        }

        int count = 1;
        int answer = 0;
        move = true;

        while(move){
            visited = new int[n][n];
            move = false;
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if(visited[i][j] == 0){
                        bfs(i, j, count);
                        count++;
                    }
                }
            }
//            for (int i = 0; i < n; i++){
//                for (int j = 0; j < n; j++) {
//                    System.out.print(board[i][j]);
//                }
//                System.out.println();
//            }

            if (move == false){
                break;
            }
            answer++;
        }
        System.out.print(answer);
    }

    static void bfs(int row, int col, int count) {
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        visited[row][col] = count;

        List<int[]> union = new ArrayList<>();
        union.add(new int[] {row, col});
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[] {row, col});
        while(!queue.isEmpty()) {

            int[] curr = queue.pollLast();
            int curr_row = curr[0];
            int curr_col = curr[1];

            for (int i = 0; i < 4; i++) {
                int next_row = curr_row + dy[i];
                int next_col = curr_col + dx[i];

                if(0 <= next_row && next_row < n && 0 <= next_col && next_col < n) {

                    if (visited[next_row][next_col] == 0 && (l <= Math.abs(board[curr_row][curr_col] - board[next_row][next_col]) && Math.abs(board[curr_row][curr_col] - board[next_row][next_col]) <= r)) {
                        move = true;
                        //System.out.print("왜");
                        visited[next_row][next_col] = count;
                        queue.addFirst(new int[] {next_row, next_col});
                        union.add(new int[] {next_row, next_col});
                    }
                }
            }
        }
        int union_sum = 0;
        for(int[] item : union){
            union_sum += board[item[0]][item[1]];
        }
        int after_moved = union_sum / union.size();
        for(int[] item : union){
            board[item[0]][item[1]] = after_moved;
        }


    }
}
