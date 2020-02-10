#!/usr/bin/node
// Rectangle Class
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 && (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
