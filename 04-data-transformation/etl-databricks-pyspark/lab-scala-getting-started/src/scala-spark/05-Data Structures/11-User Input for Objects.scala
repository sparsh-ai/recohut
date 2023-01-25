import scala.collection.mutable.ListBuffer

class Data(var item: String,var price: Int,var count: Int)
{

}


object Main {

  def main() = 
  {

    var listBuffer = ListBuffer[Data]();


    var item = readLine("Enter Item: ");
    var x = readLine("Enter price: ");
    var price = x.toInt;
    var y = readLine("Enter count: ");
    var count = y.toInt;
    


    var d = new Data(item,price,count);
    listBuffer += d;

    
  
    for(w<- listBuffer)
    {
      println(w.item);
    }
    

    
  }
  

}

