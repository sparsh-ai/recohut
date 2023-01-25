import scala.collection.mutable.ListBuffer

class Data(var item: String,var price: Int,var count: Int)
{

}


object Main {

  def main() = 
  {

    var listBuffer = ListBuffer[Data]();
    var userOption = "";



    do{
        userOption = readLine("1. To Enter new product. \n2. To Quit.")
        if (userOption == "1")
        {
          var item = readLine("Enter Item: ");
          var x = readLine("Enter price: ");
          var price = x.toInt;
          var y = readLine("Enter count: ");
          var count = y.toInt;

          var d = new Data(item,price,count);
          listBuffer += d;
        }



    }
    while(userOption != "2");

    for(w<- listBuffer)
    {
      println(w.item);
    }
    

    
  }
  

}

