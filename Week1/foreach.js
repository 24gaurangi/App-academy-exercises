Array.prototype.myforEach=function(fn){
  for(var i=0;i<this.length;i++){
    fn(this[i]);
  }
};

[1,2,3].myforEach(function(x){console.log(x); });