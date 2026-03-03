import java.io.*;
import java.util.*;
//import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] truthPeople = new int[truthCount];
        for (int i = 0; i < truthCount; i++) {
            truthPeople[i] = sc.nextInt();
        }

        List<int[]> parties = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int partySize = Integer.parseInt(st.nextToken());
            int[] partyAttendance = new int[partySize];
            if (partySize > 0) {
                partyAttendance[0] = Integer.parseInt(st.nextToken());
                for (int j = 1; j < partySize; j++) {
                    partyAttendance[j] = Integer.parseInt(st.nextToken());
                    // 같은 파티에 있는 사람들을 하나의 집합으로 합침
                    union(partyAttendance[0], partyAttendance[j]);
                }
            }
    }

}
