import scala.util.control.Breaks._
import scala.util.Random

object Main {
  def main() = {
    

    var X = Random.nextInt(101);

    var gameStatus = "Lost";


    breakable
    {
    
        for(w<- 1 to 5)
        {
          var x = readLine("Enter your guess: ");
          var guess = x.toInt;

          if(guess < X)
          {
            println("Your guess is less than the actual number.");
            println(5-w);
          }
          else if (guess > X)
          {
            println("Your guess is greater than the actual number.");
            println(5-w);
          }
          else
          {
            println("You won.");
            println(w);
            gameStatus = "Won";
            break;

          }
        }



    }

    if (gameStatus == "Lost")
    {
      println(X);
      println("You lost the game");
    }


        
   }
}
