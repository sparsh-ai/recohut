import scala.collection.immutable._



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

