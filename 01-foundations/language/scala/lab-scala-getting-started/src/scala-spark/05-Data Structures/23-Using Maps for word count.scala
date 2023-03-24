import scala.collection.mutable.Map

object Main {

  def main() = 
  {
    var map = Map[String,Int]()
    var x = readLine("How many words you want to enter: ");
    var totalWords = x.toInt;

    for(w <- 1 to totalWords)
    {
      var word = readLine("Enter word: ");

      if (map.contains(word))
      {
        map(word) = map(word) + 1
        println(map);
      }
      else
      {
        map += (word -> 1);
        println(map);
      }

    }


  }
  

}

