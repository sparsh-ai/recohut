
object Main {
  def main() = {

    var x = readLine("Enter number: ");
    var num = x.toInt;

    var factorial = 1;

    for (w <- 1 to num)
    {
      println(w);
      factorial = factorial * w;
      println(factorial);

      println("---------------------------------")


    }
  println(factorial);

   }
}
