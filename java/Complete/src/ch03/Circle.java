package ch03;

/**
 * Computes the diameter, circumference, and area of a circle with the
 * specified radius.  The radius is specified on the command line and defaults
 * to 1.
 */

public class Circle {
    private static final double DEFAULT_RADIUS = 1.0;

    private static double getRadius(String [] args) {
        double radius = DEFAULT_RADIUS;
        if (args.length > 0) {
            try {
                radius = Double.valueOf(args[0]);
            }
            catch (NumberFormatException error) {
                System.err.println(
                    "Invalid radius value, using " + DEFAULT_RADIUS
                );
                radius = DEFAULT_RADIUS;
            }
        }
        return radius;
    }

    public static void main(String [] args) {
        double radius = getRadius(args);
        double diameter = 2 * radius;
        double circumference = Math.PI * diameter;
        double area = Math.PI * radius * radius;
        System.out.println(
            "Circle: R=" + radius +
            " D=" + diameter +
            " C=" + circumference +
            " A=" + area
        );
    }
}
