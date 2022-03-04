
var fourier_pnts;
let time = 0;
let path = [];
let slider;

function setup() {
    createCanvas(800, 600);
    frameRate(60);
    colorMode(HSB);
    pixelDensity(1);

    drawing = get_path("Apple", 500);

    get_fourier_points();

    slider = createSlider(1, 500, 500, 1);
    slider.position(windowWidth / 2 - 150, windowHeight - 125);
    slider.style('width', '300px');
    slider.changed(reset);

    // console.log(fourier_pnts)
}

function reset() {
    change_path();
    path = [];
}

function draw() {
    background(230, 60, 20, 0.1);

    let v = epicycles(width / 2, height / 2, 0, fourier_pnts, slider.value());
    // path.unshift(v);

    var start_pos = createVector(v.x, v.y);
    var end_pos = createVector(v.x, v.y);
    var clr = 200
    var new_particle = new Particle(start_pos, end_pos, clr, null, null, 8);
    path.unshift(new_particle);

    draw_path(path);

    const dt = TWO_PI / fourier_pnts.length;
    time += dt;
    // time += 0.001

    if (time > TWO_PI) {
        time = 0;
        if (path.length > 2 * fourier_pnts.length) {
            path = path.slice(0, fourier_pnts.length);
        }
        path = [];
    }
}

function draw_path(path) {
    push();
    noFill();
    for (let i = 0; i < path.length - 1; i++) {
        let clr = map(i % fourier_pnts.length, 0, fourier_pnts.length, 0, 360)

        strokeWeight(5);
        stroke(clr, 60, 90);
        // stroke(305, 95, 49);

        let [x1, y1] = [path[i].pos.x, path[i].pos.y];
        let [x2, y2] = [path[i + 1].pos.x, path[i + 1].pos.y];

        if (dis(x1, y1, x2, y2) < 40) {
            beginShape();
            vertex(x1, y1);
            vertex(x2, y2);
            endShape();
        }

        pnt = path[i];
        // pnt.draw(clr, 60, 90);
        pnt.update()
    }
    pop();
}

function dis(x1, y1, x2, y2) {
    return Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
}

function change_path() {

    get_fourier_points();
    let t = 0;
    const _dt = TWO_PI / fourier_pnts.length;

    for (let i = 0; i < path.length; i++) {

        let [x, y] = get_points(t)

        t += _dt;

        let target = createVector(x, y);
        path[i].target = target;
    }
    time = 0;
}

function get_points(t) {
    let [x, y] = [width / 2, height / 2];
    for (let i = 0; i < fourier_pnts.length; i++) {

        let freq = fourier_pnts[i].freq;
        let radius = fourier_pnts[i].amp;
        let phase = fourier_pnts[i].phase;

        x += radius * cos(freq * t + phase);
        y += radius * sin(freq * t + phase);
    }
    return [x, y];
}


function epicycles(x, y, rotation, fourier, num_cycles) {
    for (let i = 0; i < num_cycles; i++) {

        let prevx = x;
        let prevy = y;
        let freq = fourier[i].freq;
        let radius = fourier[i].amp;
        let phase = fourier[i].phase;

        x += radius * cos(freq * time + phase + rotation);
        y += radius * sin(freq * time + phase + rotation);

        stroke(255, 255, 255, 0.5);
        noFill();
        ellipse(prevx, prevy, radius * 2);
        stroke(255, 0.5);
        line(prevx, prevy, x, y);
    }
    fill(255);
    ellipse(x, y, 10)
    return createVector(x, y);
}

function get_fourier_points() {
    let x = []
    fourier_pnts = [];
    const step = 1;
    // let prev = []
    for (let i = 0; i < drawing.length; i += step) {
        const c = new Complex(drawing[i].x, drawing[i].y);
        // prev.push(drawing[i]);
        x.push(c);
    }

    fourier_pnts = dft(x);
    fourier_pnts.sort((a, b) => b.amp - a.amp);
}



function dft(x) {
    const X = [];
    const N = x.length;
    const num_cycles = N;
    for (let k = 0; k < num_cycles; k++) {
        let sum = new Complex(0, 0);
        for (let n = 0; n < N; n++) {
            const phi = (TWO_PI * k * n) / N;
            const c = new Complex(cos(phi), -sin(phi));
            sum.add(x[n].mult(c));
        }
        sum.re = sum.re / N;
        sum.im = sum.im / N;

        let freq = k;
        let amp = sqrt(sum.re * sum.re + sum.im * sum.im);
        let phase = atan2(sum.im, sum.re);
        X[k] = { re: sum.re, im: sum.im, freq, amp, phase };
    }
    // X.splice(0, 1);
    return X;
}