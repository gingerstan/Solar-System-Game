import pygame as py
import pathlib

py.init()
py.display.set_caption("solar system something")
screen = py.display.set_mode((1000,1000), 0, 32)

white = (255,255,255)

assets = {}

for asset_path in pathlib.Path('assets').iterdir():
	if asset_path.is_file() and asset_path.name.endswith('.png'):
		# print(asset_path.stem)
		asset = py.image.load(asset_path)
		asset.set_colorkey(white)
		asset.convert()
		assets[f"{asset_path.stem}"] = asset


def scale_by(image_name,scale):
	asset_dict[image_name] = py.transform.scale_by(asset_dict[image_name],scale)

