import java.util.*;
class Star
{
    public static void main()
    {
        int k,m=9;
        for ( int i=1; i<=9; i+=2)
        {
            for (int j=1;j<=m;j++)
            {
                System.out.print(" ");        
            }
            for (k=1;k<=i;k++)
            {
                System.out.print("* ");
            }
            System.out.println();
            m=m-2;
        }
        int p=2;
        for (int a=7;a>=1;a-=2)
        {
            for (int y=1;y<=p;y++)
            {
                System.out.print(" ");
            }
            for (int b=1;b<=a;b++)
            {
                System.out.print("*"+" ");
            }
            System.out.println();
            p=p+2;
        }
    }
}
