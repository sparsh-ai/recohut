
object Main {
  def main() = {
   
    
    println(1<2);
    println(1>2);


    println(1 <  2 && 1 < 5);
    println(1 >  2 && 1 < 5);
    println(1 >  2 && 1 > 5);


    println(1 < 2 || 1 < 5);
    println(1 > 2 || 1 < 5);
    println(1 < 2 || 1 > 5);
    println(1 > 2 || 1 > 5);


    println( !(1 < 2) );
    println( !(1 > 2) );
    println(!(1 <  2 && 1 < 5));
    println(!(1 > 2 || 1 > 5));

  }
}
