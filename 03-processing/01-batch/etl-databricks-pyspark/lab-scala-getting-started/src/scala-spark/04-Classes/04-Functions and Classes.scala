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

