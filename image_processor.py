# -*- coding:utf-8 -*-
from PIL import Image

class ImageProcessor():

    @staticmethod
    def transparentize(src,dst):
        # 透過したい画像を読み込み
        org = Image.open(src)
        # 同じサイズの画像を作成
        trans = Image.new('RGBA', org.size, (0, 0, 0, 0))
        width,height = org.size
        for x in xrange(width):
            for y in xrange(height):
                pixel = org.getpixel( (x, y) )

                # 白なら処理しない
                if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                    continue

                # 白以外なら、用意した画像にピクセルを書き込み
                trans.putpixel( (x, y), pixel )
        # 透過画像を保存
        trans.save(dst)

    @staticmethod
    def grayscalize(src,dst):
        img = Image.open(src).convert('L').save(dst)

    @staticmethod
    def convert_gray_to_red(src,dst):
        img1 = Image.open(src)

        # RGB値のバンドを持つ画像オブジェクトに変換
        img1 = img1.convert('RGB')

        # 画像のピクセルサイズを取得（タプル型）
        pixelSizeTuple = img1.size

        # 新しい画像オブジェクトを用意する
        # ここではアルファ値を持つ、img1と同じサイズの画像を用意
        img2 = Image.new('RGB', img1.size)

        # 各ピクセルからgetpixelメソッドで色情報を取得し、特定の条件に基づいてputpixelメソッドで別の色を入れる。
        # ここでは、RGBの内、赤と緑と青が220以上の値をとるピクセルを赤で塗り替える。
        for i in range(pixelSizeTuple[0]):
            for j in range(pixelSizeTuple[1]):
                r,g,b = img1.getpixel((i,j))
                if r < 220 and g < 220 and b < 220:
                    img2.putpixel((i,j), (255,0,0)) # 真っ赤に！
                else:
                    img2.putpixel((i,j), (r,g,b)) # 元の色

        # 画像を保存
        img2.save(dst)
