  
import java.util.*;
public class States_capitals
{     //opening of class
    public static void main(String[] args)
    {     //opening of main
        Scanner sc=new Scanner(System.in);
        int i,a,k;  //declaring the integer variables
        k=0;a=0;  //initializing the integer variables;
        String st;  //declaring the String variable
        
        String m[]=new String[10]; //creating 10 different memory locations in an array to store the strings
        String n[]=new String[10]; //creating 10 different memory locations in an array to store the strings
        
        for(i=0;i<10;i++)
        {
            System.out.println("Enter the state");  //to enter the names of 10 states
            m[i]=sc.nextLine();
            System.out.println("Enter the capital");  //to enter the names of 10 capitals
            n[i]=sc.nextLine();
        }
        System.out.println("Enter the state whose capital is to be searched"); //to enter the name of the state whose capital is to be searched
        st=sc.nextLine();
        
        for(i=0;i<10;i++)
        {
            if (m[i].equals(st))  //checking the condition
            {
                k=1;
                a=i;
            }
        }
        if (k==1)  //checking the condition
        System.out.println("The capital is :"+n[a]);  //printlng the name of the capital
        else
            System.out.println("The state :"+st+"is not found in any location");
        }   //closing of main
}   //closing of class
