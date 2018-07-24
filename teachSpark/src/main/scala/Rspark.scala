import scala.collection.mutable.ListBuffer

/**
  * Created by 10257 on 2018/7/24.
  */
object Rspark {
  def main(args: Array[String]) {
    import org.json.JSONObject
    import org.apache.spark.SparkConf
    import org.apache.spark.SparkContext
    //sparkcontext的配置，运行在本地，名为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf)
    //使用spark读取文本文件
    sc.textFile("F:\\shixun\\我们组招生计划.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))

  }
}
