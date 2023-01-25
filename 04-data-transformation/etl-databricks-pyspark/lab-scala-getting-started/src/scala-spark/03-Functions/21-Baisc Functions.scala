
object Main {

  var balance = 100;



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
      var input = " ";


      do{
        println("1. To check balance");
        println("2. To withdraw");
        println("3. To deposit");
        println("4. To quit");

        input = readLine("Enter your option.");

        if(input == "1")
        {
          checkBalance();
        }
        else if(input == "2")
        {
          var bal = readLine("Enter amount to withdraw: ");
          var userAmount = bal.toInt;
          withdraw(userAmount);
        }
        else if(input == "3")
        {
          var bal = readLine("Enter amount to deposit: ");
          var userAmount = bal.toInt;
          deposit(userAmount);          
        }

      }
      while(input != "4")

    }

  }

  def deposit(amount: Int): Unit={
    balance = balance + amount;
    checkBalance();

  }

  def withdraw(amount: Int): Unit ={
      if(amount > balance)
      {
        println("Your balance is not enough.");
      }
      else
      {
        println("Your amount has been deducted.");
        balance = balance - amount;
        checkBalance();
      }

  }

  def checkBalance(): Unit = {

    println("Your balance is: ");
    println(balance);

  }



}

