run:
	processing cli --sketch=../testSketch --run

refresh:
	rm -rf frames && mkdir frames && rm -f *.gif *.mp4

generateVideo:
	ffmpeg -r 30 -i frames/line-%06d.png animation.mp4
