import scala.collection.mutable.ListBuffer

class Data(var item: String,var price: Int,var count: Int)
{
    def printData(): Unit = {
      println(item);
      println(price);
      println(count);

    }

    def total() : Int = {

        return price * count;

    }
}


object Main {

  def main() = 
  {

    var listBuffer = ListBuffer[Data]();
    var userOption = "";
    var totalBill = 0;



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
        w.printData();
        totalBill += w.total();
    }
    println(totalBill);
    

    
  }
  

}

