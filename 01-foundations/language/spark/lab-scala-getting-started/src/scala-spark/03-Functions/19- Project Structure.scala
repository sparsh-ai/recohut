
object Main {

  def main() = 
  {
    var cardNumber = 12345;
    var pin = 1234;

    var status = "Failed";


    for(w<- 1 to 3)
    {
      var x = readLine("Enter card number: ");
      var userCardNumber = x.toInt;

      var y = readLine("Enter pin: ");
      var userPin = y.toInt;

      if(userCardNumber == cardNumber && userPin == pin)
      {
        status = "Passed";
        println("Valid infromation, Welcome to ATM");
      }
      else
      {
        println("Invalid information, Try again.");
      }
    } 


    if (status == "Passed")
    {


    }
    
  }

}

