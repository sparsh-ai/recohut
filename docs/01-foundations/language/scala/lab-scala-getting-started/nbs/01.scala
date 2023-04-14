// Databricks notebook source
import scala.collection.immutable._
import scala.collection.mutable.ListBuffer
import scala.collection.mutable.Map
import scala.collection.mutable

// COMMAND ----------

1 + 1

// COMMAND ----------

println(1) // 1
println(1 + 1) // 2
println("Hello!") // Hello!
println("Hello," + " world!") // Hello, world!

// COMMAND ----------

val x = 1 + 1
println(x) // 2

// COMMAND ----------

// Values cannot be re-assigned

x = 3 // This does not compile.

// COMMAND ----------

// The type of a value can be omitted and inferred, or it can be explicitly stated

val x: Int = 1 + 1

// COMMAND ----------

var x: Int = 1 + 1
println(x)

// COMMAND ----------

x = 3

// COMMAND ----------

println({
  val x = 1 + 1
  x * x
})

// COMMAND ----------

val addOne = (x: Int) => x + 1
println(addOne(1)) // 2

// COMMAND ----------

val add = (x: Int, y: Int) => x + y
println(add(1, 2)) // 3

// COMMAND ----------

val getTheAnswer = () => 42
println(getTheAnswer()) // 42

// COMMAND ----------

def add(x: Int, y: Int): Int = x + y
println(add(1, 2)) // 3

// COMMAND ----------

def addThenMultiply(x: Int, y: Int)(multiplier: Int): Int = (x + y) * multiplier
println(addThenMultiply(1, 2)(3)) // 9

// COMMAND ----------

for (i <- Range.inclusive(1, 10)) {
  println(
    if (i % 3 == 0 && i % 5 == 0) "FizzBuzz"
    else if (i % 3 == 0) "Fizz"
    else if (i % 5 == 0) "Buzz"
    else i
  )
}

// COMMAND ----------

object Main {
  def main() = {
    var s1: String = "How are you?";
    val s2: String = "I'm fine";
    println(s1.length()+s2.length());
    println(s1.concat(s2));
  }
}

// COMMAND ----------

object Main {
  def main(s1: String, s2: String) = {
    println(s1.length()+s2.length());
    println(s1.concat(s2));
  }
}

// COMMAND ----------

val string1: String = "How are you?";
val string2: String = "I'm fine";

Main.main(string1, string2)

// COMMAND ----------

def main() = {
    var a: Int = 2;
    var b: Int = 4;
    var c: Int = 6;
    var step1: Int = (a+b);
    var step2: Int = step1 / c ;
    var ans: Int = ( (step2) * a);
    println( ans )
}

main()

// COMMAND ----------

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

Main.main()

// COMMAND ----------

object Main {
  def main(x: Int, y: Int) = {
  var num1 = x.toInt;
  var num2 = y.toInt;
  if (num1 > num2)
  {
    println("Number 1 is greater");
  }    
  else
  {
    println("Number 2 is greater");    
  }
  }
}

// COMMAND ----------

Main.main(5, 3)

// COMMAND ----------

Main.main(15, 29)

// COMMAND ----------

object Main {
  def main() = {
      if (1 > 2)
      {
        println("I'm in if 1");
      }
      else if (6 < 2)
      {
        println("I am in else");
      }
      else if (1 < 0)
      {
        println("I am in else 2");
      }
      else 
      {
          print("I am in final else");
      }
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main() = {
    println(1<2);
    println(1>2);
    println(1 <  2 && 1 < 5);
    println(1 >  2 && 1 < 5);
    println(1 >  2 && 1 > 5);
    println(1 < 2 || 1 < 5);
    println(1 > 2 || 1 < 5);
    println(1 < 2 || 1 > 5);
    println(1 > 2 || 1 > 5);
    println( !(1 < 2) );
    println( !(1 > 2) );
    println(!(1 <  2 && 1 < 5));
    println(!(1 > 2 || 1 > 5));
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main(x: Int) = {
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

// COMMAND ----------

Main.main(83)

// COMMAND ----------

object Main {
  def main() = {
    var num = 5;
    while(num > 0)
    {
      println(num);
      num = num - 1; 
    }    
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main(x: Int) = {
    var num = x.toInt;
    var factorial = 1;
    for (w <- 1 to num)
    {
      println(w);
      factorial = factorial * w;
      println(factorial);
      println("---------------------------------")
    }
  println(factorial);
   }
}

// COMMAND ----------

Main.main(4)

// COMMAND ----------

object Main {
  def main() = {
      println(addition(5,6));
      println(addition(2,2));
      println(addition(9,9));
   }

  def addition(a: Int, b: Int) : Int = {
    var sum = a + b;
    return sum;
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main() = {
    var x = "Hello ";
    var y = "World";
    println(concatination(x,y));
  }

  def concatination(str1: String, str2: String) : String= {
    return str1 + str2;
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main() = {
    foo(12,11,33);
  }

  def foo(b: Int, a:Int = 5, c:Int = 12, d:Int = 15) = {
	  println(b);
      println(a);
      println(c);
      println(d);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main() = {
    var inc = (x:Int) => x + 1;  
    var x = inc(4);
    println(x);
    var mul = (x:Int, y:Int) => x*y;
    println(mul(2,4))
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {
  def main() = {
    var add = (x:Int, y:Int) => x + y;
    var sub = (x:Int, y:Int) => x - y;
    var mul = (x:Int, y:Int) => x * y;
    var div = (x:Int, y:Int) => x / y;
    var a = 10;
    var b = 20;
    var c = 30;
    var x = add(a,b);
    var y = div(x,c);
    var z = mul(y,a);
    println(z);
    println(mul(div(add(a,b),c),a));
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

class Student{
  var name = "";
  var roll = "";
}


object Main {
  def main() = 
  {
      var s1 = new Student();
      var s2 = new Student();

      s1.name = "Hello";
      s1.roll = "123";
      s2.name = "World";
      s2.roll = "456";

      println(s1.name);
      println(s2.name);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

class Student(var name: String, var roll: String)
{
    var sems = 1;

    def changeSems(): Unit = {
          sems = sems + 1;

    }

    def printData(): Unit = {
      println(name);
      println(roll);
      println(sems);
    }
}

object Main {
  def main() = 
  {
     var s1 = new Student("John","123");
     var s2 = new Student("Alica","124");
    
     s1.sems = 3;
     s1.printData();
     println("---------");
     s2.printData();
    
     println(checkSems(s1,s2));
  }

  def checkSems(s1: Student, s2: Student): String =
  {
        if(s1.sems > s2.sems)
        {
          return s1.name;
        }
        else
        {
          return s2.name;
        }
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {

    val list = List(1,2,3,"Hello", "World");

    println(list(0));
    println(list(4));
    println("------------------------")

    for(w<- list)
    {
      println(w);
    }

  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
      val list = List(List(1,2,3), List(4,5,6), List(22,33,12));

      println(list);

      var l2 =  12 +: list
      var l3 =  list :+ 13 

      println(l2);
      println(l3);

  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {

    var list = List(1,2,3,4,5,6,7);
    var l2 = list.take(3);
    for(w<- l2)
    {
      println(w);
    }
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {

    var list = List(1,2,3);
    println(list);

    list += 4;
    println(list);
    
    0 +=: list;
    println(list);
  }
}

// COMMAND ----------

object Main {

  def main() = 
  {

    var listBuffer = ListBuffer(1,2,3);
    println(listBuffer);

    listBuffer += 4;
    println(listBuffer);
    
    0 +=: listBuffer;
    println(listBuffer);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
    var listBuffer = ListBuffer(1,2,3,4);
    println(listBuffer);

    listBuffer -= (3);
    println(listBuffer);

    listBuffer.remove(1);
    println(listBuffer);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
    var m = Map("A" -> "Apple", "B" -> "Ball", "C"->"Cat");
    println(m);
    println(m("A"));
    println(m("B"));
    println(m("C"));

  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
    var map = Map("A"->"Apple", "B"->"Ball");

    if(map.contains("A"))
    {
      println("A is in the map");
    }
    if(map.contains("C"))
    {
      println("C is in the map");
    }
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
    var map = Map("A"->"Apple", "B"->"Ball","C"->"Cat")

    println(map);

    map("A") = "Banana";
    map("B") = "Bat";

    println(map);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
      var map = Map[String,String]();
      println(map);
      map += ("A"->"Apple", "B" -> "Ball");
      map += ("C"->"Cat");
      println(map);

      map -= ("C","B");
      println(map);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
      var s = Set(1,2,3,4,1,2,3,4,1,2)
      println(s);
  }
}

// COMMAND ----------

Main.main()

// COMMAND ----------

object Main {

  def main() = 
  {
      var s = Set[Int]();

      s += 1;
      s += 2;
      s += 1;
      s += 3;
      println(s);

      s -= 1;
      s -= 4;
      println(s);
  }
}

// COMMAND ----------

Main.main()
