import scala.collection.mutable.Stack
import scala.util.control.Breaks._

object Main {

  def main() = 
  {
    var stack = Stack[Char]();
    var str = "(5+2))";


    breakable
    {
    for (w<- str)
    {
      if(w == '(')
      {
        stack.push('(');
      }

      if(w == ')')
      {
        if(stack.isEmpty)
        {
          println("Equation is invalid");
          break;
        }
        else
        {
          stack.pop();
        }
      }
    }
    }



  }
  

}

