import scala.collection.mutable.Map

object Main {

  def main() = 
  {
      var map = Map[String,String]();
      println(map);
      map += ("A"->"Apple", "B" -> "Ball");
      map += ("C"->"Cat");
      println(map);

      map -= ("C","B");
      println(map);



  }
  

}

