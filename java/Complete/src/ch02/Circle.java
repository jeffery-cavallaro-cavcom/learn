package ch02;

/**
 * Calculates the diameter, circumference, and area of a circle whose radius
 * is entered on the command line.
 */

public class Circle {
    public static void main(String [] args) {
        double r = args.length > 0 ? Double.parseDouble(args[0]) : 1.0;
        double d = 2.0*r;
        double c = Math.PI*d;
        double a = Math.PI*r*r;

        System.out.println("r = " + r);
        System.out.println("d = " + d);
        System.out.println("c = " + c);
        System.out.println("a = " + a);
    }
}
