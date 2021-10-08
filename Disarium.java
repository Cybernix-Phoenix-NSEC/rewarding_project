import java.util.*;
public class Disarium
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        int n,a,c=0,d;
        double sum=0.0;
        System.out.println("Enter a number");
        n=sc.nextInt();
        a=n;
        int b=n;
        while (n!=0)
        {
            d=n%10;
            c=c+1;
            n=n/10;
        }
        while (a!=0)
        {
            d=a%10;
            sum=sum+Math.pow(d,c--);
            a=a/10;
        }
        if (sum==b)
        {
            System.out.println("Disarium number");
        }
        else
        {
            System.out.println("Not a disarium number");
        }
    }
}
