package ch03;

/**
 * Demonstrates the use of literals.
 */

public class Literals {
    public static void main(String [] args) {
        // integer
        int ivalue = 0b0110_0100;
        System.out.println("binary: " + ivalue);
        ivalue = 0144;
        System.out.println("octal: " + ivalue);
        ivalue = 100;
        System.out.println("decimal: " + ivalue);
        ivalue = 0x64;
        System.out.println("hexadecimal: " + ivalue);

        // real
        float fvalue = 9.625F;
        System.out.println("\nfloat: " + fvalue);
        double dvalue = 9.625;
        System.out.println("double: " + dvalue);
        dvalue = 962.5e-2;
        System.out.println("-E: " + dvalue);
        dvalue = 0.09625e2;
        System.out.println("+E: " + dvalue);
        dvalue = 0x9.AP0;
        System.out.println("0P: " + dvalue);
        dvalue = 0x26.8P-2;
        System.out.println("-P: " + dvalue);
        dvalue = 0x2.68P2;
        System.out.println("+P: " + dvalue);

        // boolean
        boolean bvalue = false;
        System.out.println("\nvalue=" + bvalue);
        bvalue = true;
        System.out.println("bvalue=" + bvalue);

        // char
        char cvalue = 'A';
        System.out.println("\ncvalue=" + cvalue);
        cvalue = '\101';
        System.out.println("cvalue=" + cvalue);
        cvalue = '\u0041';
        System.out.println("cvalue=" + cvalue);

        // String
        String svalue = "\u00A1Hasta, ma\u00F1ana!";
        System.out.println("\nsvalue=" + svalue);

        System.out.println();
    }
}
