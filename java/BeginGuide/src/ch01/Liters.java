package ch01;

/**
 * A program to convert gallons to liters.  The number of gallons is entered on the command line.
 */

public class Liters {
    public static final double LITERS_PER_GALLON = 3.7854;

    public static void main(String [] args) {
        double gallons;
        try {
            gallons = args.length > 0 ? Double.parseDouble(args[0]) : 0.0;
        }
        catch (NumberFormatException nfe) {
            System.out.println("Invalid numeric value: " + args[0]);
            return;
        }
        double liters = LITERS_PER_GALLON * gallons;
        System.out.println(gallons + " gallons = " + liters + " liters");
    }
}
