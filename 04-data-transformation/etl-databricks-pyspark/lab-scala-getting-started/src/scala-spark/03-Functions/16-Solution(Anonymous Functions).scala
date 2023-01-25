
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

