import scala.collection.mutable.ListBuffer

object Main {

  def main() = 
  {
    var listBuffer = ListBuffer(1,2,3,4,5,6);
    var newListBuffer = listBuffer.take(4);
    for(w<- newListBuffer)
    {
      println(w);
    }   
  }

}

