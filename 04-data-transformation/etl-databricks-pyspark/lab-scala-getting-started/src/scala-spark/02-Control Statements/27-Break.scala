import scala.util.control.Breaks._

object Main {
  def main() = {

      var sum = 0;

      for(w<- 1 to 5)
      {
        var x = readLine("Enter number: ");
        var num = x.toInt;

        if(num == 0)
        {
          println("About to break");
          break;
        }



        sum = sum + num;
        println(sum);
      }
      
      println("Out of for loop");


        
   }
}
