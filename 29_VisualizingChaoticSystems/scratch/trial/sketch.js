
let dt = 5e-2; // simulation timestep
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
let xMinVal;
let xMaxVal;
let yMinVal;
let yMaxVal;
let zMinVal;
let zMaxVal;
let cam; // camera variable
let camResetButton;
let simulationResetButton;
let startSimulation=false;

// equation function definition
function f(xVal,yVal,zVal){
    xDot = zVal*1.0;
    yDot = xVal*yVal+xVal*zVal;
    zDot = -0.1*xVal**3+yVal**3;
    vec = createVector(xDot,yDot,zDot);
    return vec;
}

// setup function
function setup() {
    createCanvas(800, 500, WEBGL);

    // camera definition
    cam = createCamera();
    cam.setPosition(30,-80,150);
    cam.lookAt(0,0,0);

    // camera reset button
    camResetButton = createButton('reset view');
    camResetButton.mousePressed(resetView);
    camResetButton.position(0,0);

    // simulation time entry
    simTimePrompt = createElement('h5','sim. end time (s)');
    simTimePrompt.position(90,-20);
    simTimeInput = createInput(100);
    simTimeInput.size(30);
    simTimeInput.position(205,0);

    // start stop button
    startStopButton = createButton('start/stop');
    startStopButton.mousePressed(startStopSimulation);
    startStopButton.position(simTimeInput.x+simTimeInput.width,0);

    // simulation reset button
    simulationResetButton = createButton('reset simulation');
    simulationResetButton.mousePressed(resetSimulation);
    simulationResetButton.position(startStopButton.x+startStopButton.width+20,0);

    describe('JCS-08-13-2022 System',LABEL);
    frDiv = createDiv('');

    let scaleFactor = 0.25*height;

    // setting min and max range values
    xMinVal = -(-scaleFactor/2*xRange[1]-scaleFactor/2*xRange[0])/(xRange[0]-xRange[1]);
    xMaxVal = (-scaleFactor/2-xMinVal)/xRange[0]+xMinVal;
    yMinVal = -(-scaleFactor/2*yRange[1]-scaleFactor/2*yRange[0])/(yRange[0]-yRange[1]);
    yMaxVal = (-scaleFactor/2-yMinVal)/yRange[0]+yMinVal;
    zMinVal = -(-scaleFactor/2*zRange[1]-scaleFactor/2*zRange[0])/(zRange[0]-zRange[1]);
    zMaxVal = (-scaleFactor/2-zMinVal)/zRange[0]+zMinVal;
}
function draw() {

    background(220,224,232);

    orbitControl(); // 3d navigation with mouse

    if(simTime < Tstop && startSimulation){
        integrator();
        // updating simulation time
        simTime += dt;
    }

    // rotateY(millis()*0.001);
    drawCoordinateAxes();
    drawGrid();
    frDiv.html("Time: " + nf(simTime, 2, 2)+' / '+Tstop+' s'); // Update the div with framerate

    // drawing solution curve
    drawSolution();

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
    let xStart,yStart,zStart;
    let xEnd,yEnd,zEnd;
    let xSize = x.length;
    for(let i=1; i<xSize; i=i+1){
        stroke(0);
        xStart = x[i-1]*(xMaxVal - xMinVal)+xMinVal;
        yStart = y[i-1]*(yMaxVal - yMinVal)+yMinVal;
        zStart = z[i-1]*(zMaxVal - zMinVal)+zMinVal;
        xEnd   = x[i]*(xMaxVal - xMinVal)+xMinVal;
        yEnd   = y[i]*(yMaxVal - yMinVal)+yMinVal;
        zEnd   = z[i]*(zMaxVal - zMinVal)+zMinVal;
        line(xStart,-yStart,zStart,xEnd,-yEnd,zEnd);
    }
    push();
    translate(xEnd,-yEnd,zEnd);
    fill(210,15,57);
    sphere(1);
    pop();
    // print(xEnd,yEnd,zEnd);
}

// RK4 integrator function
function integrator(){
    // computing solution using RK4 integration
    let k1 = f(x1,y1,z1);
    let k2 = f(x1+k1.x/2*dt,y1+k1.y/2*dt,z1+k1.z/2*dt);
    let k3 = f(x1+k2.x/2*dt,y1+k2.y/2*dt,z1+k2.z/2*dt);
    let k4 = f(x1+k3.x*dt,y1+k3.y*dt,z1+k3.z*dt);
    x1 = x1 + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    y1 = y1 + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    z1 = z1 + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    x.push(x1);
    y.push(y1);
    z.push(z1);

}

// grid draw function
function drawGrid(){
    stroke(188,192,204);
    let xVal = xRange[0];
    while(xVal <=xRange[1]){
        xStart = xVal*(xMaxVal - xMinVal)+xMinVal;
        zStart = zRange[0]*(zMaxVal - zMinVal)+zMinVal;
        zEnd   = zRange[1]*(zMaxVal - zMinVal)+zMinVal;
        line(xStart,0,zStart,xStart,0,zEnd);
        xVal += 1;
    }
    let zVal = zRange[0];
    while(zVal <=zRange[1]){
        zStart = zVal*(zMaxVal - zMinVal)+zMinVal;
        xStart = xRange[0]*(xMaxVal - xMinVal)+xMinVal;
        xEnd   = xRange[1]*(xMaxVal - xMinVal)+xMinVal;
        line(xStart,0,zStart,xEnd,0,zStart);
        zVal += 1;
    }
}

// simulation reset function
function resetSimulation(){
    x = [-1]; // initial conditions
    y = [0];
    z = [0];
    x1 = x[0];
    y1 = y[0];
    z1 = z[0];
    simTime=0;
    startSimulation = false;
}

// start stop simulation
function startStopSimulation(){
    Tstop = simTimeInput.value();
    if (startSimulation)
        startSimulation = false;
    else
        startSimulation = true;
}
