package cn

    /**
      * Created by 10257 on 2018/7/20.
      */
    //需要一个main函数
    //
    object add{
      def addInt( a:Int, b:Int ) : Unit = {
        var sum:Int = 0
        sum = a + b

        println(sum)
      }
      def abc(a:Int,b:Int,opt:String="+"){
        println(opt)
        a+b
      }

  def main(args: Array[String]) {
    addInt(3,2)
    val jia = (a:Int,b:Int)=>a+b
    print("lambd函数:"+jia(3,1))
    abc(3,4)
    abc(3,4,"-")
    1.to(10).map(i=>i*10).foreach(i=>println(i))

  }
}

