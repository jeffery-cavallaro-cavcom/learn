package ch03;

/**
 * Demonstrates the various types supported by Java.
 */

public class Types {
    private static final String MIN_LABEL = "  min=";
    private static final String MAX_LABEL = "  max=";
    private static final String BYTES_LABEL = "  bytes=";
    private static final String BITS_LABEL = "  bits=";

    public static void main(String [] args) {
        // byte
        Byte bvalue = Byte.valueOf((byte) 0);
        System.out.println("\nbyte (" + bvalue + "):");
        System.out.println(MIN_LABEL + Byte.MIN_VALUE);
        System.out.println(MAX_LABEL + Byte.MAX_VALUE);
        System.out.println(BYTES_LABEL + Byte.BYTES);
        System.out.println(BITS_LABEL + Byte.SIZE);

        // short
        Short svalue = Short.valueOf((short) 1);
        System.out.println("\nshort (" + svalue + "):");
        System.out.println(MIN_LABEL + Short.MIN_VALUE);
        System.out.println(MAX_LABEL + Short.MAX_VALUE);
        System.out.println(BYTES_LABEL + Short.BYTES);
        System.out.println(BITS_LABEL + Short.SIZE);

        // int
        Integer ivalue = Integer.valueOf(2);
        System.out.println("\nint (" + ivalue + "):");
        System.out.println(MIN_LABEL + Integer.MIN_VALUE);
        System.out.println(MAX_LABEL + Integer.MAX_VALUE);
        System.out.println(BYTES_LABEL + Integer.BYTES);
        System.out.println(BITS_LABEL + Integer.SIZE);

        // long
        Long lvalue = Long.valueOf(3L);
        System.out.println("\nlong (" + lvalue + "):");
        System.out.println(MIN_LABEL + Long.MIN_VALUE);
        System.out.println(MAX_LABEL + Long.MAX_VALUE);
        System.out.println(BYTES_LABEL + Long.BYTES);
        System.out.println(BITS_LABEL + Long.SIZE);

        // float
        Float fvalue = Float.valueOf(3.14F);
        System.out.println("\nfloat (" + fvalue + "):");
        System.out.println(MIN_LABEL + Float.MIN_VALUE);
        System.out.println(MAX_LABEL + Float.MAX_VALUE);
        System.out.println(BYTES_LABEL + Float.BYTES);
        System.out.println(BITS_LABEL + Float.SIZE);

        // double
        Double dvalue = Double.valueOf(3.14);
        System.out.println("\ndouble (" + dvalue + "):");
        System.out.println(MIN_LABEL + Double.MIN_VALUE);
        System.out.println(MAX_LABEL + Double.MAX_VALUE);
        System.out.println(BYTES_LABEL + Double.BYTES);
        System.out.println(BITS_LABEL + Double.SIZE);

        // char
        Character cvalue = Character.valueOf('\u00F1');
        System.out.println("\ncharacter (" + cvalue + "):");
        System.out.println(MIN_LABEL + (int) Character.MIN_VALUE);
        System.out.println(MAX_LABEL + (int) Character.MAX_VALUE);
        System.out.println(BYTES_LABEL + Character.BYTES);
        System.out.println(BITS_LABEL + Character.SIZE);

        // boolean
        Boolean tvalue = false;
        System.out.println("\nboolean:");
        System.out.println("  tvalue=" + tvalue);
        tvalue = true;
        System.out.println("  tvalue=" + tvalue);

        System.out.println();
    }
}
