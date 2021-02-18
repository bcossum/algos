class BTNode {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  add(val) {
    if(this.root) {
      var runner = this.root;
      while(runner) {
        if(val>=runner.val) {
          if(runner.right){
            runner = runner.right;
          }
          else {
            runner.right = new BTNode(val)
            return this
          }
        }
        else {
          if(runner.left) {
            runner = runner.left;
          }
          else {
            runner.left = new BTNode(val);
            return this
          }
        }
      }
    }
    this.root = new BTNode(val);
    return this
  }

  contains(val){
    var runner = this.root;
    while (runner){
      if (runner.val == val){
        return "Yes it does contain " + val;
      }
      if (val < runner.val){
        runner = runner.left;
      }
      else {
        runner = runner.right;
      }
    }

    return "No it does not contain " + val;
  }

  min() {
    var runner = this.root;
    var min = this.root.val;
    while (runner.left){
      if(runner.left.val < min) {
        min = runner.left.val;
      }
      runner = runner.left;
    }
    return min
  }

  max() {
    var runner = this.root;
    var max = this.root.val;
    while (runner.right){
      if (runner.right.val > max){
        max = runner.right.val;
      }
      runner = runner.right
    }
    return max
  }

  size() {
    if (this.root === null) {
      return 0;
    }
    function sizeHelp(runner) {
      if (!runner) {
        return 0;
      }
      return 1 + sizeHelp(runner.left) + sizeHelp(runner.right);
    }
    return sizeHelp(this.root)
  }

  isEmpty() {
    if (this.root){
      return "Not Empty"
    }
    else {
      return "Empty"
    }
  }
}

var myNode = new BST()
myNode.add(10);
myNode.add(9);
myNode.add(30);
myNode.add(12);
myNode.add(13);
console.log(myNode.size())