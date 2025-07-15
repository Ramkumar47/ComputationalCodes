let button;

let width=800, height=800;
function setup(){
    createCanvas (width,height);

    button = createButton('start/stop');
    button.value("stop");
    button.position(0,100);

    button.mousePressed(startStopSimulation);

    describe('trial work');
}

x=0;

function draw(){
    background(17, 17, 27);

    fill(243, 139, 168);

    circle(x,400,50);
    if(button.value()==="start"){
        print(button.value());
        x++;
    }

    if(x>800)
        x=0;

    let base = createVector(0.05*width,height*0.95);
    let vec1 = createVector(width*0.08,0);
    let vec2 = createVector(0,-width*0.08);
    drawArrow(base,vec1)
    drawArrow(base,vec2)
    noStroke()
    fill(0)
    textSize(20)
    text("x",90,567)
    text("y",27,513)

}

function startStopSimulation(){
    let val = button.value();
    print(val);
    if(val==="start"){
        button.value("stop");
    }
    else{
        button.value("start");
    }
}

function drawArrow(base, vec ) {
    push();
    stroke(255);
    strokeWeight(3);
    fill(255);
    translate(base.x, base.y);
    line(0, 0, vec.x, vec.y);
    rotate(vec.heading());
    let arrowSize = 7;
    translate(vec.mag() - arrowSize, 0);
    triangle(0, arrowSize / 2, 0, -arrowSize / 2, arrowSize, 0);
    pop();
}


