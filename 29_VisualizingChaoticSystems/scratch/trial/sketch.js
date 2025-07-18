
let cam; // camera variable
let camResetButton;

let dt = 1e-3; // simulation timestep
let Tstop = 100.0; // simulation end time

let x = [-1]; // initial conditions
let y = [0];
let z = [0];

let xRange = [-4,1]; // range of coordinates
let yRange = [-3,3];
let zRange = [-5,3];

let frDiv; // other variables definition
let simTime=0;
let x1 = x[0];
let y1 = y[0];
let z1 = z[0];
let x2 = x1;
let y2 = y1;
let z2 = z1;

// equation function definition
function f(xVal,yVal,zVal){
    xDot = zVal;
    yDot = xVal*yVal+xVal*zVal;
    zDot = -0.1*x**3;
    vec = createVector(xDot,yDot,zDot);
    return vec;
}

// setup function
function setup() {
    // createCanvas(800, 500, WEBGL);
    createCanvas(800, 500, WEBGL);
    debugMode(GRID);

    // camera definition
    cam = createCamera();
    cam.setPosition(30,-80,150);
    cam.lookAt(0,0,0);

    // camera reset button
    camResetButton = createButton('reset view');
    camResetButton.mousePressed(resetView);
    camResetButton.position(0,100);

    describe('JCS-08-13-2022 System',LABEL);
    frDiv = createDiv('');
}
function draw() {

    background(220,224,232);

    orbitControl(); // 3d navigation with mouse

    // computing solution using RK4 integration
    let k1 = f(x1,y1,z1);
    let k2 = f(x1+k1.x/2*dt,y1+k1.y/2*dt,z1+k1.z/2*dt);
    let k3 = f(x1+k2.x/2*dt,y1+k2.y/2*dt,z1+k2.z/2*dt);
    let k4 = f(x1+k3.x*dt,y1+k3.y*dt,z1+k3.z*dt);
    x2 = x1 + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    y2 = y1 + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    z2 = z1 + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    x.push(x2);
    y.push(y2);
    z.push(z2);

    // updating simulation time
    simTime += dt;

    // rotateY(millis()*0.001);
    drawCoordinateAxes();
    frDiv.html("Time: " + nf(simTime, 2, 2)+' s'); // Update the div with framerate

    // drawing solution curve
    drawSolution();

    if(simTime > Tstop)
        noLoop();

}

function drawCoordinateAxes(){
    let axisScale=1;
    // center sphere
    fill(76,79,105);
    stroke(76,79,105);
    sphere(axisScale);

    // x-axis
    push();
    fill(210,15,57);
    stroke(210,15,57);
    translate(5*axisScale,0,0);
    rotateZ(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(210,15,57);
    stroke(210,15,57);
    translate(10.5*axisScale,0,0);
    rotateZ(-PI/2);
    cone(axisScale,axisScale);
    pop();

    // y-axis
    push();
    fill(64,160,43);
    stroke(64,160,43);
    translate(0,-5*axisScale,0);
    // rotateZ(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(64,160,43);
    stroke(64,160,43);
    translate(0,-10.5*axisScale,0);
    rotateZ(-PI);
    cone(axisScale,axisScale);
    pop();

    // z-axis
    push();
    fill(30,102,245);
    stroke(30,102,245);
    translate(0,0,5*axisScale);
    rotateX(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(30,102,245);
    stroke(30,102,245);
    translate(0,0,10.5*axisScale);
    rotateX(PI/2);
    cone(axisScale,axisScale);
    pop();

}

function resetView(){
    cam.setPosition(30,-80,150);
    cam.lookAt(0,0,0);
}

// draw the solution curve
function drawSolution(){
    for(let i=1; i<x.size-1; i+= 1){
        stroke(0);
        let xStart = x[i-1]*(xRange[1]-xRange[0])+xRange[0];
        let yStart = y[i-1]*(yRange[1]-yRange[0])+yRange[0];
        let zStart = z[i-1]*(zRange[1]-zRange[0])+zRange[0];
        let xEnd   = x[i]*(xRange[1]-xRange[0])+xRange[0];
        let yEnd   = y[i]*(yRange[1]-yRange[0])+yRange[0];
        let zEnd   = z[i]*(zRange[1]-zRange[0])+zRange[0];
        line(xStart,yStart,zStart,xEnd,yEnd,zEnd);
    }
}
