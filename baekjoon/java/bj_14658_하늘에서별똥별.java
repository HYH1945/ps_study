import java.io.*;
import java.util.*;

public class bj_14658_하늘에서별똥별 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<int[]> star_list = new ArrayList<>();

        for (int i = 0; i < k; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            star_list.add(new int[] {x-1, y-1});
        }
        int max_star = 0;
        for(int[] star_1 : star_list){
            for(int[] star_2 : star_list){
                int startX = star_1[0];
                int startY = star_2[1];
                int count = 0;
                for(int[] star : star_list){
                    if(star[0] >= startX && star[0] <= startX + l && star[1] >= startY && star[1] <= startY + l){
                        count++;
                    }
                }
                max_star = Math.max(max_star, count);
            }
        }
        System.out.print(k-max_star);
    }
}
