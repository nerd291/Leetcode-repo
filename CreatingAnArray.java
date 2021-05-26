//List
DVD[] dvdCollection = new DVD[15];

//def for a DVD
public class DVD{
    public String name;
    public int releaseYear;
    public String director;

    public DVD(String name, int releaseYear, String director){
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;

    }

    public String toString(){
        System.out.println(
            this.name + ", directed by " + this.director + ", released in " + this.releaseYear));
    }
}