function setup() {
  createCanvas(800, 800, WEBGL);
  // debugMode();
  describe('drawing coordinate axes');
}
function draw() {
  background(220,224,232);

  orbitControl();
  // rotateY(millis()*0.001);
  drawCoordinateAxes();
}

function drawCoordinateAxes(){
    let axisScale=10;
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
