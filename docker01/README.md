### 天池大赛【入门】Docker练习场

##### 拉取镜像
~~~
# 拉取基础镜像
docker pull registry.cn-shanghai.aliyuncs.com/tcc-public/python:3
~~~

##### 编辑Docker镜像相关文件
Dockerfile  main.py  result.json  run.sh  tcdata/num_list.csv

##### 打包镜像并提交
~~~
#登录阿里云Docker Registry
sudo docker login --username=zhix****@gmail.com registry.cn-shenzhen.aliyuncs.com
​
#打包镜像
sudo docker build -t registry.cn-shenzhen.aliyuncs.com/***/dockerlearn01:0.11 .
​
#执行任务
sudo docker run imageId sh run.sh
​
#上传镜像
sudo docker push registry.cn-shenzhen.aliyuncs.com/***/dockerlearn01:0.11
~~~

完成后提交结果即可