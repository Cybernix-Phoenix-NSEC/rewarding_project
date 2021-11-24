import java.util.*;
public class Electricbill
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        int units;
        double bill=0;
        String n;
        System.out.println("Enter the name of the customer");
        n=sc.next();
        System.out.println("Enter the units consumed");
        units=sc.nextInt();
        if (units<=100)
        {
        bill=units*2.0;
        }
        if (units>100 && units<=300)
        {
            bill=100.0*2.0+((units-100.0)*3.0);
        }
        if (units>300)
        {
            bill=100.0*2.0+200.0*3.0+((units-300.0)*5.0);
            double d=bill*5.0/100.0;
            bill=bill-d;
        }
        System.out.println("The name of the cumtomer is"+n);
        System.out.println("Number of units consumed is"+units);
        System.out.println("Bill amount"+bill);
    }
}
