package ch01;

/**
 * Adds two integer values supplied on the command line.
 */

public class Add {
    // Parses the specified string value for a decimal integer value.  Invalid
    // strings result an error message and a return value of 0.
    private static int getInteger(String svalue) {
        int ivalue = 0;
        try {
            ivalue = Integer.valueOf(svalue);
        }
        catch (NumberFormatException nfe) {
            System.err.println(
                "Invalid integer value \"" + svalue + "\" - using 0"
            );
            ivalue = 0;
        }
        return ivalue;
    }

    public static void main(String [] args) {
        // Get the two addends from the command line arguments.
        int add1 = (args.length > 0) ? getInteger(args[0]) : 0;
        int add2 = (args.length > 1) ? getInteger(args[1]) : 0;

        // Compare the two addends.
        if (add1 < add2) {
            System.out.println(add1 + " < " + add2);
        }
        if (add1 <= add2) {
            System.out.println(add1 + " <= " + add2);
        }
        if (add1 == add2) {
            System.out.println(add1 + " == " + add2);
        }
        if (add1 != add2) {
            System.out.println(add1 + " != " + add2);
        }
        if (add1 >= add2) {
            System.out.println(add1 + " >= " + add2);
        }
        if (add1 > add2) {
            System.out.println(add1 + " > " + add2);
        }

        // Add the two addends and display the result.
        int sum = add1 + add2;
        System.out.println(add1 + " + " + add2 + " = " + sum);
    }
}
