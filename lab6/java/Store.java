/**
 * The store has and sells one product: Sticky tape.
 *
 * You can sell and restock a product, view stock and view cash.
 */
public class Store {
    // insert main method here
    public static void main(String[] args){
        Store s = new Store();
        s.use();

    }

    // insert 2 fields here
    private CashRegister money;
    private Product stickyTape;


    // insert 1 constructor here
    public Store(){
        money = new CashRegister(0);
        stickyTape = new Product("Sticky tape", 200, 2.99);
    }

    public char readChoice(){
        System.out.print("Choice (s/r/v/c/x): ");
        return In.nextChar();
    }

    public void use() {

        char choice;
        while((choice = readChoice()) != 'x'){
           switch(choice){
               case 's': sell(); break;
               case 'r': restock(); break;
               case 'v': viewStock(); break;
               case 'c': viewCash(); break;
               default: help(); break;
           }

       }

       System.out.println("Done");
    }

    private int readNumber(){
        System.out.print("Number: ");
        return In.nextInt();
    }

    private void sell() {
        int amount = readNumber();
        double total = 0;
        if(stickyTape.has(amount)){ 
            total = stickyTape.sell(amount);
            money.add(total);
        }
        else{
            System.out.println("Not enough stock");
        }
        
    }

    private void restock() {
        int amount = readNumber();
        stickyTape.restock(amount);
    }

    private void viewStock() {
        System.out.println(stickyTape);
    }

    private void viewCash() {
        System.out.println(money);
    }

    private void help() {
        System.out.println("Menu options");
        System.out.println("s = sell");
        System.out.println("r = restock");
        System.out.println("v = view stock");
        System.out.println("c = view cash");
        System.out.println("x = exit");
    }


}
