// Simplest Chaotic System
let dt = 5e-2; // simulation timestep
let Tstop = 100.0; // simulation end time

let x = [-1]; // initial conditions
let y = [0];
let z = [0];
let LL = [0]; // local lyapunov
let r0 = 1e-8; // perturbation value

let xRange = [-9,9]; // range of coordinates
let yRange = [-9,9];
let zRange = [-9,9];

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
let hueCoeff = 1.5; // hue slope coeff. for lyapunov coloring
let hueOff = 2.2; // hue slope coeff. for lyapunov coloring

// equation function definition
function f(xVal,yVal,zVal){
    xDot = yVal;
    yDot = zVal;
    zDot = -2.02*zVal+yVal**2-xVal;
    vec = createVector(xDot,yDot,zDot);
    return vec;
}

// setup function
function setup() {
    createCanvas(800, 500, WEBGL);

    // setting colormode
    colorMode(HSL);

    // camera definition
    cam = createCamera();
    cam.setPosition(60,-160,300);
    cam.lookAt(0,0,0);

    // camera reset button
    camResetButton = createButton('reset view');
    camResetButton.mousePressed(resetView);
    camResetButton.position(0,0);

    // simulation time entry
    simTimePrompt = createElement('h5','sim. end time (s)');
    simTimePrompt.position(90,-20);
    simTimeInput = createInput(Tstop);
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

    describe('Simplest Chaotic System',LABEL);
    frDiv = createDiv('');

    let scaleFactor = height;

    // setting min and max range values
    xMinVal = -(-scaleFactor/2*xRange[1]-scaleFactor/2*xRange[0])/(xRange[0]-xRange[1]);
    xMaxVal = (-scaleFactor/2-xMinVal)/xRange[0]+xMinVal;
    yMinVal = -(-scaleFactor/2*yRange[1]-scaleFactor/2*yRange[0])/(yRange[0]-yRange[1]);
    yMaxVal = (-scaleFactor/2-yMinVal)/yRange[0]+yMinVal;
    zMinVal = -(-scaleFactor/2*zRange[1]-scaleFactor/2*zRange[0])/(zRange[0]-zRange[1]);
    zMaxVal = (-scaleFactor/2-zMinVal)/zRange[0]+zMinVal;
}
// main draw function
function draw() {

    background(220,21,89);

    orbitControl(); // 3d navigation with mouse

    if(simTime < Tstop && startSimulation){
        integrator();
        // updating simulation time
        simTime += dt;
        print(max(LL),min(LL));
    }

    // rotateY(millis()*0.001);
    drawCoordinateAxes();
    drawGrid();
    frDiv.html("Time: " + nf(simTime, 2, 2)+' / '+Tstop+' s'); // Update the div with framerate

    // drawing solution curve
    drawSolution();

}

// coordinates draw function
function drawCoordinateAxes(){
    let axisScale=2;
    // center sphere
    fill(234,16,35);
    stroke(234,16,35);
    sphere(axisScale);

    // x-axis
    push();
    fill(347,87,44);
    stroke(347,87,44);
    translate(5*axisScale,0,0);
    rotateZ(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(347,87,44);
    stroke(347,87,44);
    translate(10.5*axisScale,0,0);
    rotateZ(-PI/2);
    cone(axisScale,axisScale);
    pop();

    // y-axis
    push();
    fill(109,58,40);
    stroke(109,58,40);
    translate(0,-5*axisScale,0);
    // rotateZ(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(109,58,40);
    stroke(109,58,40);
    translate(0,-10.5*axisScale,0);
    rotateZ(-PI);
    cone(axisScale,axisScale);
    pop();

    // z-axis
    push();
    fill(220,91,54);
    stroke(220,91,54);
    translate(0,0,5*axisScale);
    rotateX(PI/2);
    cylinder(0.5*axisScale,10*axisScale);
    pop();
    push();
    fill(220,91,54);
    stroke(220,91,54);
    translate(0,0,10.5*axisScale);
    rotateX(PI/2);
    cone(axisScale,axisScale);
    pop();

}

// reset view button function
function resetView(){
    cam.setPosition(60,-160,300);
    cam.lookAt(0,0,0);
}

// hue function based on local lyapunov exponent
function hueVal(Lval){
    val = (1/(1+exp(-hueCoeff*Lval+hueOff)))*(0-220)+220;
    return val;
}

// draw the solution curve
function drawSolution(){
    let xStart,yStart,zStart;
    let xEnd,yEnd,zEnd;
    let xSize = x.length;
    for(let i=1; i<xSize; i=i+1){
        stroke(hueVal(LL[i]),87,44);
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
    stroke(234,16,35);
    fill(234,16,35);
    sphere(1);
    pop();
}

// RK4 integrator function
function integrator(){
    // computing solution using RK4 integration
    let k1 = f(x1,y1,z1);
    let k2 = f(x1+k1.x/2*dt,y1+k1.y/2*dt,z1+k1.z/2*dt);
    let k3 = f(x1+k2.x/2*dt,y1+k2.y/2*dt,z1+k2.z/2*dt);
    let k4 = f(x1+k3.x*dt,y1+k3.y*dt,z1+k3.z*dt);
    let x2 = x1 + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    let y2 = y1 + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    let z2 = z1 + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    x.push(x2);
    y.push(y2);
    z.push(z2);

    // perturbing x direction
    let xp = x1+r0;
    k1 = f(xp,y1,z1);
    k2 = f(xp+k1.x/2*dt,y1+k1.y/2*dt,z1+k1.z/2*dt);
    k3 = f(xp+k2.x/2*dt,y1+k2.y/2*dt,z1+k2.z/2*dt);
    k4 = f(xp+k3.x*dt,y1+k3.y*dt,z1+k3.z*dt);
    let xpf = xp + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    let ypf = y1 + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    let zpf = z1 + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    let r = sqrt((xpf-x2)**2+(ypf-y2)**2+(zpf-z2)**2)
    let Lx = log(r/r0)/dt;

    // perturbing y direction
    let yp = y1+r0;
    k1 = f(x1,yp,z1);
    k2 = f(x1+k1.x/2*dt,yp+k1.y/2*dt,z1+k1.z/2*dt);
    k3 = f(x1+k2.x/2*dt,yp+k2.y/2*dt,z1+k2.z/2*dt);
    k4 = f(x1+k3.x*dt,yp+k3.y*dt,z1+k3.z*dt);
    xpf = x1 + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    ypf = yp + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    zpf = z1 + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    r = sqrt((xpf-x2)**2+(ypf-y2)**2+(zpf-z2)**2)
    let Ly = log(r/r0)/dt;

    // perturbing z direction
    let zp = z1+r0;
    k1 = f(x1,y1,zp);
    k2 = f(x1+k1.x/2*dt,y1+k1.y/2*dt,zp+k1.z/2*dt);
    k3 = f(x1+k2.x/2*dt,y1+k2.y/2*dt,zp+k2.z/2*dt);
    k4 = f(x1+k3.x*dt,y1+k3.y*dt,zp+k3.z*dt);
    xpf = x1 + dt/6*(k1.x+2*k2.x+2*k3.x+k4.x);
    ypf = y1 + dt/6*(k1.y+2*k2.y+2*k3.y+k4.y);
    zpf = zp + dt/6*(k1.z+2*k2.z+2*k3.z+k4.z);
    r = sqrt((xpf-x2)**2+(ypf-y2)**2+(zpf-z2)**2)
    let Lz = log(r/r0)/dt;

    // determining largest lyapunov exponent
    if (abs(Lx) > abs(Ly) && abs(Lx) > abs(Lz))
        LL.push(Lx)
    else if (abs(Ly) > abs(Lx) && abs(Ly) > abs(Lz))
        LL.push(Ly)
    else
        LL.push(Lz)

    // resetting values
    x1 = x2;
    y1 = y2;
    z1 = z2;

}

// grid draw function
function drawGrid(){
    stroke(223,16,83);
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
