
object Main {
  def main() = {

    var x = readLine("Enter marks: ");
    var marks = x.toInt;



    while(marks < 0 || marks > 100)
    {
      x = readLine("Enter marks: ");
      marks = x.toInt;
    }

    if (marks > 90)
    {
      println("A grade");
    }
    else if(marks > 70)
    {
      println("B grade");
    }
    else if(marks > 60)
    {
      println("C grade");
    }
    else if(marks > 50)
    {
      println("D grade");
    }
    else
    {
      println("F grade");
    }



 



  }
}
