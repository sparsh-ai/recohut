import scala.collection.mutable.ListBuffer

object Main {

  def main() = 
  {
    var listBuffer = ListBuffer(1,2,3,4);
    println(listBuffer);

    listBuffer -= (3);
    println(listBuffer);

    listBuffer.remove(1);
    println(listBuffer);



   
  }

}

