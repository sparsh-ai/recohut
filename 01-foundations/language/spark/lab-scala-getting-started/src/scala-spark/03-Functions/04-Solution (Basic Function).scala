
object Main {

  def main() = {

      var x = readLine("Enter number 1: ");
      var num1 = x.toInt;

      var y = readLine("Enter number 2: ");
      var num2 = y.toInt;

      println(greater(num1));
   }

   def greater(a: Int, b:Int) : Int ={
     if (a > b)
     {
       return a;
     }
    else
    {
      return b;
    }

   }

}
