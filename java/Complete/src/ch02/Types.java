package ch02;

/**
 * Demonstrates the various types supported by Java.
 */

public class Types {
    public static void main(String [] args) {
        Byte bvalue = Byte.valueOf((byte) 0);
        System.out.println("byte (" + bvalue + "):");
        System.out.println("  min=" + Byte.MIN_VALUE);
        System.out.println("  max=" + Byte.MAX_VALUE);
        System.out.println("  bytes=" + Byte.BYTES);
        System.out.println("  bits=" + Byte.SIZE);

        Short svalue = Short.valueOf((short) 0);
        System.out.println("\nshort (" + svalue + "):");
        System.out.println("  min=" + Short.MIN_VALUE);
        System.out.println("  max=" + Short.MAX_VALUE);
        System.out.println("  bytes=" + Short.BYTES);
        System.out.println("  bits=" + Short.SIZE);

        Integer ivalue = Integer.valueOf((int) 0);
        System.out.println("\nint (" + ivalue + "):");
        System.out.println("  min=" + Integer.MIN_VALUE);
        System.out.println("  max=" + Integer.MAX_VALUE);
        System.out.println("  bytes=" + Integer.BYTES);
        System.out.println("  bits=" + Integer.SIZE);

        Long lvalue = Long.valueOf((long) 0);
        System.out.println("\nlong (" + lvalue + "):");
        System.out.println("  min=" + Long.MIN_VALUE);
        System.out.println("  max=" + Long.MAX_VALUE);
        System.out.println("  bytes=" + Long.BYTES);
        System.out.println("  bits=" + Long.SIZE);
    }
}
