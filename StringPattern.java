public class StringPattrn
{
    public static void main(String args[])
    {
        String s="BLUEJ";
        for(int i=0;i<=s.length()-1;i++)
        {
            for(int j=0;j<=i;j++)
            {
               System.out.print(" ");
                
            }
            String s1=s.substring(0,s.length()-i);
            System.out.println(s1);
        
    }
}
}
