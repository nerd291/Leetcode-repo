public class ArrayLoop {
    public static void main(String args[]){
        int[] squareNumbers = new int[10];

        for(int i=0;i<10;++i){
            int square = (i+1)*(i+1);
            squareNumbers[i]=square;
            System.out.println(square);
        }
    }
}
