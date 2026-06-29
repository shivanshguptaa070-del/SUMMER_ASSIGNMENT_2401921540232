interface test {
    int square(int x);
}

class Arithmetic implements test {
    public int square(int x) {
        return x * x;
    }
}

class Outer {
    void display() {
        System.out.println("Outer class display");
    }

    class Inner {
        void display() {
            System.out.println("Inner class display");
        }
    }
}

class Point {
    private int x, y;

    Point() {
        x = 0;
        y = 0;
    }

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    void setX(int x) {
        this.x = x;
    }

    void setY(int y) {
        this.y = y;
    }

    void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    void show() {
        System.out.println("X = " + x + " Y = " + y);
    }
}

class Box {
    int l, b;

    Box(int l, int b) {
        this.l = l;
        this.b = b;
    }

    int area() {
        return l * b;
    }
}

class Box3D extends Box {
    int h;

    Box3D(int l, int b, int h) {
        super(l, b);
        this.h = h;
    }

    int volume() {
        return l * b * h;
    }
}

public class Main {
    public static void main(String[] args) {

        // Q1 Interface
        Arithmetic a = new Arithmetic();
        System.out.println("Square = " + a.square(5));

        // Q2 Outer and Inner class
        Outer o = new Outer();
        o.display();

        Outer.Inner i = o.new Inner();
        i.display();

        // Q3 Point class
        Point p = new Point();
        p.show();

        p.setXY(10, 20);
        p.show();

        // Q4 Box and Box3D
        Box b1 = new Box(5, 4);
        System.out.println("Area = " + b1.area());

        Box3D b2 = new Box3D(5, 4, 3);
        System.out.println("Volume = " + b2.volume());
    }
}