
object Main {
  def main() = {
   
    var x = readLine("Enter number 1: ");
    var num1 = x.toInt;

    if (num1 > 10)
    {

      var y = readLine("Enter number 2: ");
      var num2 = y.toInt;
      if (num2 == 5)
      {
        println(num1 + num2);
      }
      else
      {
        println("Number is not 5");
      }
    }
    else
    {
      println("Your entered number is not greater then 10");

    }


  }
}
