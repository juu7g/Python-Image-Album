# Python-Image-Album

## �T�v Description
�摜�ꗗ  
Image list  

�摜�t�@�C����I�����A�t�@�C���̃T���l�C���摜�ƃt�@�C�������i�q��Ɉꗗ�\������   
Select image files and display the thumbnail image of the file and the file information in a grid pattern.  

## ���� Features

- GIF�APNG�AJPEG�AWebP �t�@�C����ǂݍ��݉摜�̃T���l�C�����i�q��ɕ\��  
	Read GIF, PNG, JPEG, WebP files and display thumbnails of images in a grid pattern  
- �摜�̃t�@�C�����A�T�C�Y�AExif ���̗L����\��  
	Show image file name, size, and presence / absence of Exif information  
- �摜��I�����Č�����Ńv���r���[���_�C�A���O�\��  
	Select images and display full-scale preview in dialog
- �h���b�O�A���h�h���b�v�Ńt�@�C�����w��\(TkinterDnD2�g�p)
	File can be specified by drag and drop(using TkinterDnD2)  
- exe�Ƀh���b�O�A���h�h���b�v�Ńt�@�C�����w��\(TkinterDnD2�g�p�ł�)
	File can be specified by dragging and dropping to exe(using TkinterDnD2)  

## �ˑ��֌W Requirement

- Python 3.8.5  
- Pillow 8.3.0  
- TkinterDnD2 0.3.0  
- TkinterLib 1.0.1

## �g���� Usage

```dosbatch
	image_album.exe
```
�܂���image_album.exe�̃A�C�R���ɕ\���������t�@�C�����h���b�O���h���b�v���܂�

- ���� Operation  
	- �\������摜�̎w����@  
		How to specify the image to be displayed  
		- �h���b�O�A���h�h���b�v  
			Drag and drop
			�A�v����ʏ�̔C�ӂ̈ʒu�ɕ\���������t�@�C�����h���b�O�A���h�h���b�v  
			Drag and drop the file you want to display anywhere on the app screen
		- �t�@�C���I��  
			File selection  
			�u�t�@�C���I���v�{�^�����N���b�N���t�@�C����I��
			Click the file selection button and select the file  
	- �摜�̃T�C�Y�̕ύX  
		Resize image
		- �u�T�C�Y�v�̉E�̓��̓G���A�ɕ����s�N�Z���P�ʂŎw�肵�܂�  
			Specify the width in pixels in the input area to the right of "Size"  
			�����ȊO�͓��͂ł��܂���  
			You can only enter numbers  
			�ύX��A�V���ɕ\�������摜����L���ł�  
			After the change, it is valid from the newly displayed image.  
	- �v���r���[  
		Preview  
		- �摜���}�E�X�̉E�{�^���Ń_�u���N���b�N  
			Double-click the image with the right mouse button  
		- �����̉摜��I����ԂŁu�v���r���[�v�{�^��������  
			Press the "Preview" button with multiple images selected

- ��ʂ̐��� Screen description  
	- �{�^�� Button  
		- �t�@�C���I���F�\������摜��I������_�C�A���O��\�����܂�  
			File selection: Displays a dialog for selecting the image to be displayed.  
		- ���ׂđI���F�\������Ă���摜�����ׂđI�����܂�  
			Select All: Select all displayed images  
		- �I�������F�\������Ă���摜�����ׂđI���������܂�  
			Deselect: Deselects all displayed images  
		- �v���r���[�F�I������Ă���摜�̃v���r���[��\�����܂�  
			Preview: Shows a preview of the selected image  
	- ���̓G���A Input area  
		- �T�C�Y�F�摜�̕����s�N�Z���Ŏw��  
			Size: Specify the width of the image in pixels  
	- �摜�\���G���A Image display area  
		- �摜���i�q��ɕ\�����܂�  
			Display images in a grid pattern  
		- �E�B���h�E�̕��ɍ��킹�ĉ摜�̗�𒲐����܂�  
			Adjust the columns of the image to fit the width of the window  
		- �c�ɃX�N���[�����܂�  
			Scroll vertically

## �C���X�g�[�����@ Installation

- pip install tkinterdnd2  
- pip install pillow  

## �v���O�����̐����T�C�g Program description site

[ScrolledFrame��wrapped_grid�ō��摜�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/image/album)  

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
This software is released under the MIT License, see LICENSE.txt.
