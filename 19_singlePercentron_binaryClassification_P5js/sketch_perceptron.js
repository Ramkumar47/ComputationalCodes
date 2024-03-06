
//------------------------------------------------------------------------------
// Sketch: single perceptron training in binary classification
// by Ramkumar
//------------------------------------------------------------------------------

// defining physical space limits
let X_lim = [-1,1]
let Y_lim = [-1,1]

// number of training points
N_points = 200

// defining learning rate
LR = 0.002

// initializing points list
let points = []
let y1, y2;

// declaring a perceptron
let ptrn

let count = 0

// defining contour function
function func(x){
	return -2*x
}

// setup function
function setup(){
	createCanvas(600,600)

	// initializing points
	for(let i = 0; i < N_points; i++){
		points.push(new Point(random(-1,1),random(-1,1)))
	}

	// computing line's extreme coordinates
	y1 = func(X_lim[0])
	y2 = func(X_lim[1])

	// initializing perceptron
	ptrn = new Perceptron()

	// creating start and stop button
	stopButton = createButton("stop")
	stopButton.position(width+10,height/2-40)
	stopButton.mousePressed(() => {
		console.log("stopped")
		noLoop()
	})
	startButton = createButton("start")
	startButton.position(width+10,height/2)
	startButton.mousePressed(() => {
		console.log("started")
		loop()
	})

	// // saving frames for animation
	// saveFrames('image','png',15,5)

}

// draw function
function draw(){
	background(255)

	// drawing line
	stroke(255,0,0)
	line(map(X_lim[0],X_lim[0],X_lim[1],0,width),map(y1,Y_lim[0],Y_lim[1],height,0),
		map(X_lim[1],X_lim[0],X_lim[1],0,width),map(y2,Y_lim[0],Y_lim[1],height,0))

	// training the perceptron with single point
	ptrn.train(points[count].x,points[count].y,points[count].label)
	count = (count + 1)%N_points

	// prediction on all the porints
	for(let i = 0; i < N_points; i++){
		let pred_val = ptrn.predict(points[i].x,points[i].y)
		if (pred_val == points[i].label)
			points[i].setColor(1)
		else
			points[i].setColor(0)
		points[i].show()
	}

	// drawing prediction line
	let xp1 = X_lim[0]
	let yp1 = -(ptrn.w1*xp1+ptrn.w3)/ptrn.w2
	let xp2 = X_lim[1]
	let yp2 = -(ptrn.w1*xp2+ptrn.w3)/ptrn.w2

	xp1 = map(xp1,X_lim[0],X_lim[1],0,width)
	yp1 = map(yp1,Y_lim[0],Y_lim[1],height,0)
	xp2 = map(xp2,X_lim[0],X_lim[1],0,width)
	yp2 = map(yp2,Y_lim[0],Y_lim[1],height,0)

	stroke(0,255,0)
	line(xp1,yp1,xp2,yp2)

}

// point object definition
class Point{
	constructor(x,y){
		this.x = x
		this.y = y
		this.px = map(x,X_lim[0],X_lim[1],0,width)
		this.py = map(y,Y_lim[0],Y_lim[1],height,0)

		let yval = func(this.x)

		if (yval > this.y){
			this.label = 1
		}
		else{
			this.label = -1
		}

		fill(255)
	}

	setColor(val){
		if(val == 1) fill(255)
		else  fill(0)
	}


	show(){
		stroke(0)
		strokeWeight(3)
		circle(this.px,this.py,10)
	}
}

// defining perceptron object
class Perceptron{
	constructor(){
		this.w1 = random(-1,1)
		this.w2 = random(-1,1)
		this.w3 = random(-1,1)
	}

	predict(x,y){
		let val = this.w1*x+this.w2*y+this.w3
		return this.activationFunction(val)
	}

	activationFunction(x){
		if (x > 0)
			return -1
		else
			return 1
	}

	train(x,y,act_val){
		let pred_val = this.predict(x,y)
		let error = pred_val - act_val

		this.w1 = this.w1 + LR*error*x
		this.w2 = this.w2 + LR*error*y
		this.w3 = this.w3 + LR*error*1

		console.log(error)
	}
}
