import scala.collection.mutable.Map

object Main {

  def main() = 
  {

    var map = Map("A"->"Apple","B"->"Ball");

    for((k,v) <- map)
    {
      println(k);
      println(v);
      println("-----------------");

    }


  }
  

}

