# ROSを用いた対話型ドイツ語勉強口座  
今回自作したROSのパッケージを動作させるための説明を以下で行う。  
##  使用した道具  
- raspberry Pi 4 model B  
## 動作環境  
- OS:ubuntu 20.04.1 LTS  
## 導入方法  
`https://github.com/Tqkqhqshi-Yuuki/mypkg.git`  
## 実行方法  
①ubuntuを４つ立ち上げ、４つ共に`cd catkin_ws/src/mypkg/scripts`を行う。  
②１つ目で`roscore`を実行。  
③２つ目で`rosrun mypkg count.py`を実行。  
④３つ目で`rostopic echo /count_up`を実行。  
⑤４つ目で`rosrun mypkg twice.py`を実行。  
⑥`rosrun mypkg count.py`を実行したウィンドウで、画面に表示されている好きなドイツ語を入力。  
⑦入力された言葉によってランダムに返事を表示。  
##  実行結果  
以下は、実際に行った動画である。  
https://youtu.be/RFzvvFlHi4o  
##  ライセンス  
[BSD 3-Clause License](https://github.com/Tqkqhqshi-Yuuki/mypkg/blob/master/LICENSE)
