# Python-Image-Album

## 概要 Description
画像一覧  
Image list  

画像ファイルを選択し、ファイルのサムネイル画像とファイル情報を格子状に一覧表示する   
Select image files and display the thumbnail image of the file and the file information in a grid pattern.  

## 特徴 Features

- GIF、PNG、JPEG、WebP ファイルを読み込み画像のサムネイルを格子状に表示  
	Read GIF, PNG, JPEG, WebP files and display thumbnails of images in a grid pattern  
- 画像のファイル名、サイズ、Exif 情報の有無を表示  
	Show image file name, size, and presence / absence of Exif information  
- 画像を選択して原寸大でプレビューをダイアログ表示  
	Select images and display full-scale preview in dialog
- ドラッグアンドドロップでファイルを指定可能(TkinterDnD2使用)
	File can be specified by drag and drop(using TkinterDnD2)  
- exeにドラッグアンドドロップでファイルを指定可能(TkinterDnD2使用でも)
	File can be specified by dragging and dropping to exe(using TkinterDnD2)  

## 依存関係 Requirement

- Python 3.8.5  
- Pillow 8.3.0  
- TkinterDnD2 0.3.0  
- TkinterLib 1.0.1

## 使い方 Usage

```dosbatch
	image_album.exe
```
またはimage_album.exeのアイコンに表示したいファイルをドラッグ＆ドロップします

- 操作 Operation  
	- 表示する画像の指定方法  
		How to specify the image to be displayed  
		- ドラッグアンドドロップ  
			Drag and drop
			アプリ画面上の任意の位置に表示したいファイルをドラッグアンドドロップ  
			Drag and drop the file you want to display anywhere on the app screen
		- ファイル選択  
			File selection  
			「ファイル選択」ボタンをクリックしファイルを選択
			Click the file selection button and select the file  
	- 画像のサイズの変更  
		Resize image
		- 「サイズ」の右の入力エリアに幅をピクセル単位で指定します  
			Specify the width in pixels in the input area to the right of "Size"  
			数字以外は入力できません  
			You can only enter numbers  
			変更後、新たに表示した画像から有効です  
			After the change, it is valid from the newly displayed image.  
	- プレビュー  
		Preview  
		- 画像をマウスの右ボタンでダブルクリック  
			Double-click the image with the right mouse button  
		- 複数の画像を選択状態で「プレビュー」ボタンを押す  
			Press the "Preview" button with multiple images selected

- 画面の説明 Screen description  
	- ボタン Button  
		- ファイル選択：表示する画像を選択するダイアログを表示します  
			File selection: Displays a dialog for selecting the image to be displayed.  
		- すべて選択：表示されている画像をすべて選択します  
			Select All: Select all displayed images  
		- 選択解除：表示されている画像をすべて選択解除します  
			Deselect: Deselects all displayed images  
		- プレビュー：選択されている画像のプレビューを表示します  
			Preview: Shows a preview of the selected image  
	- 入力エリア Input area  
		- サイズ：画像の幅をピクセルで指定  
			Size: Specify the width of the image in pixels  
	- 画像表示エリア Image display area  
		- 画像を格子状に表示します  
			Display images in a grid pattern  
		- ウィンドウの幅に合わせて画像の列を調整します  
			Adjust the columns of the image to fit the width of the window  
		- 縦にスクロールします  
			Scroll vertically

## インストール方法 Installation

- pip install tkinterdnd2  
- pip install pillow  

## プログラムの説明サイト Program description site

[ScrolledFrameとwrapped_gridで作る画像一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/image/album)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.
