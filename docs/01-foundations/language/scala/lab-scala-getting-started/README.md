# Getting Started with Scala

### Why Scala?

- Expressive
  - First-class functions
  - Closures
- Concise
  - Type inference
  - Literal syntax for function creation
- Java interoperability
  - Can reuse java libraries
  - Can reuse java tools
  - No performance penalty

### How Scala?

- Compiles to java bytecode
- Works with any standard JVM
  - Or even some non-standard JVMs like Dalvik
  - Scala compiler written by author of Java compiler

### How to install

```
pip install spylon-kernel
python -m spylon_kernel install
```

To install scala in Anaconda, first create an empty venv (`env-scala` in our case) and then install the scala from `anaconda-cluster` channel.

```
conda create -n env-scala
conda install -c anaconda-cluster scala
conda install -c conda-forge spylon-kernel
```

```
├── [ 799]  README.md
├── [ 157]  data
│   └── [  61]  download.sh
├── [ 21K]  nbs
│   ├── [ 10K]  01.scala
│   ├── [4.3K]  02.scala
│   └── [6.7K]  03.scala
└── [ 39K]  src
    └── [ 39K]  scala-spark
        ├── [2.0K]  01-Overview
        │   ├── [ 246]  06-Strings\ Basics.scala
        │   ├── [ 251]  08-Solution\ (Arithmatic\ Operations).scala
        │   ├── [ 310]  10-Solution\ (Strings).scala
        │   ├── [ 466]  11-Type\ Casting.scala
        │   ├── [ 278]  12-Taking\ input\ from\ User.scala
        │   └── [ 239]  14-Solution\ (User\ Input\ and\ Type\ Casting).scala
        ├── [ 11K]  02-Control\ Statements
        │   ├── [ 373]  11-Solution\ (Logical\ operators).scala
        │   ├── [ 346]  12-If\ else\ if.scala
        │   ├── [ 514]  14-Solution(if\ else\ if).scala
        │   ├── [ 157]  16-Overview\ of\ While\ Loop.scala
        │   ├── [ 287]  17-While\ Loop.scala
        │   ├── [ 418]  19-Solution\ 1\ (while\ loop).scala
        │   ├── [ 309]  2-If\ else\ statements.scala
        │   ├── [ 558]  20-Solution\ 2\ (while\ loop).scala
        │   ├── [ 469]  21-Do\ While\ Loop.scala
        │   ├── [ 322]  22-For\ Loop.scala
        │   ├── [ 341]  24-Solution\ (For\ Loop).scala
        │   ├── [ 584]  26-Solution(For\ Loop).scala
        │   ├── [ 432]  27-Break.scala
        │   ├── [ 481]  28-Break\ Fix.scala
        │   ├── [ 408]  3-Conditions\ in\ If.scala
        │   ├── [ 541]  30-Project\ Solution\ Code\ 1.scala
        │   ├── [ 714]  31-Project\ Solution\ Code\ 2.scala
        │   ├── [ 861]  32-Project\ Solution\ Code\ 3.scala
        │   ├── [ 931]  33-Project\ Solution\ Code\ 4.scala
        │   ├── [ 321]  5-Solution\ (if\ statement).scala
        │   ├── [ 456]  6-Nested\ if\ else.scala
        │   ├── [ 488]  8-Solution\ (nested\ if\ else).scala
        │   └── [ 438]  9-Logical\ operators.scala
        ├── [ 12K]  03-Functions
        │   ├── [ 253]  02-Writing\ addition\ function.scala
        │   ├── [ 371]  04-Solution\ (Basic\ Function).scala
        │   ├── [ 246]  06-Strings\ basics.scala
        │   ├── [ 227]  08-Solution\ (String\ Concatination\ Function).scala
        │   ├── [ 617]  10-Solution\ (Dividing\ Code\ in\ Functions).scala
        │   ├── [ 232]  11-Default\ Arguments.scala
        │   ├── [ 969]  13-Solution(Default\ Arguments).scala
        │   ├── [ 194]  14-Anonymous\ Functions.scala
        │   ├── [ 414]  16-Solution(Anonymous\ Functions).scala
        │   ├── [ 332]  17-Scopes.scala
        │   ├── [ 631]  19-\ Project\ Structure.scala
        │   ├── [1.1K]  20-Prompting\ the\ menu.scala
        │   ├── [1.8K]  21-Baisc\ Functions.scala
        │   ├── [2.3K]  22-Breaking\ code\ in\ more\ functions.scala
        │   └── [2.3K]  23-Final\ Run.scala
        ├── [2.4K]  04-Classes
        │   ├── [ 334]  02-Creating\ Class.scala
        │   ├── [ 252]  03-Class\ Constructor.scala
        │   ├── [ 751]  04-Functions\ and\ Classes.scala
        │   ├── [ 318]  06-Basic\ Strucuture.scala
        │   └── [ 537]  07-FInal\ Run.scala
        └── [ 11K]  05-Data\ Structures
            ├── [ 301]  02-Lists\ introduction.scala
            ├── [ 319]  03-Lists\ Create\ and\ Delete\ Elements.scala
            ├── [ 219]  04-Lists\ Take.scala
            ├── [ 297]  05-ListBuffer\ Introduction.scala
            ├── [ 273]  06-Add\ data\ in\ ListBuffer.scala
            ├── [ 284]  07-Remove\ data\ from\ ListBuffer.scala
            ├── [ 253]  08-Take\ data\ from\ ListBuffer.scala
            ├── [ 373]  10-Project\ Architecture\ Implementation.scala
            ├── [ 557]  11-User\ Input\ for\ Objects.scala
            ├── [ 789]  12-Implementing\ the\ control\ flow.scala
            ├── [1.0K]  13-Creating\ Required\ Functions\ inside\ Class.scala
            ├── [ 240]  15-Creating\ Maps.scala
            ├── [ 299]  16-Check\ Key\ in\ Map.scala
            ├── [ 246]  17-Update\ Value\ in\ Map.scala
            ├── [ 302]  18-Add\ and\ Remove\ items\ from\ Maps.scala
            ├── [ 262]  19-Iterating\ on\ Maps.scala
            ├── [ 409]  22-Project\ Structure\ Code.scala
            ├── [ 507]  23-Using\ Maps\ for\ word\ count.scala
            ├── [ 768]  24-Final\ Run.scala
            ├── [ 151]  25-Sets\ Overview.scala
            ├── [ 255]  26-Add\ and\ Remove\ Item\ from\ the\ Set.scala
            ├── [ 400]  29-Push\ and\ Pop\ in\ Stack.scala
            ├── [ 467]  30-Stack\ Attributes.scala
            ├── [ 535]  33-Project\ Architecture\ Code.scala
            └── [ 912]  34-Extra\ Starting\ Bracket\ Use\ Case.scala

  62K used in 9 directories, 79 files
```