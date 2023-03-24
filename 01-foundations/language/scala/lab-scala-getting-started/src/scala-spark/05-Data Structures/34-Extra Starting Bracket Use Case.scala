import scala.collection.mutable.Stack
import scala.util.control.Breaks._

object Main {

  def main() = 
  {
    var stack = Stack[Char]();
    var str = "(5+2)(5*2)((12+2)/(22/33+(22-3)))";
    var validation = "valid";


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
              validation = "invalid";
              break;
            }
            else
            {
              stack.pop();
            }
          }
        }
    }

    if (validation == "valid")
    {
      if(!stack.isEmpty)
      {
        println("Equation is invalid");
      }
      else
      {
        println("Equation is valid");
      }
    }




  }
  

}

