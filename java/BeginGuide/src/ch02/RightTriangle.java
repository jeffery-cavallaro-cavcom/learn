package ch02;

/**
 * An abstraction of a right triangle.  The constructor is used to set the base and height, and then calculates the
 * resulting hypotenuse.
 */

public class RightTriangle {
    private final double base;
    private final double height;
    private final double hypotenuse;

    public RightTriangle(double base, double height) {
        this.base = base;
        this.height = height;
        this.hypotenuse = Math.sqrt(this.base*this.base + this.height*this.height);
    }

    public double getBase() {
        return base;
    }

    public double getHeight() {
        return height;
    }

    public double getHypotenuse() {
        return hypotenuse;
    }

    // Read base and height from the command line.
    public static void main(String [] args) {
        double base, height;
        int n = args.length;
        try {
            base = (n > 0) ? Double.parseDouble(args[0]) : 1.0;
            height = (n > 1) ? Double.parseDouble(args[1]) : 1.0;
        }
        catch (NumberFormatException nfe) {
            System.out.println(nfe.getMessage());
            return;
        }
        RightTriangle rt = new RightTriangle(base, height);
        System.out.println("a=" + rt.getBase() + " b=" + rt.getHeight() + " c=" + rt.getHypotenuse());
    }
}
