package ch04;

/**
 * Demonstrates the various operators supported by Java.  Two real operands are
 * specified on the command line and default to 1.0.
 */

 public class Operators {
    private static final double DEFAULT_VALUE = 1.0;

    private static double getOperand(String [] args, int index) {
        double arg = DEFAULT_VALUE;
        if (index < args.length) {
            String svalue = args[index];
            try {
                arg = Double.valueOf(svalue);
            }
            catch (NumberFormatException error) {
                System.err.println(
                    "Invalid real argument \"" + svalue + "\" - using 1"
                );
                arg = DEFAULT_VALUE;
            }
        }
        return arg;
    }

    private static <T> void showResult(T arg1, T arg2, char op, T result) {
        System.out.println(
            "  " + arg1 + " " + op + " " + arg2 + " = " + result
        );
    }

    public static void main(String [] args) {
        double darg1 = getOperand(args, 0);
        double darg2 = getOperand(args, 1);

        System.out.println("\nInteger arithmetic:");
        int iarg1 = (int) darg1;
        int iarg2 = (int) darg2;
        System.out.println("  -" + iarg1 + " = " + -iarg1);
        showResult(iarg1, iarg2, '+', iarg1 + iarg2);
        showResult(iarg1, iarg2, '-', iarg1 - iarg2);
        showResult(iarg1, iarg2, '*', iarg1 * iarg2);
        showResult(iarg1, iarg2, '/', iarg1 / iarg2);
        showResult(iarg1, iarg2, '%', iarg1 % iarg2);

        System.out.println("\nReal arithmetic:");
        System.out.println("  -" + darg1 + " = " + -darg1);
        showResult(darg1, darg2, '+', darg1 + darg2);
        showResult(darg1, darg2, '-', darg1 - darg2);
        showResult(darg1, darg2, '*', darg1 * darg2);
        showResult(darg1, darg2, '/', darg1 / darg2);
        showResult(darg1, darg2, '%', darg1 % darg2);

        System.out.println("\nCompound Operators:");
        System.out.println("  iarg1: " + iarg1);
        iarg1 += 1;
        System.out.println("  iarg1 += 1: " + iarg1);
        iarg1 -= 2;
        System.out.println("  iarg1 -= 2: " + iarg1);
        iarg1 *= 3;
        System.out.println("  iarg1 *= 3: " + iarg1);
        iarg1 /= 4;
        System.out.println("  iarg1 /= 4: " + iarg1);
        iarg1 %= 5;
        System.out.println("  iarg1 %= 5: " + iarg1);

        System.out.println("\nIncrement/Decrement:");
        System.out.println("  iarg1: " + iarg1 + "  iarg2: " + iarg2);
        int result = ++iarg1;
        System.out.println("  result = ++iarg1: " + result + "  iarg1: " + iarg1);
        result = --iarg2;
        System.out.println("  result = --iarg2: " + result + "  iarg2: " + iarg2);
        result = iarg1++;
        System.out.println("  result = iarg1++: " + result + "  iarg1: " + iarg1);
        result = iarg2--;
        System.out.println("  result = iarg2--: " + result + "  iarg2: " + iarg2);
    }
 }
