import java.io.*;
import java.util.*;

public class bj_10026_적록색약 {
    static int n, horizon_max;
    static char[][] drawing;
    static int[][] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        horizon_max = 0;
        drawing = new char[n][n];
        for(int i = 0; i<n; i++) {
            String line = br.readLine();
            char[] char_arr = line.toCharArray();
            horizon_max = char_arr.length;
            for(int j = 0; j < char_arr.length ; j++){
                drawing[i][j] = char_arr[j];
            }
        }

        int count_x = 1;
        visited = new int[n][n];
        for (int i = 0; i<n; i++){
            for (int j = 0; j<horizon_max; j++){
                if(visited[i][j] == 0){
                    bfs(i, j, count_x++);
                }
            }
        }

        int count_y = 1;
        visited = new int[n][n];
        for (int i = 0; i<n; i++){
            for (int j = 0; j<horizon_max; j++){
                if(visited[i][j] == 0){
                    bfs_special(i, j, count_y++);
                }
            }
        }

        System.out.printf("%d %d", count_x - 1, count_y - 1);
    }

    static void bfs(int row, int col, int count){
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[] {row, col});
        while(!queue.isEmpty()){
            int[] curr = queue.pollLast();
            int curr_row = curr[0];
            int curr_col = curr[1];

            for (int i = 0; i < 4; i++){
                int next_row = curr_row + dy[i];
                int next_col = curr_col + dx[i];

                if(0 <= next_row && next_row < horizon_max && 0 <= next_col && next_col < n){
                    if(drawing[curr_row][curr_col] == drawing[next_row][next_col] && visited[next_row][next_col] == 0){
                        visited[next_row][next_col] = count;
                        queue.addFirst(new int[] {next_row, next_col});
                    }
                }
            }
        }
    }

    static void bfs_special(int row, int col, int count){
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[] {row, col});
        while(!queue.isEmpty()){
            int[] curr = queue.pollLast();
            int curr_row = curr[0];
            int curr_col = curr[1];

            for (int i = 0; i < 4; i++){
                int next_row = curr_row + dy[i];
                int next_col = curr_col + dx[i];

                if(0 <= next_row && next_row < horizon_max && 0 <= next_col && next_col < n){
                    if(drawing[curr_row][curr_col] == 'B') {
                        if (drawing[curr_row][curr_col] == drawing[next_row][next_col] && visited[next_row][next_col] == 0) {
                            visited[next_row][next_col] = count;
                            queue.addFirst(new int[]{next_row, next_col});
                        }
                    }
                    else{
                        if (drawing[next_row][next_col] != 'B' && visited[next_row][next_col] == 0) {
                            visited[next_row][next_col] = count;
                            queue.addFirst(new int[]{next_row, next_col});
                        }
                    }
                }
            }
        }
    }
}
