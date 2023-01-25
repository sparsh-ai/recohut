
object Main {

  def main() = {

    foo(12,11,33);

  
  }


  def foo(b: Int, a:Int = 5, c:Int = 12, d:Int = 15): Unit = {

	  println(b);
	  
      println(a);
      println(c);
      println(d);

  }

}

