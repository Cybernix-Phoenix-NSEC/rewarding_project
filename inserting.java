import java.util.*;
class Inserting
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        int n,k,p,i;
        System.out.println("Enter number of array elements");
        n=sc.nextInt();
        int a[]=new int[n+1];
        System.out.println("Enter the array elements");
        for (i=0;i<n;i++)
        a[i]=sc.nextInt();
        System.out.println("Enter element to be inserted");
        k=sc.nextInt();
        System.out.println("Enter position of insertion");
        p=sc.nextInt();
        for (i=n-1;i>=p;i--)
        a[i+1]=a[i];
        a[p]=k;
        n++;
        System.out.println("Array elements after insertion");
        for (i=0;i<n;i++)
        System.out.println(a[i]);
    }
}
