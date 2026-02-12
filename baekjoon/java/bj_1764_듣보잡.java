import java.util.*;
import java.io.*;

public class bj_1764_듣보잡 {
    // 듣보잡 (해시셋)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashSet<String> set = new HashSet<>();
        for (int i = 0; i<n; i++)
        {
            set.add(br.readLine());
        }

        ArrayList<String> result = new ArrayList<>();
        for (int j = 0 ; j<m; j++)
        {
            String name = br.readLine();
            if (set.contains(name))
                result.add(name);
        }

        Collections.sort(result);

        System.out.println(result.size());
        for (String s : result)
        {
            System.out.println(s);
        }
    }


}
