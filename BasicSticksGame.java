import java.util.*;
class Game
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        char ch='y';
        int n,a=0;
        while(ch=='y')
        {
            System.out.println("\t\tRules:");
            System.out.println("1.There are 51 sticks in total.");
            System.out.println("2.You have to pick any number of sticks(1-4).");
            System.out.println("3.One who picks the last stick loses.");
            System.out.println("Ready to play(y/n)?");
            ch=sc.next().charAt(0);
            if(ch!='y')
            {
                System.out.println("Have a Nice Day");
                break;
            }
            n=51;
            while(n!=1)
            {
                System.out.println("Enter the Number of Sticks you want to pick:");
                a=sc.nextInt();

                //As I didn't knew thread
                for(double i=0;i<10000000.0d;i++)
                    System.out.print("");
                switch(a)
                {
                    case 1:
                    case 2:
                    case 3:
                    case 4:System.out.println("Computer Picks:"+(5-a));
                        n-=5;
                        System.out.println("Sticks Remaining:"+n);
                        break;
                    default:System.out.println("Wrong Choice.....");
                        break;

                }
            }
            if(n==1)
            {
                System.out.println("You have to pick the last Stick.\n \t\tComputer Wins....");
            }
            System.out.println("Wanna Play Again(y/n)):");
            ch=sc.next().charAt(0);
            if(ch!='y')
            {
                System.out.println("Have a Nice Day...");
                break;
            }
        }
    }
}
