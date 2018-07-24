package cn


/**
  * Created by 10257 on 2018/7/20.
  */
object HelloScala {
  def main(args: Array[String]) {
    println("hello scala,hello world!") //第一次测试
    System.out.println("a\nb")
    var a = 3 //Int
    var b = 3.14d //Float
    var c = 3.14f //单精度
    var d = true //Boolean
    var e = "Scala" //string
    var f = Array(1, 2, 3, 4, 5)
    var g = Array[Int](1, 2, 3, 4, 11)
    println(a + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g + "\n")
    var h = Tuple1(1, 2)
    println("元组h的第一个数据:" + h._1)
    val m = List[String]("加油", "努力", "学习")
    println(m + "\n" + m(2))
    print("今天天气温度%s".format(38))
    weather()
    val gg= for (i <-Range(0,10)) yield i*10
    println(gg)

  }
  def weather(){
    var temp = List(11,22,33,44,55,66,77)
    for (i <- Range(1,8) if (i==3)){
      println(temp(i+1))
    }

  }
}



