
object Main {
  def main() = {
    
    var s1 = "123";
    println(s1.getClass.getName);
    var s2 = s1.toInt;
    println(s2.getClass.getName);


    var i1 = 12;
    var i2 = 6.0F;
    

    println(i1.getClass.getName);
    println(i2.getClass.getName);

    var i3 = i1.asInstanceOf[Float];
    var i4 = i2.asInstanceOf[Int];

    println(i3.getClass.getName);
    println(i4.getClass.getName);













      
  }
}
