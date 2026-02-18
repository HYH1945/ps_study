import java.io.*;
import java.util.*;

public class bj_1043_거짓말 {
    static int[] parent;
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int truth = Integer.parseInt(st.nextToken());

        if (truth == 0)
        {
            System.out.println(m);
            return;
        }

        parent = new int[n+1];
        for (int i = 1; i<=n; i++)
            parent[i] = i;

        int[] truthpeople = new int[truth];
        for (int i = 0; i< truth; i++)
        {
            truthpeople[i] = Integer.parseInt(st.nextToken());
        }


        for (int i = 1; i < truth; i++)
        {
            union(truthpeople[0], truthpeople[i]);
        }


        List<int[]> parties = new ArrayList<>();
        for (int i = 0; i < m; i++)
        {
            st = new StringTokenizer(br.readLine());
            int partysize = Integer.parseInt(st.nextToken());
            int[] party_attend = new int[partysize];
            if (partysize > 0)
            {
                party_attend[0] = Integer.parseInt(st.nextToken());
                for (int j = 1; j<partysize;j++)
                {
                    party_attend[j] = Integer.parseInt(st.nextToken());

                    union(party_attend[0], party_attend[j]);
                }
            }
            parties.add(party_attend);
        }

        int answer = 0;
        for (int[] party : parties)
        {
            boolean canlie = true;
            for (int person : party)
            {
                if (isTruth(person, truthpeople[0])) {
                    canlie = false;
                    break;
                }

            }
            if(canlie) answer++;
        }
        System.out.println(answer);

    }

    static int find(int x)
    {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int x, int y)
    {
        x = find(x);
        y = find(y);
        if (x != y)
            parent[y] = x;
    }

    static boolean isTruth(int person, int truthperson)
    {
        return find(person) == find(truthperson);
    }




}
