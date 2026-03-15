import java.io.*;
import java.util.*;

// 14891 톱니바퀴 (구현)
// 연쇄작용 생각을 안해서 틀림

public class bj_14891_톱니바퀴 {
    static String[] gears;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        gears = new String[4];

        // 서로 맞닿은부분 : 인덱스 2
        // 인덱스2의 값이 서로 같으면 회전영향 x
        // 다르면 서로 반대로 회전

        // 시계방향 회전 : 배열을 오른쪽으로 한칸씩 밀기
        // 반시계 : 왼쪽으로 한칸씩 밀기
        for (int i = 0; i<4; i++){
            gears[i] = br.readLine();
        }

        int k = Integer.parseInt(br.readLine());

        for(int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int curr = Integer.parseInt(st.nextToken()) - 1;
            int angle = Integer.parseInt(st.nextToken());
            int[] directions = new int[4];
            directions[curr] = angle;

            // 왼쪽으로 연쇄작용
            for(int j = curr-1; j >= 0; j--)
            {
                if(gears[j].charAt(2) != gears[j+1].charAt(6))
                    directions[j] = -directions[j+1];
                else
                    break;
            }
            for(int j = curr+1; j < 4; j++)
            {
                if(gears[j].charAt(6) != gears[j-1].charAt(2))
                    directions[j] = -directions[j-1];
                else
                    break;
            }

            for(int j = 0; j < 4; j++)
                rotate(j, directions[j]);
        }
        double answer = 0;
        for (int i = 0; i < 4; i++) {
            if (gears[i].charAt(0) == '0')
                continue;
            else {
                answer += Math.pow(2, i);
            }
        }
        System.out.print((int)answer);
    }
    static void rotate(int gear_num, int angle)
    {
        if(angle == 1) // 시계
        {
            gears[gear_num] = gears[gear_num].charAt(gears[gear_num].length()-1) + gears[gear_num].substring(0, gears[gear_num].length()-1);
        }
        else if(angle == -1)
        {
            gears[gear_num] = gears[gear_num].substring(1) + gears[gear_num].charAt(0);
        }

    }


}
