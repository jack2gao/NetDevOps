# git


git是一个应用最广泛的分布式版本管理的工具，能够实现版本修改控制，多人协作，线上线下协同。
所以在无论是学习记录，还是程序开发，都首先安装使用git工具，同时实现代码和记录同步github/gitee。

以下是对git的基本的使用方法，详细的内容可以参考：

[廖雪峰git教程](https://www.liaoxuefeng.com/wiki/896043488029600)

[菜鸟git教程](https://www.runoob.com/git/git-tutorial.html)

# Git 基础使用

## 安装
[GIT download](https://git-scm.com/downloads)

1. 下载git后，step的方式进行安装。

2. 安装完成后，在CMD 下查看是否安装成功：git  

```shell
$ git  version
git version 2.32.0.windows.1
```


3. 注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

```shell
$ git config --list
$ git config --global user.name "Your Name"  
$ git config --global user.email "email@example.com"
```
记录了操作的用户以及邮箱，然后后面在进行git push后就会提示密码账号

## 创建版本库
1. 创建一个版本库非常简单，首先，选择一个合适的地方，创建一个空目录：
```shell
$ mkdir learngit
$ cd learngit
$ pwd
/Users/michael/learngit
```
2. 通过git init命令把这个目录变成Git可以管理的仓库：
```shell
$ git init
Initialized empty Git repository in /Users/michael/learngit/.git/
```

3. 编写一个readme.txt文件

用命令git add告诉Git，把文件添加到仓库
```shell
$ git add readme.txt

//用命令git commit告诉Git，把文件提交到仓库
$ git commit -m "wrote a readme file"
```
## 查看git信息
我们用git log命令查看：
```shell
$ git log
```
如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数：
```shell
$ git log --pretty=oneline

$ git reset --hard HEAD^
$ git reset --hard 1094a
```
git reflog用来记录你的每一次命令：
```shell
$ git reflog
```

用git status查看一下状态：
```shell
$ git status
git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支。
```
用git diff HEAD -- readme.txt命令可以查看工作区和版本库里面最新版本的区别：
```shell
$ git diff HEAD -- readme.txt 
```

## 丢弃以及恢复
git checkout -- file可以丢弃工作区的修改：
```shell
$ git checkout -- readme.txt
```
把readme.txt文件在工作区的修改全部撤销，这里有两种情况：
一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令

用命令git reset HEAD <file>可以把暂存区的修改撤销掉（unstage），重新放回工作区：
```shell
$ git reset HEAD readme.txt
```

用rm命令删了：
```shell
$ rm test.txt
```
从版本库中删除该文件，那就用命令git rm删掉，并且git commit：
```shell
$ git rm test.txt
```
把误删的文件恢复到最新版本：
```shell
$ git checkout -- test.txt
```

## 上传github等云端

```shell
echo "# 50RPA" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote set-url origin https://gXXXm/cexxxa/50RPA.git
git push -u origin main

```

## 创建分支以及合并管理
创建dev分支，然后切换到dev分支：
```shell
$ git checkout -b dev
Switched to a new branch 'dev'
```
git checkout命令加上-b参数表示创建并切换，相当于以下两条命令：
```shell
$ git branch dev
$ git checkout dev
```
然后，用git branch命令查看当前分支：
```shell
$ git branch
```
dev分支的工作完成，我们就可以切换回master分支：
```shell
$ git checkout master
```
把dev分支的工作成果合并到master分支上：
```shell
$ git merge dev
```

创建并切换到新的dev分支，可以使用：
```shell
$ git switch -c dev
```
直接切换到已有的master分支，可以使用：
```shell
$ git switch master
```

总结：
* 查看分支：git branch
* 创建分支：git branch <name>
* 切换分支：git checkout <name>或者git switch <name>
* 创建+切换分支：git checkout -b <name>或者git switch -c <name>
* 合并某分支到当前分支：git merge <name>
* 删除分支：git branch -d <name>

注意：

* 合并dev分支，请注意--no-ff参数，表示禁用Fast forward：
```shell
$ git merge --no-ff -m "merge with no-ff" dev
```
本次合并要创建一个新的commit，所以加上-m参数，把commit描述写进去。
合并后，我们用git log看看分支历史：
```shell
$ git log --graph --pretty=oneline --abbrev-commit
```
如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。