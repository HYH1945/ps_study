import java.io.*;
import java.util.*;

//14503 로봇청소기, 구현문제

public class bj_14503_로봇청소기 {
    static int n, m;
    static int[][] room;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        room = new int[n][m];

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        for (int i = 0; i<n; i++)
        {
            st = new StringTokenizer(br.readLine());
            for (int j =0; j<m;j++)
            {
                room[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 북동남서 (반시계)
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        // 시작
        int answer = 0;
        int curr_row = r;
        int curr_col = c;

        boolean done = false;
//        for(int i = 0; i < n; i++){
//            for (int j = 0; j < m; j++)
//                System.out.print(room[i][j]);
//            System.out.println();
//        }
        boolean found = false;
        while(true)
        {
            found = false;
            if(room[curr_row][curr_col] == 0) {
                room[curr_row][curr_col] = 2;
                answer++;
            }

            //answer += 1;
            for (int i = 0; i < 4; i++)
            {
                int next_row = curr_row + dy[i];
                int next_col = curr_col + dx[i];

                if(0 <= next_row && next_row < n && 0 <= next_col && next_col < m)
                {
                    if(room[next_row][next_col] == 0){
                        //System.out.printf("%d %d %d\n", next_row, next_col, d);
                        //System.out.printf("%d %d %d\n", curr_row, curr_col, d);
                        found = true;
                        break;
                    }
                }
            }

            if(found)
            {
                for (int i = 0 ; i< 4; i++)
                {
                    d = (d+3) % 4;
                    int next_row = curr_row + dy[d];
                    int next_col = curr_col + dx[d];

                    if(room[next_row][next_col] == 0)
                    {
                        curr_row = next_row;
                        curr_col = next_col;
                        break;
                    }

                }
            }
            else // 후진가능하면 후진시키고 다시 루프, 불가능시 프로그램 종료
            {
                // 후진 -> 방향 뒤집기 : 현재 d가 0이면 2, 1이면 3, 2면 0, 3이면 1
                int back_d = (d+2) % 4;
                int next_row = curr_row + dy[back_d];
                int next_col = curr_col + dx[back_d];

                // 후진가능하면 후진, 아니면 종료
                if(room[next_row][next_col] == 1)
                    break;
                else{
                    curr_row = next_row;
                    curr_col = next_col;
                }
            }
        }
        System.out.print(answer);
    }



}
