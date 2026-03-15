import java.io.*;

public class bj_2140_지뢰찾기 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++)
        {
            String line = (br.readLine());
            for (int j = 0; j < n; j++)
            {
                if (line.charAt(j) == '#')
                    board[i][j] = -1;
                else
                    board[i][j] = line.charAt(j) -'0';
            }

        }
        // 8방향 검사: i-1 j-1 / i-1 j / i-1 j+1 / i j-1 / i j+1 / i+1 j-1 / i+1 j / i+1 j+1
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        int answer = 0;
        for (int i = 0 ; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == -1)
                {
                    boolean bomb = true;
                    // 폭탄 주변 8방향 검사 : 0이 한개라도 있으면 못놓음
                    for (int k = 0; k<8; k++)
                    {
                        int nx = i + dx[k];
                        int ny = j + dy[k];

                        if(0 <= nx && nx < n && 0<= ny && ny < n)
                        {
                            if(board[nx][ny] == 0) {
                                bomb = false;
                                break;
                            }
                        }
                    }

                    if(bomb)
                    {
                        answer++; // 폭탄을 놓고

                        // 주변 숫자 1 감소
                        for (int k = 0; k<8; k++)
                        {
                            int nx = i + dx[k];
                            int ny = j + dy[k];

                            if(0 <= nx && nx < n && 0<= ny && ny < n)
                            {
                                if(board[nx][ny] > 0) {
                                    board[nx][ny]--;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.print(answer);
    }
}
