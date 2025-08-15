Table dataTable;

int rowCount=100000;

float x[] = new float[rowCount];
float y[] = new float[rowCount];
float z[] = new float[rowCount];
float L[] = new float[rowCount];

float xMax=0, xMin=0;
float yMax=0, yMin=0;
float zMax=0, zMin=0;
float LMax=0, LMin=0;

float angle=0;

float cameraRadius;

float colorSwitcher(float LVal){
    float hueValue = 1.0/(1.0+exp(-5*LVal))*(0-220)+220;
    return hueValue;
}

void setup(){
    size(400,400,P3D);

    dataTable = loadTable("solutionData.csv","header");

    // filling data
    int idx=0;
    for(TableRow row: dataTable.rows()){
        x[idx] = row.getFloat("x");
        y[idx] = row.getFloat("y");
        z[idx] = row.getFloat("z");
        L[idx] = row.getFloat("L");
        idx++;
    }

    // finding max and min values
    for(idx=0; idx < rowCount; idx++){
        if(x[idx] > xMax)
            xMax = x[idx];
        if(x[idx] < xMin)
            xMin = x[idx];
        if(y[idx] > yMax)
            yMax = y[idx];
        if(y[idx] < yMin)
            yMin = y[idx];
        if(z[idx] > zMax)
            zMax = z[idx];
        if(z[idx] < zMin)
            zMin = z[idx];
        if(L[idx] > LMax)
            LMax = L[idx];
        if(L[idx] < LMin)
            LMin = L[idx];
    }

    cameraRadius = width/10;

    camera(cameraRadius*cos(angle)+width/2,height/2,cameraRadius*sin(angle)+height/2,
    width/2,height/2,height/2,0,1,0);
}

void draw(){
    colorMode(RGB,255,255,255);
    background(220,224,232);

    float xStart=x[0],yStart=y[0],zStart=z[0];
    float xEnd=x[1],yEnd=y[1],zEnd=z[1];


    pushMatrix();
    translate(width/2,height/2,height/2);
    scale(width/(xMax-xMin)*0.1);
    strokeWeight(0.01);
    colorMode(HSB,360,100,100);
    for(int i=1; i<rowCount; i++){
        float hueVal = colorSwitcher(L[i]);
        stroke(hueVal, 79, 105);
        xEnd = x[i];
        yEnd = y[i];
        zEnd = z[i];
        xStart = x[i-1];
        yStart = y[i-1];
        zStart = z[i-1];
        line(xStart,yStart,zStart,xEnd,yEnd,zEnd);
    }
    popMatrix();

    ortho(); // orthogonal projection

    camera(cameraRadius*cos(angle)+width/2,height/2,cameraRadius*sin(angle)+height/2,
    width/2,height/2,height/2,0,1,0);

    angle += 1/30.0/PI;

    if(angle > 2*PI)
        noLoop();
    saveFrame("line-######.png");
}

