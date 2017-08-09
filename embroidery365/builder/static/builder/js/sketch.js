var img;

function setup() {
  let canvas = createCanvas(640, 480);
  canvas.parent('builder-canvas');

  img = createImage("http://images.clipartpanda.com/shirt-clip-art-t-shirt-clip-art-7.gif");
  img.hide();

  background(0);
  image(img, 0, 0);
}

function draw() {
  // background('#666');
  // if (mouseIsPressed) {
  //   fill(0);
  // } else {
  //   fill(255);
  // }
  // ellipse(mouseX, mouseY, 80, 80);
}
