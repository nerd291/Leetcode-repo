public class DVD {

    DVD[] dvdCollection = new DVD[15];
    public String name;
    public int releaseYear;
    public String director;

    public static void main(String args[]){
        System.out.println(DVD());
    }

    public DVD(String name, int releaseYear, String director) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;
    }

    public String string() {
        System.out.println(
            this.name + ", directed by " + this.director + ", released in " + this.releaseYear);
        return null;
    }
}