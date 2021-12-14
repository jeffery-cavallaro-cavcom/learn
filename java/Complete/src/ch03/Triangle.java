package ch03;

/**
 * Computes the hypotenuse of a right triangle.  The other two sides are
 * specified on the command line and both default to 1.
 */

public class Triangle {
    private static final double DEFAULT_SIDE = 1.0;

    private static double getSide(String [] args, int index) {
        double side = DEFAULT_SIDE;
        if (index < args.length) {
            try {
                side = Double.valueOf(args[index]);
            }
            catch (NumberFormatException error) {
                System.err.println(
                    "Invalid side value, using " + DEFAULT_SIDE
                );
                side = DEFAULT_SIDE;
            }
        }
        return side;
    }

    public static void main(String [] args) {
        double a = getSide(args, 0);
        double b = getSide(args, 1);
        double c = Math.sqrt(a*a + b*b);
        System.out.println("a=" + a + " b=" + b + " c=" + c);
    }   
}
