
object Main {
  def main() = {

      var x = readLine("Enter marks: ");
      var marks = x.toInt;

      if (marks > 90)
      {
          println("Your grade is A");
      }
      else if(marks > 70)
      {
          println("Your grade is B");
      }
      else if(marks > 60)
      {
          println("Your grade is C");
      }
      else if(marks > 50)
      {
        println("Your grade is D");
      }
      else
      {
        println("Your grade is F");
      }
  }
}
