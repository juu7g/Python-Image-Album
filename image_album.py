"""
画像アルバム
画像を格子状に並べて一覧表示
"""

import os, sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinterdnd2 import *
from typing import Tuple                # 関数アノテーション用 
from PIL import Image, ImageTk          # Pillow
from PIL.ExifTags import TAGS, GPSTAGS  # Exifタグ情報
from tkinter_libs import TkinterLib
from tkinter_libs import ScrolledFrame

class Album(ttk.Frame):
    """
    画像をリストビューで表示する
    """
    def __init__(self, master):
        """
        画面の作成
        上のFrame: 入力用
        下のFrame: 出力用
        """
        super().__init__(master)
        self.thumbnail_xy = 200
        self.image_op = ImageOp()
        self.u_frame = tk.Frame(master, bg="white")     # 背景色を付けて配置を見る
        self.b_frame = tk.Frame(master, bg="green")     # 背景色を付けて配置を見る
        self.u_frame.pack(fill=tk.X)
        self.b_frame.pack(fill=tk.BOTH, expand=True)
        self.create_input_frame(self.u_frame)
        self.frame4images = ScrolledFrame(self.b_frame, padx=5, pady=5)
        self.frame4images.parent_frame.pack(fill=tk.BOTH, expand=True)
        self.frame4images.parent_canvas.config()
        # bind
        self.frame4images.bind_class("Checkbutton", "<Double 3>", self.preview_image)  # マウスを右ダブルクリックしたときの動作
        # wrapped_gridのbind
        self.frame_children = []
        self.frame4images.parent_canvas.bind("<Configure>", lambda event: TkinterLib.wrapped_grid(
            self.frame4images.parent_canvas, *self.frame_children, event=event, flex=False), add=True)

    def entry_validate(self, action:str, modify_str:str) -> bool:
        """
        エントリーの入力検証
        Args:
            str:    アクション(削除：0、挿入：1、その他：-1)
            str:    挿入、削除されるテキスト
        """
        if action != "1": return True   # 挿入の時だけ検証
        return modify_str.isdigit()     # 数字かどうか

    def create_input_frame(self, parent):
        """
        入力項目の画面の作成
        上段：ファイル選択ボタン、すべて選択、選択解除、プレビューボタン
        下段：メッセージ
        """
        self.btn_f_sel = tk.Button(parent, text="ファイル選択", command=self.select_files)
        self.btn_select_all = tk.Button(parent, text="すべて選択", command=self.select_all)
        self.btn_deselect_all = tk.Button(parent, text="選択解除", command=self.deselect_all)
        self.btn_preview = tk.Button(parent, text="プレビュー", command=self.preview_images)
        # サイズ指定 エントリーは検証して数字のみ入力
        self.lbl_size = tk.Label(parent, text="サイズ")
        self.var_size = tk.StringVar(value="200")
        self.ety_size = tk.Entry(parent, width=8, textvariable=self.var_size
                                , validate="key", vcmd=(self.register(self.entry_validate), "%d", "%S"))
        # massage
        self.msg = tk.StringVar(value="msg")
        self.lbl_msg = tk.Label(parent
                                , textvariable=self.msg
                                , justify=tk.LEFT
                                , font=("Fixedsys", 11)
                                , relief=tk.RIDGE
                                , anchor=tk.W)
        # pack
        self.lbl_msg.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)    # 先にpackしないと下に配置されない
        self.ety_size.pack(side=tk.RIGHT, padx=5)
        self.lbl_size.pack(side=tk.RIGHT, padx=5)
        self.btn_preview.pack(side=tk.RIGHT, padx=5)
        self.btn_deselect_all.pack(side=tk.RIGHT, padx=5)
        self.btn_select_all.pack(side=tk.RIGHT, padx=5)
        self.btn_f_sel.pack(side=tk.RIGHT, padx=5)
        # bind

    def on_check(self, event=None, var_check:tk.Variable=None, obj_check:str=None):
        """
        チェックボックスがクリックされたらチェックされている集合の内容を更新する
        Args:
            Variable:   ウィジェット変数
            str:        画像のパス
        """
        if var_check.get():
            self.checked_image_paths.add(obj_check)
        else:
            self.checked_image_paths.discard(obj_check)

    def set_images2frame(self, parent:tk.Frame, rows:list, images:list):
        """
        parent(Frame)にimagesの要素分Frameを作成しgrid
        Frameはself.frame_childrenにappendして画像が残るようにする
        Frameには画像用Checkbuttonと情報用Labelを追加
        Args:
            Frame:      親Frame
            list:       行データ(行リストの列リスト((ファイル名、幅、高さ、ファイルサイズ、exif情報、gps情報)))
            list:       画像データ
        """
        if not rows:    # 要素が無ければ戻る
            return

        # チェックされた画像用セットを初期化
        self.checked_image_paths = set()

        # 要素の削除
        for w in parent.winfo_children():
            w.destroy()

        # 要素の追加
        self.frame_children = []
        for row, image in zip(rows, images):
            # 要素の追加(Frameに画像用Checkbuttonと情報用Label)
            frame1 = tk.Frame(parent, relief=tk.GROOVE, borderwidth=2)
            if row[4]:
                exif = " | Exifあり"
            else:
                exif = ""
            # ファイル名、Exif情報のあり/なしを表示するラベルの作成。文字はサムネイルの幅+10pxで折り返し
            disp_text = f"{os.path.basename(row[0])}\n{row[1]} x {row[2]}{exif}" 
            label_f_name = tk.Label(frame1, text=disp_text, wraplength=self.thumbnail_xy + 10)
            boolen_var = tk.BooleanVar(False)
            # チェックボックスの作成(imageに画像、textに画像パス(ダブルクリックプレビューで使用))
            check_box = tk.Checkbutton(frame1, image=image, width=self.thumbnail_xy + 10, text=row[0], compound=tk.NONE, variable=boolen_var, indicatoron=False)
            check_box.config(command = lambda x=boolen_var, o=row[0]: self.on_check(var_check=x, obj_check=o))
            # pack
            label_f_name.pack(side=tk.BOTTOM)
            check_box.pack()
            self.frame_children.append(frame1)
            frame1.grid(row=0, column=0)    # 一度仮にgridして個々のサイズが確定 できるようにする
        
        # コマンドライン引数指定の場合、mainloopが起動していないのでupdateする
        # parent.update()

        # 親Frameの幅に合わせてgridする
        if self.frame_children:
            TkinterLib.wrapped_grid(parent.parent_canvas
                                , *self.frame_children, flex=False, force=True)

    def open_files_get_images_set2frame(self, event=None):
        """
        self.file_pathsのパスからファイル情報、画像サムネイルを作成
        frame4imagesに画像を含んだFrameを追加
        """
        self.image_op.msg = ""
        self.thumbnail_xy = int(self.var_size.get())
        # DnD対応
        if event:
            # DnDのファイル情報はevent.dataで取得
            # "{空白を含むパス名1} 空白を含まないパス名1"が返る
            # widget.tk.splitlistでパス名のタプルに変換
            self.file_paths = self.u_frame.tk.splitlist(event.data)
            
        # 取得したパスから拡張子がself.extentiosのkeyに含まれるものだけにする
        file_paths2 = tuple(path for path in self.file_paths if os.path.splitext(path)[1].lower() in self.image_op.extensions)
        if len(file_paths2) == 0:
            self.image_op.msg = "対象のファイルがありません"
            self.msg.set(self.image_op.msg)
            return
        if file_paths2 != self.file_paths:
            self.image_op.msg = "対象外のファイルは除きました"
            self.file_paths = file_paths2

        # 取得したパスから表示データと画像を作成
        columns1, rows1, images1, msg1 = self.image_op.get_images(self.file_paths, self.thumbnail_xy)
        self.images4dialog = {}  # ダイアログ表示用画像初期化

        self.msg.set(self.image_op.msg)     # エラーメッセージの表示

        # 画像を含むFrameをframe4imagesに新規追加
        self.set_images2frame(self.frame4images, rows1, images1)

    def select_files(self, event=None):
        """
        ファイル選択ダイアログを表示。選択したファイルパスを取得
        ファイル情報や画像を取得して表示
        """
        # 拡張子の辞書からfiletypes用のデータを作成
        # 辞書{".csv":"CSV", ".tsv":"TSV"}、filetypes=[("CSV",".csv"), ("TSV",".tsv")]
        self.file_paths = filedialog.askopenfilenames(
            filetypes=[(value, key) for key, value in self.image_op.extensions.items()])
        self.open_files_get_images_set2frame()		# ファイル情報や画像を取得して表示

    def preview_image(self, event=None, path=""):
        """
        画像のプレビュー
        ダイアログ表示
		Args:
            string:     ファイルパス(ない場合もある)
        """

        if event:
            if not event.widget.config("image"): return # imageオプションに指定がないなら抜ける
            path1 = event.widget.cget("text")   # ファイル名取得
        else:
            path1 = path

        # ダイアログ表示
        dialog_ = tk.Toplevel(self)      # モードレスダイアログの作成
        dialog_.title("Preview")         # タイトル
        self.images4dialog[path1] = ImageTk.PhotoImage(file=path1)    # 複数表示する時のために画像を残す
        label1 = tk.Label(dialog_, image=self.images4dialog[path1])   # 最後のものを表示
        label1.pack()
        dialog_.focus()
        # 閉じた時の動作を指定 最前面のウィジェットに設定しないと複数回発生する
        label1.bind("<Destroy>", lambda e: self.on_destroy(event=e, path=path1))
        # make Esc exit the preview
        dialog_.bind('<Escape>', lambda e: dialog_.destroy())

    def on_destroy(self, event=None, path=None):
        if event:
            # print(f"do pop key:{path} widget:{event.widget}")   # for debug
            self.images4dialog.pop(path)    # 表示用に残した画像を削除

    def preview_images(self, event=None):
        """
        選択された画像のプレビュー
        """
        self.msg.set("")
        paths = self.checked_image_paths
        for path1 in paths:
            self.preview_image(path=path1)
        if not paths:
            self.msg.set("選択された画像がありません")

    def select_all(self, event=None):
        """
        Checkbuttonをすべて選択する
        """
        self.set_all_checkbox(True)

    def deselect_all(self, event=None):
        """
        Checkbuttonをすべて選択解除する
        """
        self.set_all_checkbox(False)

    def set_all_checkbox(self, is_selected:bool):
        """
        Checkbuttonの選択状態をすべて設定する
		Args:
			bool: 選択するか選択解除するか
        """
        for child_ in self.frame_children:
            for item_ in child_.winfo_children():
                if type(item_) == tk.Checkbutton:
                    if is_selected:
                        item_.select()      # Checkbuttonを選択
                        self.checked_image_paths.add(item_.cget("text"))        # パスを登録
                    else:
                        item_.deselect()    # Checkbuttonを非選択
                        self.checked_image_paths.discard(item_.cget("text"))    # パスを削除

class ImageOp():
    """
    画像データの操作を行う
    """
    def __init__(self):
        self.msg = ""   # メッセージ受渡し用
        # 対象拡張子	辞書(key:拡張子、値:表示文字)
        self.extensions = {".png .jpg .gif .webp":"画像", ".png":"PNG", 
                            ".jpg":"JPEG", ".gif":"GIF", ".webp":"WebP"}

    def get_images(self, file_names:tuple, thumbnail_xy = 160) -> Tuple[list, list, list, str]:
        """
        画像ファイルを読みデータを返す
        Args:
            str:    ファイル名
        Returns:
            columns1(list):     列名 
            rows1(list):        行データ(行リストの列リスト)
                                ファイル名, 幅(px), 高さ(px), サイズ(kB), 画像情報 EXIF, 位置情報 GPS
            self.images(list):  画像データ
            msg1(str):          エラーメッセージ(空文はエラーなし)
        """
        msg1 = ""
        columns1 = ["ファイル名", "幅(px)", "高さ(px)", "サイズ(kB)", "画像情報 EXIF", "位置情報 GPS"]
        try:
            self.images = []    # selfでないとうまくいかない。理由はローカル変数だと関数終了後gcされるため
            rows1 = []
            for file_name in file_names:   # パス名で回す
                # basename = os.path.basename(file_name)
                f = os.path.normpath(file_name)
                wrap_file_name = f.replace("\\", "\\\n")
                # 画像のサイズ
                file_size = os.path.getsize(file_name)
                # 画像の取得
                image1 = Image.open(file_name)
                # ファイルサイズの取得
                image_size = image1.size
                # Exif情報の取得
                exif_dict = image1.getexif()
                exif = [TAGS.get(k, "Unknown")+ f": {str(v)}" for k, v in exif_dict.items()]
                exif_str = "\n".join(exif)
                # GPS情報の取得
                gps_dict = exif_dict.get_ifd(34853)
                gps = [GPSTAGS.get(k, "Unknown") + f": {str(v)}" for k, v in gps_dict.items()]
                gps_str = "\n".join(gps)
                # 縮小
                image1.thumbnail((thumbnail_xy, thumbnail_xy), Image.BICUBIC) # image1が直接縮小される
                # サムネイルの大きさを統一(そうしないとチェックボックスの位置がまちまちになるため)
                # ベース画像の作成と縮小画像の貼り付け(中央寄せ)
                base_image = Image.new('RGBA', (thumbnail_xy, thumbnail_xy), (255, 0, 0, 0))  # 透明なものにしないとgifの色が変わる
                horizontal = int((base_image.size[0] - image1.size[0]) / 2)
                vertical = int((base_image.size[1] - image1.size[1]) / 2)
                # print(f"size:{image1.size} h,v:{horizontal},{vertical}, base:{base_image.size}")  # debug
                base_image.paste(image1, (horizontal, vertical))
                image1 = base_image
                # PhotoImageへ変換
                image1 = ImageTk.PhotoImage(image1)
                # 列データと画像データを追加
                self.images.append(image1)
                # 列データ(ファイル名、幅、高さ、ファイルサイズ、exif情報、gps情報)
                rows1.append([f, image_size[0], image_size[1], 
                                "{:.1f}".format(file_size/1024), exif_str, gps_str])
        except Exception as e:
            msg1 = e
            print(f"error:{e}")
        finally:
            return columns1, rows1, self.images, msg1

if __name__ == '__main__':
    root = TkinterDnD.Tk()      # トップレベルウィンドウの作成  tkinterdnd2の適用
    root.title("アルバム")      # タイトル
    root.geometry("750x702")    # サイズ
    album = Album(root)   # Albumクラスのインスタンス作成
    root.drop_target_register(DND_FILES)            # ドロップ受け取りを登録
    root.dnd_bind("<<Drop>>", album.open_files_get_images_set2frame)    # ドロップ後に実行するメソッドを登録
    # コマンドライン引数からドラッグ＆ドロップされたファイル情報を取得
    if len(sys.argv) > 1:
        album.file_paths = tuple(sys.argv[1:])
        album.open_files_get_images_set2frame()			# オープン処理の実行
    root.mainloop()
