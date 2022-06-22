public class Powxn {
    public double myPow(double x, int n) {
        if (n==0) {
            return 1.0;
        } else if (n < 0) {
            return 1.0/myPow(x, -n);
        } else {
            double ans = 1;
            double conProduct = x;
            for (int i=n; i>0; i/=2) {
                if (i % 2 == 1) {
                    ans *= conProduct;
                }
                conProduct = conProduct * conProduct;
            }
            return ans;
        }
    }
}
