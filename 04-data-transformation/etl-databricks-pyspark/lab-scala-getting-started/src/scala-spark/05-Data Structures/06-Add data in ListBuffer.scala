import scala.collection.mutable.ListBuffer

object Main {

  def main() = 
  {

    var listBuffer = ListBuffer(1,2,3);
    println(listBuffer);

    listBuffer += 4;
    println(listBuffer);


    0 +=: listBuffer;
    println(listBuffer);


  }

}

