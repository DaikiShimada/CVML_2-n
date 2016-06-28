# 第2部 コンピュータビジョン (Computer Vision)

画像の扱い方，画像から情報を取り出す手法の基礎練習問題です．  
本章は，一般的な画像ライブラリを用いることでスムーズにすすめることが出来ます．  
以下に主な画像ライブラリを挙げておきます．  
- [Pillow](http://python-pillow.org/)
    - Python
- [scikit-image](http://scikit-image.org/)
    - Python
- [OpenCV](http://opencv.org/)
    - C/C++, Python, Java
- [dlib](http://dlib.net/)
    - C++, Python


1. [画像の入出力と保存形式・色空間](#io_color)
2. [画像の変形と色の変換](#transformation)
3. [フィルタリング](#filtering)
4. 画像の周波数表現とその処理
5. 画像記述子とその応用

## <a name ="io_color">[第1章 画像の入出力と保存形式・色空間](1_io_color/io_color.md)
プログラムで画像を読み込む方法，保存する方法，またその形式による違い，色空間に関する練習問題です．  
- [画像の読み込み](1_io_color/io_color.md#imread)
- [画像の書き出し](1_io_color/io_color.md#imsave)
- [グレースケール画像を作る](1_io_color/io_color.md#gray)
- [ヒストグラムを作る](1_io_color/io_color.md#hist)
- [HSV色空間](1_io_color/io_color.md#hsv)

__キーワード: JPEG, BMP, PNG, RGB, HSV, ヒストグラム, Pillow, scikit-image, OpenCV, dlib__

## <a name ="transformation">[第2章 画像の変形と色の変換](2_transformation/transformation.md)
画像を変形する方法，画像内の色を変換する方法に関する練習問題です．  
- [画像の拡大縮小](2_transformation/transformation.md#resize)
- [画像の回転](2_transformation/transformation.md#rotation)
- [ガンマ補正](2_transformation/transformation.md#gamma)
- [2値化](2_transformation/transformation.md#binalization)
- [ヒストグラム均等化](2_transformation/transformation.md#histeq)
- [疑似カラー](2_transformation/transformation.md#pseudo)

__キーワード: アフィン変換, リサイズ, 回転, ガンマ補正, 2値化, ヒストグラム均等化, 擬似カラー__

## <a name ="filtering">[第3章 フィルタリング](3_filtering/filtering.md)
フィルタリングによって画像から情報を取り出す方法に関する練習問題です．  
- [2-3-1 エッジ検出](3_filtering/filtering.md#edge)
- [2-3-2 ボケて](3_filtering/filtering.md#blur)  
- [2-3-3 ボケをなおして](3_filtering/filtering.md#unsharp)
- [2-3-4 ノイズを載せて，除いて](3_filtering/filtering.md#noise)
- [2-3-5 モルフォルジー](3_filtering/filtering.md#morphology)
- [2-3-6 太文字](3_filtering/filtering.md#thinning)
__キーワード: 輪郭抽出, ブラー, アンシャープマスク, ノイズ除去, 細線化__
