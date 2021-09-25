package ch02;

public class Literals {
    private final static int [] IVALUES = {
            0b01100100,
            0144,
            100,
            0x64,
            1_000_000
    };

    public static void main(String [] args) {
        for (int i: IVALUES) {
            System.out.println(i);
        }
    }
}
