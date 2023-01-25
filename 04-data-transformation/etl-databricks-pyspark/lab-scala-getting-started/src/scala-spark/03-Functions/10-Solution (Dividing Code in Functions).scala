
object Main {

  def main() = {

    var num = take_input();
    var factorial = calculate_factorial(num);
    show_results(num,factorial);

    
  }

  def show_results(num: Int, factorial: Int) : Unit ={
    println("Your output is: ");
    println(num);
    println(factorial)

  }

  def calculate_factorial(num: Int) : Int = {

    var factorial = 1;

    for(w<- 1 to num)
    {
      factorial = factorial * w;
    }

    return factorial;



  }

  def take_input() : Int = {
    var x = readLine("Enter number: ");
    var num = x.toInt;
    return num;
  }
 

}

