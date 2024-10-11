package ch01;

/**
 * Simple use of variables.
 */

public class Number {
    public static void main(String [] args) {
        int number = 100;
        System.out.println("The value of number is " + number);

        number *= 2;
        System.out.print("The value of number is now ");
        System.out.println(number);
    }
}
