import scala.collection.mutable.ListBuffer

class Data(var item: String,var price: Int,var count: Int)
{

}


object Main {

  def main() = 
  {
    var d1 = new Data("Bags",100,5);
    var d2 = new Data("Mats",10,15);
    
    var listBuffer = ListBuffer(d1,d2);

    for(w<- listBuffer)
    {
      print(w.item);
    }
    

    
  }
  

}

