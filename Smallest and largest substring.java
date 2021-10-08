import java.util.Scanner;

public class Comparison {
  
    //function to find the smallest and largest substring.
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        String a;
        int n = 0;
        for (int i = k; i <= s.length(); i++) {
            a = s.substring(n, i);
            if (a.compareTo(smallest) < 0)
                smallest = a;
            if (a.compareTo(largest) > 0)
                largest = a;
            n++;
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String s = scan.nextLine();
        System.out.print("Enter length of substring : ");
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
