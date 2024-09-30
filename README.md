# HEIC / TIFF Converter TIPS
Ver 1.0     
2024/10/01　J-KITAKATA

## 概要    
　iPhoneやiPadでそのまま画像を撮影すると `.heic` という拡張子ファイルとして保存され、Windowsやその他ソフトウェアでは読み取れない場合が多々あります。それを解決するためにHEICファイルをTIFFファイルとJPEGファイルの2種類に変換できるようなアプリケーションを作成しました。   
　また、TIFFで保存したファイルをJPEGに再変換等を行いたい場合も考慮して、TIFFファイルから、JPEGに変換するモードも用意した。JPEGやTIFFからHEICに変換するモードはメリットが少ないと考え搭載していません。  
　処理時間に関しては、約0.6秒/枚で処理することが可能です。




## 利用可能な処理モード
* HEIC → JPEG
* HEIC → TIFF
* TIFF → JPEG




## 各拡張子の説明

| 拡張子 | 説明 |
| :---: | --- |
| `.heic` | アップル製品でデフォルトで採用されている形式。圧縮率はJPEGよりも高い。圧縮方法はH.265を利用。 |
| `.jpeg` / `.jpg` | 汎用的な画像ファイル。非可逆圧縮であるため、画像を編集して保存していくごとにだんだん画質が下がっていってしまうことが特徴。使いどころとしては、他人に画像を送る場合や、最終保存版に使用する。 |
| `.tiff` | zipファイルのような可逆圧縮を採用している画像ファイル。圧縮しても元に戻すことができる有能な画像ファイルではあるが、ファイルサイズが非常に大きいため、取り扱いには注意が必要。使いどころとしては、RAW画像ほどではないが、画質をある程度保持できるため、画像編集中の保存形式に適している。 |


## ライセンス等について
GitHubライセンスの`Apache License 2.0`に基づき改変して、Github上にアップロードする場合には元のソースコードと一緒にどこをどのように改変したのかを示すようにしてください。  
配布する場合には、このページのURLも一緒に配布してください。
詳しくは[リンク](https://www.apache.org/licenses/LICENSE-2.0.html)に記載されている内容を確認してください。  

>Copyright [yyyy] [name of copyright owner]
>
>Licensed under the Apache License, Version 2.0 (the "License");  
>you may not use this file except in compliance with the License.  
>You may obtain a copy of the License at  
>
>    http://www.apache.org/licenses/LICENSE-2.0
>
>Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



## その他(Other)
使用しているときに問題が発生したり、機能の追加を必要とする場合には[Discuss](https://github.com/J-KITAKATA/HEIC-TIFF_to_TIFF_or_JPEG/discussions)にて教えてください。  
見落としがない限りは、おおよそ2週間くらいで対応すると思います。  
  
If you encounter any problems when using it, or if you need additional features, please let us know on [Discuss](https://github.com/J-KITAKATA/HEIC-TIFF_to_TIFF_or_JPEG/discussions).
We will respond to your request within approximately two weeks, unless we have missed it.  

https://github.com/J-KITAKATA/HEIC-TIFF_to_TIFF_or_JPEG
