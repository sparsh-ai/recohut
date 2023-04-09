object Main {
  def main() = {
    var s1: String = "abc";
    var s2: String = "de";
    var totalLength: Int =  s1.length() + s2.length();

    println(totalLength);


    var s3: String = s1.concat(s2);
    println(s3);
    println(s3.length());

    println(s1.concat(s2).length())

  }
}
