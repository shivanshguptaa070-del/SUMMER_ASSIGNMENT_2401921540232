package live;

import music.Playable;
import music.string.Veena;
import music.wind.Saxophone;

public class Test {
    public static void main(String[] args) {

        // a. Create Veena object
        Veena v = new Veena();
        v.play();

        // b. Create Saxophone object
        Saxophone s = new Saxophone();
        s.play();

        // c. Polymorphism using Playable reference
        Playable p;

        p = v;
        p.play();

        p = s;
        p.play();
    }
}