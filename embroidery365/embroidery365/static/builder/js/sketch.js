let img, x, y;
let shirt_div_width = document.getElementById('shirt-container').offsetWidth;
let shirt_div_height, shirt_width, shirt_height;

function preload() {
  img = loadImage('../static/builder/img/shirt.png');
}

function setup() {

  let canvas = createCanvas(shirt_div_width, windowHeight*0.40);

  canvas.parent('shirt-container');
  x = y = -999999;
  shirt_div_height = windowHeight*0.40;

  // console.log(img.width/shirt_div_width)

  dims = scale_shirt(img, shirt_div_height);

  shirt_width = dims[0]; //img.width*0.42;
  shirt_height = dims[1]; //img.height*0.42;
}



function draw() {
  background('#FFF');


  image(img, width/2 - shirt_width/2, height/2 - shirt_height/2, shirt_width, shirt_height);
  noFill();
  stroke('#333');
  strokeWeight(2);
  ellipse(x,y,40,40);

}

function mouseClicked() {
  if(mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
    x = mouseX;
    y = mouseY;
  }
}

function scale_shirt(img, oh) {
  let og_width = img.width;
  let og_height = img.height;

  let ratio = get_height_ratio(og_height, oh) - 0.05;

  console.log(ratio);

  let n_width = og_width * ratio;
  let n_height = og_height * ratio;

  return [n_width, n_height];
}

function get_height_ratio(img_h, cont_h) {
  if(img_h > cont_h){
    console.log('img > container')
    return cont_h/img_h;
  } else {
    console.log('container > img')
    return img_h/cont_h;
  }
}


function windowResized() {
  shirt_div_width = document.getElementById('shirt-container').offsetWidth;

  dims = scale_shirt(img, shirt_div_height);

  shirt_width = dims[0]; //img.width*0.42;
  shirt_height = dims[1]

  // shirt_width = shirt_div_width;
  // shirt_height = windowHeight*0.40;
  resizeCanvas(shirt_div_width, windowHeight*0.40);
}
