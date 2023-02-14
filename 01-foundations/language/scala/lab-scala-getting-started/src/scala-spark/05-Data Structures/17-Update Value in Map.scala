import scala.collection.mutable.Map

object Main {

  def main() = 
  {
    var map = Map("A"->"Apple", "B"->"Ball","C"->"Cat")

    println(map);

    map("A") = "Banana";
    map("B") = "Bat";

    println(map);

  }
  

}

