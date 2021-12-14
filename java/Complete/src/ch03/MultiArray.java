package ch03;

/**
 * Demonstrates a multi-dimensional array with differing row sizes.
 */

public class MultiArray {
    private static final int NROWS = 5;

    public static void main(String [] args) {
        // Allocate
        int [][] values = new int[NROWS][];
        for (int i = 0; i < values.length; ++i) {
            values[i] = new int[i + 1];
        }

        // Assign
        int value = 0;
        for (int [] row : values) {
            for (int i = 0; i < row.length; ++i) {
                row[i] = ++value;
            }
        }

        // Show (with var)
        for (var row : values) {
            for (var i : row) {
                System.out.print(" " + i);
            }
            System.out.println();
        }
    }
}
