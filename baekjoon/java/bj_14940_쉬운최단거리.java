import java.io.*;
import java.util.*;

public class bj_14940_쉬운최단거리 {
    static int n, m;
    static int[][] board;
    static int[][] dist;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        dist = new int[n][m];

        int start_row = 0, start_col = 0;

        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<m; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 2){
                    start_row = i;
                    start_col = j;
                }
                if (board[i][j] != 0)
                    dist[i][j] = -1;
            }
        }

        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        int distance = 0;
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[]{start_row, start_col, distance});
        while(!queue.isEmpty()){
            int[] curr = queue.pollLast();
            int curr_row = curr[0];
            int curr_col = curr[1];
            distance = curr[2];

            for(int j = 0; j<4; j++){
                int next_row = dy[j] + curr_row;
                int next_col = dx[j] + curr_col;

                if(0 <= next_row && next_row < n && 0 <= next_col && next_col < m){
                    if(board[next_row][next_col] != 0 && dist[next_row][next_col] == -1){
                        dist[next_row][next_col] = distance + 1;
                        queue.addFirst(new int[]{next_row, next_col, distance+1});
                    }
                }
            }


        }
        dist[start_row][start_col] = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sb.append(dist[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
        }
    }
