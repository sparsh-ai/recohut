import scala.collection.immutable._



object Main {

  def main() = 
  {
      val list = List(List(1,2,3), List(4,5,6), List(22,33,12));

      println(list);

      var l2 =  12 +: list
      var l3 =  list :+ 13 

      println(list);


      println(l2);
      println(l3);




  }

}

