from PIL import Image, ImageDraw, ImageFont
import numpy as np
import io

class create:
	def diagram(data):
		width, height = 4000, 4000
		size = min(width, height) 
		
		image = Image.new('RGBA', (width, height), "white")
		draw = ImageDraw.Draw(image)
		
		total = sum(data.values())
		angles = [value / total * 360 for value in data.values()]
		colors = [
			'#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6',
			'#FFA533', '#33FF8C', '#B833FF', '#FFD733', '#33FFDA',
			'#FF3378', '#FFDB33', '#33FF6D', '#EF33FF', '#FF7F33',
			'#33FFBD', '#FF337A', '#FF335F', '#FF33FF', '#33FF4D',
			'#FF33FC', '#FF8033', '#FFC233', '#33BFFF', '#FF3333',
			'#33FF93', '#C533FF', '#33FF2D', '#FFB433', '#FF3389',
			'#FF334F', '#FFBE33', '#47FF33', '#FFB1C5', '#9D33FF',
			'#33A1FF', '#FF336B', '#FF5B33', '#C7FF33', '#E733FF',
			'#FF6D33', '#FF337D', '#33FF8E', '#FF5933', '#FFBB33',
			'#FFC4FF', '#33FFA0', '#FF6F8A', '#FF3535', '#AAFF33',
			'#FF7A33', '#FFC4A8', '#FF4B33', '#D5FF33', '#FFE833',
			'#B8FF33', '#FF3F33', '#FF7EDD', '#7333FF', '#FF3B33',
			'#33FFE4', '#FFA733', '#ED33FF', '#33DF33', '#FF8C33',
			'#FF4C33', '#A5FF33', '#11FF33', '#FF6F33', '#FF8C58',
			'#B933FF', '#E4FF33', '#FFBD33', '#33FF6E', '#FFA233',
			'#FF8D80', '#FF8C58', '#FF9D33', '#FFAA33', '#78FF33',
			'#FEFF33', '#F4FF33', '#33FF53', '#B0FF33', '#33D6FF',
			'#85FF33', '#9A33FF', '#3F33FF', '#FF6333', '#FF5733'
		]
		
		font = ImageFont.truetype("front.otf", size=65)
		start_angle = 0
		for i, (name, value) in enumerate(data.items()):
			end_angle = start_angle + angles[i]
			draw.pieslice([800, 800, size - 800, size - 800], start_angle, end_angle, fill=colors[i % len(colors)], outline='black', width=5)
			
			mid_angle = (start_angle + end_angle) / 2
			text_x = size / 2 + (size / 2 - 400) * np.cos(np.radians(mid_angle)) - 65 / 2
			text_y = size / 2 + (size / 2 - 400) * np.sin(np.radians(mid_angle)) - 65 / 2
			draw.text((text_x, text_y), name, fill="black", font=font)
			
			start_angle = end_angle
		
		image_io = io.BytesIO()
		image.save(image_io, format='PNG')
		image_io.seek(0)
		return image_io


