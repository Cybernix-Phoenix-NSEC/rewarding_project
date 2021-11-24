import java.util.*;
public class Palindrome
{
    Scanner sc=new Scanner(System.in);
    public void check()
    {
        int n,num,rev=0,d;
        System.out.println("Enter a number");
        n=sc.nextInt();
        num=n;
        while (n!=0)
        {
            d=n%10;
            rev=(rev*10)+d;
            n=n/10;
        }
        if (rev==num)
        {
            System.out.println("Palindrome");
        }
        else
        {
            System.out.println("Not palindrome");
        }
    }
    public static void main()
    {
        Palindrome ob=new Palindrome();
        ob.check();
    }
}
