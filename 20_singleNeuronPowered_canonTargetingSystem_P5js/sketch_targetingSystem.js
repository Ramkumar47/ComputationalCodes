
//------------------------------------------------------------------------------
// Sketch: single neuron powered targeting system
// by Ramkumar
//------------------------------------------------------------------------------


// defining basic parameters---------------------------------------------------
let dia             = 1.0
let xlim            = [0,2]
let ylim            = [-1,1]
let target_width    = 0.15
let width           = 600
let height          = 400
let target_location = 1.5
let LR              = 0.4

let target_y,target_y_px,t_width_px
let count = 1

// intermediate functions and objects definition-------------------------------
// draw target function
function draw_target(yloc){

    let t_x_loc = map(target_location,xlim[0],xlim[1],0,width)

    fill(0,0,255)
    circle(t_x_loc,yloc+t_width_px/2.0,10)
    circle(t_x_loc,yloc-t_width_px/2.0,10)

    text("target",t_x_loc,yloc-t_width_px)

}

// draw cannon function
function draw_cannon(angle){
    strokeWeight(20)
    stroke(0,255,0)
    line(0,height/2,20*cos(angle),height/2-20*sin(angle))
    stroke(0)
    strokeWeight(1)

    fill(0,255,0)
    text("cannon",0,height/2+30)
}

// ball object definition
class Ball{
    constructor(){
        this.radius   = 10
        this.velocity = createVector(0,0)
        // this.Vmag     = 7
        this.Vmag     = 0.03
        this.angle    = random(-PI/4.0,PI/4.0)
        // this.position = createVector(this.radius,height/2)
        this.position = createVector(0,0)
        this.pos_px = map(this.position.x, xlim[0],xlim[1],0,width)
        this.pos_py = map(this.position.y, ylim[0],ylim[1],height,0)
        this.W        = random(-1,1)
    }

    show(){
        fill(255,0,0)
        // circle(this.position.x, this.position.y, this.radius*2)
        circle(this.pos_px, this.pos_py, this.radius*2)
    }

    update(){
        this.velocity.x = this.Vmag*cos(this.angle)
        this.velocity.y = this.Vmag*sin(this.angle)
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
        this.pos_px = map(this.position.x, xlim[0],xlim[1],0,width)
        this.pos_py = map(this.position.y, ylim[0],ylim[1],height,0)
        // this.position.x += this.velocity.x
        // this.position.y += this.velocity.y
    }

}

// neuron definition
class Neuron{
    constructor(yloc){
        this.weight = random(-1,1)
        this.yloc   = yloc
        this.L      = 1
        this.gradL  = 1
    }

    // sigmoid activation
    activation(){
        return 1.0/(1+exp(-this.weight))
    }

    // loss evaluation and optimization using reverse mode autodiff
    optimize(){
        // evaluating forward pass
        let dw     = 1.0

        let t1     = exp(-this.weight)
        let dt1    = -exp(-this.weight)*dw

        let t2     = 1 + t1
        let dt2    = dt1

        let t3     = 1.0/t2
        let dt3    = -1.0/t2**2*dt2

        let t4     = PI/2.0*t3 - PI/4.0
        let dt4    = PI/2.0*dt3

        let t5     = target_location*tan(t4)
        let dt5    = target_location/cos(t4)**2*dt4

        let t6     = (target_y - t5)
        let dt6    = -dt5

        this.L     = t6**2

        // reverse pass
        let dLdt6 = 2*t6
        let dLdt5 = dLdt6*dt6/dt5
        let dLdt4 = dLdt5*dt5/dt4
        let dLdt3 = dLdt4*dt4/dt3
        let dLdt2 = dLdt3*dt3/dt2
        let dLdt1 = dLdt2*dt2/dt1
        this.gradL = dLdt1*dt1/dw

        // adjusting weight
        this.weight -= this.gradL*LR
    }

}


// setup function definition---------------------------------------------------
let ball1;
let n1;
function setup(){
    createCanvas(width, height)

    // converting target width to pixels
    t_width_px = map(target_width, 0,1, 0,height/2)

    // fixing y location of target
    target_y_px = random(t_width_px,height-t_width_px)
    target_y    = map(target_y_px,0,height,ylim[1],ylim[0])

    // creating ball and neuron objects
    ball1 = new Ball()
    n1    = new Neuron(target_y)

    // saving frames
    saveFrames("image","png",25,10)

}

// draw function definition----------------------------------------------------
function draw(){
    background(255)

    draw_target(target_y_px)

    // drawing pathline
    strokeWeight(0.01)
    line(10,height/2,width, map(xlim[1]*tan(ball1.angle),ylim[0],ylim[1],height,0))

    ball1.show()
    ball1.update()

    // resetting ball position
    if (ball1.pos_px > width){
        let yval = ball1.position.y
        ball1.position = createVector(0,0)
        n1.optimize()
        let val = n1.activation()
        ball1.angle = PI/2.0*val - PI/4.0
        count += 1
    }


    stroke(0)
    strokeWeight(1)
    fill(0)
    textSize(20)
    text("Attempt = "+str(count), width/2-120,20)
    let acc = (1-n1.L)*100
    text("Accuracy = "+str(round(acc,2))+" %", width/2+20,20)

    // drawing cannon
    draw_cannon(ball1.angle)
}
