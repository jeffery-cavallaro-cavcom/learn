package ch01;

/**
 * Compares two numbers from the command line.
 */

public class Compare {
    public static void main(String [] args) {
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);

        if (x < y) {
            System.out.println(x + " < " + y);
        } else if (x == y) {
            System.out.println(x + " = " + y);
        } else {
            System.out.println(x + " > " + y);
        }
    }
}
