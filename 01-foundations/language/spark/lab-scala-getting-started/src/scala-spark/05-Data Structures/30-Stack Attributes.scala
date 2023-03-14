import scala.collection.mutable.Stack

object Main {

  def main() = 
  {
   var stack = Stack(1,2,3,4,5,6);
   println(stack);

   println(stack.top);
   println(stack.top);
   println(stack.top);
   println("--------------");
   println(stack.pop());
   println(stack.top);


   println(stack.size);

   if(stack.isEmpty)
   {
     println("Stack is empty");
   }
   else
   {
     println("Stack is not empty");
   }


  }
  

}

