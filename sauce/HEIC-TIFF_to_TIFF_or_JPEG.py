import tkinter as tk
from tkinter import ttk, filedialog
import os
import subprocess
import threading

class HEICtoTIFFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC / TIFF Converter")
        self.root.geometry("450x330")

        self.input_folder = ""
        self.output_folder = ""
        self.converting = False
        self.current_output_file = ""

        # ラジオボタン用の変数
        self.output_format = tk.StringVar(value="jpeg")

        # 入力フォルダ選択用のフレーム
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5)

        self.input_entry = tk.Entry(input_frame, width=50, state='readonly')
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_button = tk.Button(input_frame, text="変換前フォルダを選択", command=self.select_input_folder)
        self.input_button.pack(side=tk.LEFT)

        # 出力フォルダ選択用のフレーム
        output_frame = tk.Frame(self.root)
        output_frame.pack(pady=5)

        self.output_entry = tk.Entry(output_frame, width=50, state='readonly')
        self.output_entry.pack(side=tk.LEFT, padx=5)
        self.output_button = tk.Button(output_frame, text="変換後フォルダを選択", command=self.select_output_folder)
        self.output_button.pack(side=tk.LEFT)

        # 変換形式を選択するラジオボタン
        tk.Label(self.root, text="変換形式を選択してください:").pack(pady=5)
        self.heic_to_jpeg_radio = tk.Radiobutton(self.root, text="HEIC → JPEG", variable=self.output_format, value="jpeg")
        self.heic_to_tiff_radio = tk.Radiobutton(self.root, text="HEIC → TIFF", variable=self.output_format, value="tiff")
        self.tiff_to_jpeg_radio = tk.Radiobutton(self.root, text="TIFF → JPEG", variable=self.output_format, value="tiff_to_jpeg")

        self.heic_to_jpeg_radio.pack(pady=5)
        self.heic_to_tiff_radio.pack(pady=5)
        self.tiff_to_jpeg_radio.pack(pady=5)

        # ステータスバー (プログレスバー)
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(padx=10, pady=10)

        # ステータステキスト
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=5)

        # ボタンフレーム（スタートボタンとキャンセルボタンを横並びに配置）
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # スタートボタン
        self.start_button = tk.Button(button_frame, text="変換開始", command=self.start_conversion, state=tk.DISABLED)
        self.start_button.grid(row=0, column=0, padx=10)

        # キャンセルボタン
        self.cancel_button = tk.Button(button_frame, text="キャンセル", command=self.cancel_conversion)
        self.cancel_button.grid(row=0, column=1, padx=10)

    def select_input_folder(self):
        """入力フォルダを選択"""
        self.input_folder = filedialog.askdirectory()
        if self.input_folder:
            self.input_entry.config(state='normal')
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.input_folder)
            self.input_entry.config(state='readonly')
        self.update_start_button_state()

    def select_output_folder(self):
        """出力フォルダを選択"""
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, self.output_folder)
            self.output_entry.config(state='readonly')
        self.update_start_button_state()

    def update_start_button_state(self):
        """入力・出力フォルダが選択されたら開始ボタンを有効にする"""
        if self.input_folder and self.output_folder:
            self.start_button.config(state=tk.NORMAL)

    def start_conversion(self):
        """変換処理を開始"""
        self.converting = True
        self.status_label.config(text="変換処理中...")
        thread = threading.Thread(target=self.process_folder)
        thread.start()

    def cancel_conversion(self):
        """変換処理をキャンセル"""
        if self.converting:
            self.converting = False
            self.status_label.config(text="変換をキャンセルしました。")
            self.progress.stop()
        else:
            # 処理をしていない場合はアプリケーションを終了
            self.root.quit()

    def process_folder(self):
        """フォルダ内のファイルを選択された形式に変換"""
        if self.output_format.get() == "tiff_to_jpeg":
            files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.tiff') or f.lower().endswith('.tif')]
        else:
            files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.heic')]

        total_files = len(files)
        if total_files == 0:
            self.status_label.config(text="変換するファイルが見つかりません。")
            self.start_button.config(state=tk.NORMAL)
            return

        self.progress["maximum"] = total_files

        for index, file in enumerate(files):
            if not self.converting:
                break

            input_file_path = os.path.join(self.input_folder, file)

            if self.output_format.get() == "jpeg":
                output_file_name = os.path.splitext(file)[0] + '.jpeg'
            elif self.output_format.get() == "tiff":
                output_file_name = os.path.splitext(file)[0] + '.tiff'
            elif self.output_format.get() == "tiff_to_jpeg":
                output_file_name = os.path.splitext(file)[0] + '.jpeg'

            self.current_output_file = os.path.join(self.output_folder, output_file_name)

            try:
                subprocess.run(['magick', input_file_path, self.current_output_file], check=True)
                self.status_label.config(text=f"{file} を変換しました。")
            except subprocess.CalledProcessError as e:
                self.status_label.config(text=f"エラーが発生しました: {e}")
                break

            self.progress["value"] = index + 1
            self.root.update_idletasks()

        self.converting = False
        self.status_label.config(text="変換が完了しました。")
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = HEICtoTIFFConverterApp(root)
    root.mainloop()
