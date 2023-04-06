# Dirac_data_convert
## 1.运行Extract_T60.py
修改路径
```
config_path = r"D:\YouSonic\extract_t60\Echo_label"
```
以及
```
xlsx_path = r"D:\YouSonic\extract_t60\Echo_label\{}\新建 Microsoft Office Excel 工作表.xlsx".format(lst_name)
```
## 2.手动修改一下生成的模板的错误
错误的：

![image](https://user-images.githubusercontent.com/61625754/230377421-249f0d40-0c41-4ec9-9b5f-4246d801cfc3.png)
正确的（这个正确的参数从原始csv里面看）

![image](https://user-images.githubusercontent.com/61625754/230377554-5003c595-64d9-4291-a84c-74277243db9b.png)
只需要修改这一个地方就行。
每个生成的csv都改一下这个地方。
这是代码的bug，有空也可以修修。

## 3.运行csv_standard.py
修改参数,把total_csv.csv换成moban.csv就行
```
path = "D:/YouSonic/extract_t60/Finished_File"

total_csv = pd.read_csv("D:/YouSonic/extract_t60/total_csv.csv")
```
