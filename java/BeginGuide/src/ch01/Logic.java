package ch01;

public class Logic {
    public static void main(String [] args) {
        int v1 = 0, v2 = 0;
        int n = args.length;
        try {
            if (n > 0) v1 = Integer.parseInt(args[0]);
            if (n > 1) v2 = Integer.parseInt(args[1]);
        }
        catch (NumberFormatException nfe) {
            System.out.println(nfe.getMessage());
            return;
        }

        if (v1 < v2) System.out.println(v1 + " < " + v2);
        if (v1 <= v2) System.out.println(v1 + " <= " + v2);
        if (v1 == v2) System.out.println(v1 + " == " + v2);
        if (v1 != v2) System.out.println(v1 + " != " + v2);
        if (v1 >= v2) System.out.println(v1 + " >= " + v2);
        if (v1 > v2) System.out.println(v1 + " > " + v2);
    }
}
