import scala.collection.mutable.Map

object Main {

  def main() = 
  {
    var m = Map("A" -> "Apple", "B" -> "Ball", "C"->"Cat");
    println(m);
    println(m("A"));
    println(m("B"));
    println(m("C"));

  }
  

}

