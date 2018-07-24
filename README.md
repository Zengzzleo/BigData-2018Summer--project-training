# BigData-2018Summer--project-training
>about python,scale,echart...
##项目列表
*1 天气预报 采用python
*2 淘宝数据爬取 采用python+urlibs
*3 全国高校数据爬取 采用python
*4 全国数据进行清理 采用scala+spark
*5 数据可视化        采用Echart
>代码示例
'
 sc.textFile("F:\\shixun\\我们组招生计划.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
'
