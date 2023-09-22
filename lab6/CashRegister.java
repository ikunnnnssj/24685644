import java.text.*;

/**
 * The cash register stores cash.
 *
 * You can add cash to the cash register.
 */
public class CashRegister {
    private double cash;

    public CashRegister(double cash) {
        this.cash = cash;
    }

    // insert 1 method here
    public void add(double amount){
        cash += amount;
    }


    /**
     * Return a string in the form:
     *
     * Cash register: $[cash]
     *
     * e.g. "Cash register: $29.90"
     *
     * If there is no cash, instead return:
     *
     * "Cash register: empty"
     */
    @Override
    public String toString() {
        String s = "Cash register: ";
        if(cash == 0){
            return s + "empty";
        }
        else
            return s + "$" + formatted(cash);
    }

    private String formatted(double value){
        return new DecimalFormat("###,##0.00").format(value);
    }
}
