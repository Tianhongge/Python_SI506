#In class notes(Week02) 20220111

##查找当前工作空间

```bash
pwd
```

##更改路径
```bash
cd '完整路径/下一级文件夹的名字'
```

###返回当前用户最上级位置
```bash
cd ~
```

###返回上一级位置
```bash
cd ../
```

##搜索当前位置所有文件
```bash
ls -la
```

##创建文件夹
```bash
mkdir '文件夹名称'
```

##删除文件夹
```bash
rmdir '文件夹名称'
```

##复制文件夹至某位置
```bash
cp 'filename' 'path'
```

###e.g.
```bash
cp scratch.py ../Documents/umich/courses/SI506/lectures/lecture_02
```

###复制文件夹中某一类型所有的文件至某位置
```bash
cp *.md ../Documents/umich/courses/SI506/lectures/lecture_02
```