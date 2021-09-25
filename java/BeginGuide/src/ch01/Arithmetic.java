package ch01;

public class Arithmetic {
    private static <T> void show(T op1, String op, T op2, T answer) {
        System.out.println(op1 + " " + op + " " + op2 + " = " + answer);
    }

    public static void main(String [] args) {
        int n = 4;

        int i = 10;
        show(i, " + ", n, (i + n));
        show(i, " - ", n, (i - n));
        show(i, " * ", n, (i * n));
        show(i, " / ", n, (i / n));
        System.out.println();

        double x = 10.0;
        show(x, " + ", n, (x + n));
        show(x, " - ", n, (x - n));
        show(x, " * ", n, (x * n));
        show(x, " / ", n, (x / n));
    }
}
