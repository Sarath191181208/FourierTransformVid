class Particle {
  constructor(pos, target, hue, mforce, mspeed, radius) {
    this.pos = pos.copy();
    this.radius = radius;

    this.hue = hue;
    this.saturation = 70;

    this.vel = createVector();
    this.acc = createVector();

    this.target = target.copy();

    this.maxForce = mforce || 0.3;
    this.maxSpeed = mspeed || 4;
  }
  behaviours() {
    const seek = this.seek(this.target);
    this.applyForce(seek);
  }
  seek(target) {
    const desired = p5.Vector.sub(target, this.pos);
    const dist = desired.mag();
    let speed = this.maxSpeed;
    if (dist < 50) {
      speed = map(dist, 0, 50, 0, this.maxSpeed);
    }
    desired.setMag(speed);
    const steer = p5.Vector.sub(desired, this.vel);
    steer.limit(this.maxForce);
    return steer;
  }

  draw(h, s, v) {
    push();
    noStroke();
    fill(h, s, v);
    ellipse(this.pos.x, this.pos.y, this.radius);
    pop();
  }
  update() {
    // this.draw();
    this.behaviours();
    // this.target.add(gravity);
    this.pos.add(this.vel);
    this.vel.add(this.acc);
    this.acc.mult(0);
  }
  applyForce(force) {
    this.acc.add(force);
  }
}
