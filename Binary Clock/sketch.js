var clock;
var binClock;

var cols = 6;
var rows = 4;

var w = 100;
var h = 40;

function Clock(max) {
  this.time = [0,0,0,0];
  this.max = max;
}

Clock.prototype.inc = function(i) {
    this.time[i] += 1;
}

Clock.prototype.zero = function(i) {
  this.time[i] = 0;
}

Clock.prototype.carry = function() {
  if (this.time[0] == 10) {
    this.zero(0);
    this.inc(1);
  }
  for (var i = 1; i < 3; i++) {
    if (this.time[i] >= this.max) {
      this.zero(i);
      this.inc(i+1);
    }
  }
}

Clock.prototype.toBinary = function() {
  var bin = "";
  var temp;

  for (var i = 0; i < 4; i++) {
    if ((i == 1 || i == 2) && (this.time[i] / 10 < 1)) {
      temp = "0" + this.time[i];
    }
    else {
      temp = "" + this.time[i];
    }

    for (var j = (temp.length - 1); j >= 0; j--)
    {
      var digit = (temp.charAt(j) >>> 0).toString(2);
      var num = pad(digit, rows);
      bin = num + bin; // hr ... milli
    }
  }

  return bin;
}

Clock.prototype.end = function() {
  return (this.time[3] == 9);
}

Clock.prototype.update = function() {
  var t = "";
  t = pad(this.time[3],2) + ":" + pad(this.time[2],2)
                          + ":" + pad(this.time[1],2) + "." + this.time[0];
  if (t.substring(0,2) == "00") {
    t = "   " + t.substring(3);
  }

  return t;
}

Clock.prototype.show = function() {
  fill(color("black"));
  text(this.update(), 0, 200);
  textSize(40);
  textAlign(LEFT);


}

//-------------------------------------
function pad(num, amt) {
  var bin = num + "";
  while (bin.length < amt) {
    bin = "0" + bin;
  }

  return bin;
}

function make2DArray() {
  var arr = new Array(rows);

  for (var i = 0; i < arr.length; i++) {
    arr[i] = new Array(cols);
  }

  return arr;
}

//-------------------------------------
function BinClock() {
  this.grid = make2DArray();
}

BinClock.prototype.fill = function() {
  for (var r = 0; r < rows; r++) {
    for (var c = 0; c < cols; c++) {
      this.grid[r][c] = new Bit(c*w, r*h, 0);
    }
  }
}

BinClock.prototype.set = function(bin) {
  bin = bin.split("");
  for (var c = 0; c < cols; c++) {
    for (var r = 0; r < rows; r++) {
      this.grid[r][c].set(bin.shift());
    }
  }
}

BinClock.prototype.show = function() {
  for (var r = 0; r < rows; r++) {
    for (var c = 0; c < cols; c++) {
      this.grid[r][c].show();
    }
  }
}

//-------------------------------------
function Bit(x, y, val) {
  this.x = x;
  this.y = y;
  this.val = val;
}

Bit.prototype.set = function(val) {
  this.val = val;
}

Bit.prototype.show = function() {
  //text(this.val, this.x, this.y, w, h);
  //textAlign(CENTER, CENTER);

  if (this.val == "1") {
    fill(color('turquoise'));
  }
  else {
    noFill();
  }
  stroke(color("lightgrey"));
  rect(this.x, this.y, w, h);

}

//-------------------------------------
function setup() {
  createCanvas(1000,1000);
  clock = new Clock(60);
  binClock = new BinClock();
  binClock.fill();

}

function draw(){
  background(255);
  frameRate(10);

  if (!clock.end()) {
    clock.inc(0);
    clock.carry();

    binClock.set(clock.toBinary());
  }

  binClock.show();
  clock.show();
}
