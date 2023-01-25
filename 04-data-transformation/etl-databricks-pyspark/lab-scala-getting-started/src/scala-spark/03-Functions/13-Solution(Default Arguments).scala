
object Main {

  def main() = {
    var totalBill = get_bill_amount();
    var totalDiscount = get_discount_amount();
    var totalDiscountedBill = 0;

    if(totalDiscount == 0 )
    {
      totalDiscountedBill = apply_discount(totalBill);
    }
    else
    {
      totalDiscountedBill = apply_discount(totalBill,totalDiscount);
    }
    print_bill(totalDiscountedBill,totalBill);



  
  }

  def print_bill(discountedBill: Int, totalBill: Int): Unit ={
      println(totalBill);
      println(discountedBill);
  }


  def apply_discount(totalBill: Int, totalDiscount: Int = 10): Int = {
    var total = totalBill - totalDiscount;
    return total;
  }

  def get_bill_amount(): Int ={
    var x = readLine("Enter total bill: ");
    var num = x.toInt;
    return num;
  }

  def get_discount_amount(): Int ={
    var x = readLine("Enter total discount: ");
    var num = x.toInt;
    return num;
  }



 


}

