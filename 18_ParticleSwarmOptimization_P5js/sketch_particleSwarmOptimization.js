
//------------------------------------------------------------------------------
// Sketch: particle swarm optimization visualization of Bukin function
// by Ramkumar
//------------------------------------------------------------------------------

// declaring width and height of canvas
let width,height;

// defining min and max ranges of x andy
let Xmin = -15, Xmax = -5, Ymin = -4, Ymax = 6;

let img;

// defining constants of PSO algorithm
let w = 0.8, C1 = 0.01, C2 = 0.01;

// defining global best variable and initial number of particles
let Gbest, N_init = 15;

// declaring particles array
particles = []

// defining objective function - Bukin function N. 6
function f_obj(x,y){
    return 100*sqrt(abs(y-0.01*x**2))+0.01*abs(x+10);
}

// function converting pixels to coordinates
function getXY(x,y){
    // normalizing and scaling x and y values
    let xval = x/width*(Xmax-Xmin) + Xmin;
    let yval = (height-y)/height*(Ymax-Ymin) + Ymin;

    return [xval, yval]
}

// function converting coordinates to pixels
function getPixel(x,y){
    let px = (x-Xmin)/(Xmax-Xmin)*width
    let py = height - (y-Ymin)/(Ymax-Ymin)*height
    return [px,py]
}

// preloading the contour image of obj. function
function preload(){
    // loading image
    img = loadImage("contour.png")
}

function setup(){
    // setting width and height of canvas based on f_obj contour
    width  = img.width
    height = img.height

    // randomly initializing global best point
    Gbest = [random(width),random(height)]

    // creating canvas
    createCanvas(width, height);

    // initializing particles
    for(let i = 0; i < N_init; i++)
        particles.push(new Particle(random(width),random(height),random(0.01),random(0.01)))

}

// draw function definition
function draw(){

    // showing objective function contour
    image(img,0,0)
    describe("objective function contour")

    let fvals = []

    // updating particle data
    for(let i = 0; i < particles.length; i++){
        particles[i].show()
        particles[i].updateVelocity()
        particles[i].updatePosition()
        particles[i].updatePbest()
        fvals.push(particles[i].Pbest_f)
    }

    // updating Gbest
    let idx = fvals.indexOf(Math.min(...fvals))
    Gbest[0] = particles[idx].x_show
    Gbest[1] = particles[idx].y_show

    let gbestXY = getXY(Gbest[0],Gbest[1])

    // console.log(particles[0].Pbest_x,particles[0].Pbest_y)
    console.log(gbestXY[0],gbestXY[1],idx)

    // text output
    textSize(30)
    text("Particle Swarm Optimization of Bukin function",width*0.1,height*0.1)
    text("Gbest = ("+str(round(gbestXY[0],3))+","+str(round(gbestXY[1],3))+")",width*0.1,height*0.9)

}

// defining particle class
class Particle{
    // constructor function
    constructor (x,y,vx,vy,dia=10,color=[0,0,0]){
        this.x_show   = x
        this.y_show   = y
        let xvec      = getXY(x,y)
        this.x_curr   = xvec[0]
        this.y_curr   = xvec[1]
        this.vx_curr  = vx
        this.vy_curr  = vy
        this.vx_np1   = vx
        this.vy_np1   = vy
        this.x_np1    = x
        this.y_np1    = y

        this.Pbest_x  = this.x_curr
        this.Pbest_y  = this.y_curr
        this.Pbest_f  = f_obj(this.x_curr,this.y_curr)

        this.diameter = dia
        this.color    = color
    }

    // updaring particle velocity
    updateVelocity(){
        let r1 = random(1)
        let r2 = random(1)

        let gbest = getXY(Gbest[0],Gbest[1])
        // computing velocity
        this.vx_np1 = (w*this.vx_curr + C1*r1*(this.Pbest_x - this.x_curr) +
                            C2*r2*(gbest[0] - this.x_curr))
        this.vy_np1 = (w*this.vy_curr + C1*r1*(this.Pbest_y - this.y_curr) +
                            C2*r2*(gbest[1] - this.y_curr))
    }

    // updating particle position
    updatePosition(){
        this.x_np1 = this.x_curr + this.vx_np1
        this.y_np1 = this.y_curr + this.vy_np1
    }

    // updating Pbest
    updatePbest(){
        // computing f_obj value for new position
        let f_new = f_obj(this.x_np1,this.y_np1)

        // checking if f_new is best
        if (f_new < this.Pbest_f){
            this.Pbest_x = this.x_np1
            this.Pbest_y = this.y_np1
            this.Pbest_f = f_new
        }

        // updating postion and velocity values
        this.x_curr  = this.x_np1
        this.y_curr  = this.y_np1
        this.vx_curr = this.vx_np1
        this.vy_curr = this.vy_np1

        let pvec = getPixel(this.x_curr,this.y_curr)
        this.x_show  = pvec[0]
        this.y_show  = pvec[1]
    }

    // show particle
    show(){
        fill(this.color)
        circle(this.x_show,this.y_show,this.diameter)
    }
}


// mouse function to add new particle at clicked location
function mousePressed(){
    let x = mouseX, y = mouseY;
    particles.push(new Particle(x,y,random(0.01),random(0.01)))
}

