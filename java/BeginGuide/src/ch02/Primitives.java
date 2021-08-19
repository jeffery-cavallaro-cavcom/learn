package ch02;

public class Primitives {
    private static <T> void show(String name, T min, T max) {
        System.out.println(name + ": min=" + min + " max=" + max);
    }

    public static void main(String [] args) {
        show("byte", Byte.MIN_VALUE, Byte.MAX_VALUE);
        show("short", Short.MIN_VALUE, Short.MAX_VALUE);
        show("int", Integer.MIN_VALUE, Integer.MAX_VALUE);
        show("long", Long.MIN_VALUE, Long.MAX_VALUE);
        System.out.println();
        show("char", (int) Character.MIN_VALUE, (int) Character.MAX_VALUE);
        System.out.println();
        show("float", Float.MIN_VALUE, Float.MAX_VALUE);
        show("double", Double.MIN_VALUE, Double.MAX_VALUE);
        System.out.println();
        System.out.println("boolean: true=" + true + " false=" + false);
    }
}
